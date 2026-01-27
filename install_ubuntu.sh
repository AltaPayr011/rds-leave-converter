#!/bin/bash
# Automated installation script for RDS Leave Converter
# For Ubuntu 20.04+ servers

set -e  # Exit on error

echo "=================================================="
echo "RDS PaySpace Leave Converter - Server Setup"
echo "=================================================="
echo ""

# Check if running as root
if [ "$EUID" -ne 0 ]; then 
    echo "❌ Please run as root (use sudo)"
    exit 1
fi

# Get server IP
SERVER_IP=$(hostname -I | awk '{print $1}')
echo "✅ Detected server IP: $SERVER_IP"
echo ""

# Update system
echo "📦 Updating system packages..."
apt update && apt upgrade -y

# Install required packages
echo "📦 Installing required packages..."
apt install -y python3-pip python3-venv nginx git ufw

# Create streamlit user if doesn't exist
if ! id "streamlit" &>/dev/null; then
    echo "👤 Creating streamlit user..."
    adduser --disabled-password --gecos "" streamlit
    echo "streamlit:streamlit123" | chpasswd
    echo "✅ Created user 'streamlit' with password 'streamlit123'"
    echo "⚠️  Please change this password after installation!"
else
    echo "✅ User 'streamlit' already exists"
fi

# Set up firewall
echo "🔒 Configuring firewall..."
ufw --force enable
ufw allow ssh
ufw allow 80/tcp
ufw allow 443/tcp
echo "✅ Firewall configured"

# Get app directory
read -p "Enter the path where app files are located [/home/streamlit/leave_breakdown_app]: " APP_DIR
APP_DIR=${APP_DIR:-/home/streamlit/leave_breakdown_app}

if [ ! -d "$APP_DIR" ]; then
    echo "❌ Directory $APP_DIR not found!"
    echo "Please upload your app files first and run this script again."
    exit 1
fi

# Set up Python environment
echo "🐍 Setting up Python environment..."
cd "$APP_DIR"
sudo -u streamlit python3 -m venv venv
sudo -u streamlit "$APP_DIR/venv/bin/pip" install -r requirements.txt
echo "✅ Python environment ready"

# Set up systemd service
echo "⚙️ Setting up systemd service..."
if [ -f "$APP_DIR/streamlit.service" ]; then
    sed "s|/home/streamlit/leave_breakdown_app|$APP_DIR|g" "$APP_DIR/streamlit.service" > /etc/systemd/system/streamlit.service
else
    cat > /etc/systemd/system/streamlit.service << EOF
[Unit]
Description=RDS PaySpace Leave Converter - Streamlit App
After=network.target

[Service]
Type=simple
User=streamlit
WorkingDirectory=$APP_DIR
Environment="PATH=$APP_DIR/venv/bin"
ExecStart=$APP_DIR/venv/bin/streamlit run app.py --server.port 8501 --server.address 0.0.0.0 --server.headless true
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF
fi

systemctl daemon-reload
systemctl enable streamlit
systemctl start streamlit
echo "✅ Streamlit service started"

# Set up Nginx
echo "🌐 Setting up Nginx..."
if [ -f "$APP_DIR/nginx.conf" ]; then
    cp "$APP_DIR/nginx.conf" /etc/nginx/sites-available/streamlit
    sed -i "s/YOUR_DOMAIN_OR_IP/$SERVER_IP/g" /etc/nginx/sites-available/streamlit
else
    cat > /etc/nginx/sites-available/streamlit << EOF
server {
    listen 80;
    server_name $SERVER_IP;
    client_max_body_size 100M;
    
    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade \$http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
        proxy_buffering off;
    }
}
EOF
fi

ln -sf /etc/nginx/sites-available/streamlit /etc/nginx/sites-enabled/
rm -f /etc/nginx/sites-enabled/default
nginx -t && systemctl reload nginx
echo "✅ Nginx configured"

# Set up backup cron job
echo "💾 Setting up daily backups..."
BACKUP_SCRIPT="/home/streamlit/backup.sh"
cat > "$BACKUP_SCRIPT" << 'EOF'
#!/bin/bash
BACKUP_DIR="/home/streamlit/backups"
APP_DIR="/home/streamlit/leave_breakdown_app"
DATE=$(date +%Y%m%d_%H%M%S)
mkdir -p $BACKUP_DIR
cp $APP_DIR/employee_data.csv $BACKUP_DIR/employee_data_$DATE.csv 2>/dev/null || true
cp $APP_DIR/users.csv $BACKUP_DIR/users_$DATE.csv 2>/dev/null || true
find $BACKUP_DIR -name "*.csv" -mtime +30 -delete
echo "Backup completed: $DATE"
EOF

sed -i "s|/home/streamlit/leave_breakdown_app|$APP_DIR|g" "$BACKUP_SCRIPT"
chmod +x "$BACKUP_SCRIPT"
chown streamlit:streamlit "$BACKUP_SCRIPT"

# Add to crontab
(sudo -u streamlit crontab -l 2>/dev/null; echo "0 2 * * * /home/streamlit/backup.sh") | sudo -u streamlit crontab -
echo "✅ Backup configured (runs daily at 2 AM)"

# Check service status
sleep 3
if systemctl is-active --quiet streamlit; then
    echo ""
    echo "=================================================="
    echo "✅ Installation Complete!"
    echo "=================================================="
    echo ""
    echo "🌐 Your app is now running at:"
    echo "   http://$SERVER_IP"
    echo ""
    echo "📝 Default login credentials:"
    echo "   Username: admin"
    echo "   Password: admin123"
    echo "   ⚠️  Change this password immediately!"
    echo ""
    echo "📊 Useful commands:"
    echo "   Check status:  sudo systemctl status streamlit"
    echo "   View logs:     sudo journalctl -u streamlit -f"
    echo "   Restart app:   sudo systemctl restart streamlit"
    echo ""
    echo "📂 App location: $APP_DIR"
    echo "💾 Backups: /home/streamlit/backups"
    echo ""
    echo "🔐 Next steps:"
    echo "   1. Open http://$SERVER_IP in your browser"
    echo "   2. Login and change admin password"
    echo "   3. Add your team members"
    echo "   4. (Optional) Set up domain name and SSL"
    echo ""
else
    echo ""
    echo "=================================================="
    echo "❌ Installation completed but service not running"
    echo "=================================================="
    echo ""
    echo "Check logs with: sudo journalctl -u streamlit -n 50"
fi
