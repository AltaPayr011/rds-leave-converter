# 🖥️ Server Management Quick Reference

## Quick Commands for Managing Your Self-Hosted App

---

## Service Management (Ubuntu)

### Check App Status
```bash
sudo systemctl status streamlit
```

### Start App
```bash
sudo systemctl start streamlit
```

### Stop App
```bash
sudo systemctl stop streamlit
```

### Restart App
```bash
sudo systemctl restart streamlit
```

### Enable Auto-Start on Boot
```bash
sudo systemctl enable streamlit
```

### Disable Auto-Start
```bash
sudo systemctl disable streamlit
```

---

## Viewing Logs

### View Last 100 Lines
```bash
sudo journalctl -u streamlit -n 100
```

### Follow Logs in Real-Time
```bash
sudo journalctl -u streamlit -f
```

### View Logs from Today
```bash
sudo journalctl -u streamlit --since today
```

### View Error Logs Only
```bash
sudo journalctl -u streamlit -p err
```

### Save Logs to File
```bash
sudo journalctl -u streamlit > ~/streamlit_logs.txt
```

---

## System Monitoring

### Check Disk Space
```bash
df -h
```

### Check Memory Usage
```bash
free -h
```

### Check CPU Usage
```bash
top
# Or for better view:
htop  # Install with: sudo apt install htop
```

### Check Network Connections
```bash
sudo netstat -tulpn | grep 8501
```

### Check Running Processes
```bash
ps aux | grep streamlit
```

---

## Nginx Management

### Check Nginx Status
```bash
sudo systemctl status nginx
```

### Test Nginx Configuration
```bash
sudo nginx -t
```

### Reload Nginx (after config changes)
```bash
sudo systemctl reload nginx
```

### Restart Nginx
```bash
sudo systemctl restart nginx
```

### View Nginx Access Logs
```bash
sudo tail -f /var/log/nginx/access.log
```

### View Nginx Error Logs
```bash
sudo tail -f /var/log/nginx/error.log
```

---

## Firewall Management

### Check Firewall Status
```bash
sudo ufw status
```

### Allow New Port
```bash
sudo ufw allow PORT_NUMBER/tcp
```

### Remove Port Rule
```bash
sudo ufw delete allow PORT_NUMBER/tcp
```

### List All Rules
```bash
sudo ufw status numbered
```

---

## Backup Management

### Run Manual Backup
```bash
/home/streamlit/backup.sh
```

### List Backups
```bash
ls -lh /home/streamlit/backups
```

### Restore from Backup
```bash
# Replace YYYYMMDD_HHMMSS with actual backup date
sudo cp /home/streamlit/backups/employee_data_YYYYMMDD_HHMMSS.csv /home/streamlit/leave_breakdown_app/employee_data.csv
sudo cp /home/streamlit/backups/users_YYYYMMDD_HHMMSS.csv /home/streamlit/leave_breakdown_app/users.csv
sudo systemlit restart streamlit
```

### Check Backup Schedule
```bash
sudo crontab -u streamlit -l
```

---

## App Updates

### Update App from Git
```bash
cd /home/streamlit/leave_breakdown_app
sudo -u streamlit git pull
sudo systemctl restart streamlit
```

### Update Python Packages
```bash
cd /home/streamlit/leave_breakdown_app
sudo -u streamlit venv/bin/pip install -r requirements.txt --upgrade
sudo systemctl restart streamlit
```

---

## System Updates

### Update All Packages (Ubuntu)
```bash
sudo apt update
sudo apt upgrade -y
```

### Update Security Patches Only
```bash
sudo apt update
sudo apt upgrade -y --security
```

### Clean Up Old Packages
```bash
sudo apt autoremove -y
sudo apt autoclean
```

---

## SSL Certificate (Let's Encrypt)

### Install SSL Certificate
```bash
sudo certbot --nginx -d your-domain.com
```

### Renew Certificate (manual)
```bash
sudo certbot renew
```

### Test Auto-Renewal
```bash
sudo certbot renew --dry-run
```

### Check Certificate Expiry
```bash
sudo certbot certificates
```

---

## User Management

### Change Password for User
```bash
sudo passwd USERNAME
```

### Add New System User
```bash
sudo adduser USERNAME
```

