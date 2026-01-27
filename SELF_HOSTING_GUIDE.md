# 🖥️ Self-Hosting Guide - RDS PaySpace Leave Converter

## Complete Guide to Hosting on Your Own Server

Self-hosting gives you **full control** and **permanent data storage**. No more data loss when the app restarts!

---

## 📋 Table of Contents

1. [Server Requirements](#server-requirements)
2. [Hosting Options](#hosting-options)
3. [Option A: Ubuntu Server (Recommended)](#option-a-ubuntu-server-recommended)
4. [Option B: Windows Server](#option-b-windows-server)
5. [Option C: Docker (Advanced)](#option-c-docker-advanced)
6. [Security Setup](#security-setup)
7. [Domain Setup (Optional)](#domain-setup-optional)
8. [Maintenance](#maintenance)
9. [Troubleshooting](#troubleshooting)

---

## Server Requirements

### Minimum Requirements:
- **CPU:** 1 core (2 cores recommended)
- **RAM:** 1GB minimum (2GB recommended)
- **Storage:** 10GB minimum (20GB recommended)
- **OS:** Ubuntu 20.04+ or Windows Server 2019+
- **Network:** Static IP address or domain name
- **Bandwidth:** 10GB/month (light usage)

### Software Requirements:
- Python 3.8 or higher
- pip (Python package manager)
- (Optional) Nginx or Apache for reverse proxy
- (Optional) SSL certificate for HTTPS

### Cost Estimate:
- **VPS (Cloud):** $5-20/month
- **On-premises:** Hardware cost only
- **Dedicated Server:** $50-200/month

---

## Hosting Options

### Option 1: Cloud VPS (Virtual Private Server) 💻
**Best for:** Small to medium deployments

**Providers:**
- **DigitalOcean** - Droplets from $6/month
- **Linode** - Shared CPU from $5/month
- **Vultr** - Cloud Compute from $6/month
- **AWS Lightsail** - From $5/month
- **Azure** - B1S from $10/month
- **Google Cloud** - E2-micro from $7/month

**Pros:**
- ✅ Easy to set up
- ✅ Scalable
- ✅ Reliable
- ✅ Automatic backups available

**Cons:**
- ⚠️ Monthly cost
- ⚠️ Requires basic Linux knowledge

---

### Option 2: On-Premises Server 🏢
**Best for:** Companies with existing IT infrastructure

**Options:**
- Dedicated physical server
- Spare computer/workstation
- Virtual machine on existing server

**Pros:**
- ✅ One-time hardware cost
- ✅ Full physical control
- ✅ No monthly fees
- ✅ Data stays on-premises

**Cons:**
- ⚠️ Need to maintain hardware
- ⚠️ Need reliable internet
- ⚠️ Need backup solution
- ⚠️ Power and cooling costs

---

### Option 3: Company Cloud Account ☁️
**Best for:** Companies with existing cloud infrastructure

**Use your existing:**
- Microsoft Azure account
- Amazon AWS account
- Google Cloud Platform account

**Pros:**
- ✅ Use existing infrastructure
- ✅ Integrated with company systems
- ✅ IT team can manage

**Cons:**
- ⚠️ May need IT approval
- ⚠️ May have policies to follow

---

## Option A: Ubuntu Server (Recommended)

### Best for: Most users, VPS, or on-premises Linux server

This is the **most reliable and cost-effective** option.

### Step 1: Get a Server

**Cloud VPS (Recommended):**

1. **Sign up for DigitalOcean** (easiest for beginners):
   - Go to https://www.digitalocean.com
   - Create account
   - Add payment method

2. **Create a Droplet:**
   - Click "Create" → "Droplets"
   - Choose: **Ubuntu 22.04 LTS**
   - Plan: **Basic** ($6/month)
   - CPU: **Regular (1GB RAM)**
   - Region: Choose closest to you
   - Authentication: **SSH keys** (recommended) or **Password**
   - Click "Create Droplet"

3. **Get your server IP:**
   - Copy the IP address shown (e.g., `45.55.123.234`)

**OR On-Premises Server:**
- Install Ubuntu 22.04 on your server
- Ensure it has a static IP on your network
- Continue to Step 2

---

### Step 2: Connect to Your Server

**From Windows:**
```cmd
# Download PuTTY: https://putty.org
# Or use Windows Terminal with SSH:
ssh root@YOUR_SERVER_IP
```

**From Mac/Linux:**
```bash
ssh root@YOUR_SERVER_IP
```

Enter your password when prompted.

---

### Step 3: Initial Server Setup

Run these commands one by one:

```bash
# Update system
apt update && apt upgrade -y

# Install Python and required packages
apt install python3-pip python3-venv nginx certbot python3-certbot-nginx -y

# Create a user for the app (more secure than using root)
adduser streamlit
# Follow prompts to set password

# Add user to sudo group
usermod -aG sudo streamlit

# Switch to new user
su - streamlit
```

---

### Step 4: Upload Your App

**Option A: Using Git (Recommended)**

```bash
# Install git
sudo apt install git -y

# Clone your repository (if you have it on GitHub)
git clone https://github.com/your-username/rds-leave-converter.git
cd rds-leave-converter
```

**Option B: Using SCP (File Upload)**

On your local computer:
```bash
# Zip your app folder
cd leave_breakdown_app
zip -r app.zip .

# Upload to server
scp app.zip streamlit@YOUR_SERVER_IP:/home/streamlit/

# On server:
unzip app.zip
```

---

### Step 5: Set Up Python Environment

```bash
# Navigate to app directory
cd /home/streamlit/leave_breakdown_app

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

### Step 6: Test the App

```bash
# Run the app
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```

**Test it:**
- Open browser: `http://YOUR_SERVER_IP:8501`
- If you see the login screen: ✅ Success!
- Press Ctrl+C to stop

---

### Step 7: Run App as a Service (Auto-Start)

This keeps the app running 24/7 and auto-restarts if it crashes.

**Create service file:**

```bash
sudo nano /etc/systemd/system/streamlit.service
```

**Paste this content:**

```ini
[Unit]
Description=Streamlit Leave Converter
After=network.target

[Service]
Type=simple
User=streamlit
WorkingDirectory=/home/streamlit/leave_breakdown_app
Environment="PATH=/home/streamlit/leave_breakdown_app/venv/bin"
ExecStart=/home/streamlit/leave_breakdown_app/venv/bin/streamlit run app.py --server.port 8501 --server.address 0.0.0.0 --server.headless true
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

**Save and exit:** Ctrl+X, then Y, then Enter

**Enable and start the service:**

```bash
# Reload systemd
sudo systemctl daemon-reload

# Enable service (start on boot)
sudo systemctl enable streamlit

# Start service
sudo systemctl start streamlit

# Check status
sudo systemctl status streamlit
```

**You should see:** "Active: active (running)"

---

### Step 8: Set Up Nginx (Reverse Proxy)

This makes your app accessible on port 80 (standard web port) instead of 8501.

**Create Nginx configuration:**

```bash
sudo nano /etc/nginx/sites-available/streamlit
```

**Paste this content:**

```nginx
server {
    listen 80;
    server_name YOUR_SERVER_IP;  # Or your domain name

    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_buffering off;
    }
}
```

**Save and exit:** Ctrl+X, then Y, then Enter

**Enable the configuration:**

```bash
# Create symbolic link
sudo ln -s /etc/nginx/sites-available/streamlit /etc/nginx/sites-enabled/

# Remove default site
sudo rm /etc/nginx/sites-enabled/default

# Test configuration
sudo nginx -t

# Reload Nginx
sudo systemctl reload nginx
```

**Test it:**
- Open browser: `http://YOUR_SERVER_IP`
- No need for `:8501` anymore!

---

### Step 9: Enable HTTPS (Optional but Recommended)

**If you have a domain name:**

```bash
# Get free SSL certificate from Let's Encrypt
sudo certbot --nginx -d your-domain.com

# Follow prompts:
# - Enter email address
# - Agree to terms
# - Choose: Redirect HTTP to HTTPS (option 2)
```

**Your app is now at:** `https://your-domain.com` 🔒

**Auto-renewal:** Certbot automatically renews certificates.

---

### Step 10: Set Up Automatic Backups

**Create backup script:**

```bash
nano /home/streamlit/backup.sh
```

**Paste this content:**

```bash
#!/bin/bash
# Backup script for RDS Leave Converter

BACKUP_DIR="/home/streamlit/backups"
APP_DIR="/home/streamlit/leave_breakdown_app"
DATE=$(date +%Y%m%d_%H%M%S)

# Create backup directory if it doesn't exist
mkdir -p $BACKUP_DIR

# Backup employee data
cp $APP_DIR/employee_data.csv $BACKUP_DIR/employee_data_$DATE.csv 2>/dev/null

# Backup user data
cp $APP_DIR/users.csv $BACKUP_DIR/users_$DATE.csv 2>/dev/null

# Keep only last 30 days of backups
find $BACKUP_DIR -name "*.csv" -mtime +30 -delete

echo "Backup completed: $DATE"
```

**Make it executable:**

```bash
chmod +x /home/streamlit/backup.sh
```

**Schedule daily backups:**

```bash
# Open crontab
crontab -e

# Add this line (runs daily at 2 AM):
0 2 * * * /home/streamlit/backup.sh
```

---

## Option B: Windows Server

### Best for: Windows-based infrastructure

### Step 1: Prepare Windows Server

**Requirements:**
- Windows Server 2019 or later
- OR Windows 10/11 Pro

**Install Python:**
1. Download Python 3.11 from https://www.python.org/downloads/windows/
2. Run installer
3. ✅ Check "Add Python to PATH"
4. Click "Install Now"

---

### Step 2: Upload App Files

1. **Copy** your `leave_breakdown_app` folder to server
2. **Recommended location:** `C:\inetpub\leave_converter`

---

### Step 3: Install Dependencies

```cmd
# Open Command Prompt as Administrator
cd C:\inetpub\leave_converter

# Install dependencies
pip install -r requirements.txt
```

---

### Step 4: Test the App

```cmd
# Run the app
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```

**Test:** Open `http://localhost:8501` in browser

---

### Step 5: Run as Windows Service

**Option A: Using NSSM (Easiest)**

1. **Download NSSM:**
   - Go to https://nssm.cc/download
   - Extract to `C:\nssm`

2. **Install service:**
   ```cmd
   cd C:\nssm\win64
   nssm install StreamlitApp
   ```

3. **Configure in GUI:**
   - Path: `C:\Python311\Scripts\streamlit.exe`
   - Startup directory: `C:\inetpub\leave_converter`
   - Arguments: `run app.py --server.port 8501 --server.address 0.0.0.0 --server.headless true`
   - Click "Install service"

4. **Start service:**
   ```cmd
   net start StreamlitApp
   ```

**Option B: Using Task Scheduler**

1. Open Task Scheduler
2. Create Basic Task
3. Name: "Streamlit Leave Converter"
4. Trigger: When computer starts
5. Action: Start a program
6. Program: `C:\Python311\Scripts\streamlit.exe`
7. Arguments: `run app.py --server.port 8501 --server.address 0.0.0.0 --server.headless true`
8. Start in: `C:\inetpub\leave_converter`

---

### Step 6: Set Up IIS (Optional)

If you want to use IIS as reverse proxy:

1. **Install IIS:**
   - Server Manager → Add Roles → Web Server (IIS)

2. **Install URL Rewrite and ARR:**
   - Download from microsoft.com
   - Install both modules

3. **Configure reverse proxy in IIS**
   - (Advanced - see Microsoft documentation)

---

## Option C: Docker (Advanced)

### Best for: Advanced users, consistent deployments

### Dockerfile

Create `Dockerfile` in your app folder:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

# Create volume mount points for data persistence
VOLUME /app/data

# Expose port
EXPOSE 8501

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

# Run app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true"]
```

### docker-compose.yml

```yaml
version: '3.8'

services:
  streamlit:
    build: .
    ports:
      - "8501:8501"
    volumes:
      # Persist data files
      - ./data:/app/data
      - ./employee_data.csv:/app/employee_data.csv
      - ./users.csv:/app/users.csv
    restart: unless-stopped
    environment:
      - STREAMLIT_SERVER_HEADLESS=true
      - STREAMLIT_SERVER_PORT=8501
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8501/_stcore/health"]
      interval: 30s
      timeout: 10s
      retries: 3
```

### Deploy with Docker

```bash
# Build image
docker-compose build

# Start container
docker-compose up -d

# View logs
docker-compose logs -f

# Stop container
docker-compose down
```

---

## Security Setup

### 1. Firewall Configuration

**Ubuntu:**
```bash
# Enable firewall
sudo ufw enable

# Allow SSH
sudo ufw allow ssh

# Allow HTTP
sudo ufw allow 80/tcp

# Allow HTTPS
sudo ufw allow 443/tcp

# Check status
sudo ufw status
```

**Windows:**
```cmd
# Open Windows Firewall
# Add inbound rules for ports 80, 443, 8501
```

---

### 2. Keep System Updated

**Ubuntu:**
```bash
# Update weekly
sudo apt update && sudo apt upgrade -y
```

**Windows:**
- Enable Windows Update
- Install updates monthly

---

### 3. User Access Control

**Restrict SSH access (Ubuntu):**

```bash
# Edit SSH config
sudo nano /etc/ssh/sshd_config

# Change these settings:
PermitRootLogin no
PasswordAuthentication no  # Use SSH keys only
Port 2222  # Change default port

# Restart SSH
sudo systemctl restart sshd
```

---

### 4. Monitor Access

**Check who's accessing:**

```bash
# Ubuntu - View access logs
sudo tail -f /var/log/nginx/access.log

# View app logs
journalctl -u streamlit -f
```

---

## Domain Setup (Optional)

### If you want a custom domain like `leave.yourcompany.com`:

**Step 1: Get a domain name**
- Register at: Namecheap, GoDaddy, Google Domains

**Step 2: Point domain to your server**
1. Go to domain registrar
2. Find DNS settings
3. Add A Record:
   - Name: `leave` (or `@` for root domain)
   - Value: `YOUR_SERVER_IP`
   - TTL: 3600

**Step 3: Update Nginx config**
```bash
sudo nano /etc/nginx/sites-available/streamlit

# Change:
server_name YOUR_SERVER_IP;
# To:
server_name leave.yourcompany.com;

# Reload Nginx
sudo systemctl reload nginx
```

**Step 4: Enable HTTPS**
```bash
sudo certbot --nginx -d leave.yourcompany.com
```

---

## Maintenance

### Daily:
- ✅ Check app is accessible
- ✅ Verify backups are running

### Weekly:
- ✅ Review access logs
- ✅ Check disk space: `df -h`
- ✅ Check memory: `free -h`

### Monthly:
- ✅ Update system packages
- ✅ Review user accounts
- ✅ Test backup restoration

### Commands:

```bash
# Restart app
sudo systemctl restart streamlit

# View logs
journalctl -u streamlit -n 100

# Check status
sudo systemctl status streamlit

# Update app (if using Git)
cd /home/streamlit/leave_breakdown_app
git pull
sudo systemctl restart streamlit
```

---

## Troubleshooting

### App won't start:

```bash
# Check service status
sudo systemctl status streamlit

# View detailed logs
journalctl -u streamlit -n 200

# Test app manually
cd /home/streamlit/leave_breakdown_app
source venv/bin/activate
streamlit run app.py
```

### Can't access from browser:

```bash
# Check if port is open
sudo netstat -tulpn | grep 8501

# Check firewall
sudo ufw status

# Check Nginx
sudo systemctl status nginx
sudo nginx -t
```

### App is slow:

```bash
# Check resources
htop  # Install with: sudo apt install htop

# Restart services
sudo systemctl restart streamlit nginx
```

### Data files missing:

```bash
# Check permissions
ls -la /home/streamlit/leave_breakdown_app/*.csv

# Fix permissions
sudo chown streamlit:streamlit /home/streamlit/leave_breakdown_app/*.csv
```

---

## Cost Comparison

### Option 1: DigitalOcean Droplet
- **Cost:** $6/month ($72/year)
- **Includes:** 1GB RAM, 25GB SSD, 1TB transfer
- **Setup time:** 30 minutes
- **Maintenance:** 30 min/month

### Option 2: On-Premises
- **Hardware:** $200-500 one-time
- **Electricity:** ~$5-10/month
- **Setup time:** 1-2 hours
- **Maintenance:** 1 hour/month

### Option 3: Streamlit Cloud Pro
- **Cost:** $20-200/month
- **Setup time:** 5 minutes
- **Maintenance:** None

---

## Quick Start Summary

**Fastest way to self-host (Ubuntu VPS):**

```bash
# 1. Create DigitalOcean Droplet (Ubuntu 22.04)
# 2. SSH to server
ssh root@YOUR_IP

# 3. Run quick setup
apt update && apt upgrade -y
apt install python3-pip python3-venv nginx git -y
adduser streamlit
su - streamlit
git clone YOUR_REPO_URL
cd leave_breakdown_app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 4. Test
streamlit run app.py

# 5. Set up service (see Step 7 above)

# Done! Your app is live at http://YOUR_IP
```

**Total time:** 30-45 minutes

---

## Benefits of Self-Hosting

✅ **Full Control** - You own the server  
✅ **Data Persistence** - Files never disappear  
✅ **No Sleep** - Always available 24/7  
✅ **Customization** - Full access to configure  
✅ **Scalability** - Upgrade resources anytime  
✅ **Privacy** - Data stays on your server  
✅ **Cost-effective** - $6/month vs $20+ for managed  

---

## Next Steps

1. **Choose hosting option:** VPS, on-premises, or Docker
2. **Follow the guide** for your chosen option
3. **Test thoroughly** before going live
4. **Set up backups** (critical!)
5. **Configure domain** (optional)
6. **Train your team** on new URL

---

## Need Help?

**Included in your package:**
- This complete guide
- All app files ready to deploy
- Backup scripts
- Service configuration files

**External resources:**
- DigitalOcean tutorials: https://www.digitalocean.com/community
- Ubuntu Server guide: https://ubuntu.com/server/docs
- Nginx documentation: https://nginx.org/en/docs/

---

**You now have everything you need to host the app on your own server!** 🚀

Choose your hosting option and let me know if you need help with any step!