### Grant Sudo Access
```bash
sudo usermod -aG sudo USERNAME
```

---

## File Permissions

### Fix App File Permissions
```bash
sudo chown -R streamlit:streamlit /home/streamlit/leave_breakdown_app
sudo chmod -R 755 /home/streamlit/leave_breakdown_app
```

### Make Script Executable
```bash
chmod +x /path/to/script.sh
```

---

## Troubleshooting Commands

### Check if App is Listening on Port
```bash
sudo lsof -i :8501
```

### Kill Process on Port (if stuck)
```bash
sudo kill -9 $(sudo lsof -t -i:8501)
```

### Check App Directory Size
```bash
du -sh /home/streamlit/leave_breakdown_app
```

### Find Large Files
```bash
sudo find / -type f -size +100M -exec ls -lh {} \;
```

### Check System Uptime
```bash
uptime
```

---

## Docker Commands (if using Docker)

### Start Containers
```bash
docker-compose up -d
```

### Stop Containers
```bash
docker-compose down
```

### View Logs
```bash
docker-compose logs -f
```

### Restart Containers
```bash
docker-compose restart
```

### Check Container Status
```bash
docker-compose ps
```

### Rebuild and Restart
```bash
docker-compose up -d --build
```

### Remove All Containers
```bash
docker-compose down -v
```

---

## Useful One-Liners

### Quick Health Check
```bash
curl http://localhost:8501/_stcore/health && echo "✅ App is healthy" || echo "❌ App is down"
```

### Check App Response Time
```bash
time curl -I http://localhost:8501
```

### Count Access Today
```bash
sudo grep $(date +%d/%b/%Y) /var/log/nginx/access.log | wc -l
```

### Find Out Who's Logged In
```bash
who
```

### Reboot Server
```bash
sudo reboot
```

### Shutdown Server
```bash
sudo shutdown -h now
```

---

## Emergency Procedures

### If App Won't Start:
```bash
# 1. Check logs
sudo journalctl -u streamlit -n 200

# 2. Try manual start
cd /home/streamlit/leave_breakdown_app
source venv/bin/activate
streamlit run app.py

# 3. Check for errors
# 4. Fix issue
# 5. Restart service
sudo systemctl restart streamlit
```

### If Server is Slow:
```bash
# 1. Check resources
htop

# 2. Restart app
sudo systemctl restart streamlit

# 3. Restart nginx
sudo systemctl restart nginx

# 4. If needed, reboot
sudo reboot
```

### If Disk is Full:
```bash
# 1. Check what's using space
du -sh /* | sort -hr | head -10

# 2. Clear old backups
find /home/streamlit/backups -mtime +7 -delete

# 3. Clear apt cache
sudo apt clean

# 4. Clear logs
sudo journalctl --vacuum-time=7d
```

---

## Daily Checklist

- [ ] Check app is accessible
- [ ] Verify backups completed
- [ ] Check disk space: `df -h`
- [ ] Check for errors: `sudo journalctl -u streamlit -p err --since today`

## Weekly Checklist

- [ ] Review access logs
- [ ] Check for system updates
- [ ] Verify SSL certificate validity
- [ ] Test backup restoration

## Monthly Checklist

- [ ] Update system packages
- [ ] Review user accounts
- [ ] Check resource usage trends
- [ ] Review and clean old logs

---

## Important File Locations

| File/Directory | Location | Purpose |
|----------------|----------|---------|
| App files | `/home/streamlit/leave_breakdown_app` | Main application |
| Service config | `/etc/systemd/system/streamlit.service` | Systemd service |
| Nginx config | `/etc/nginx/sites-available/streamlit` | Web server config |
| Backups | `/home/streamlit/backups` | Data backups |
| Logs | `journalctl -u streamlit` | App logs |
| Nginx logs | `/var/log/nginx/` | Web server logs |

---

## Support Contacts

**For Server Issues:**
- DigitalOcean Support: https://cloud.digitalocean.com/support
- Ubuntu Forums: https://ubuntuforums.org

**For App Issues:**
- Check logs: `sudo journalctl -u streamlit -n 100`
- Review documentation in app package

---

**Keep this reference handy for quick server management!** 🖥️
