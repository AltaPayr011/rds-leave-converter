#!/bin/bash
# Backup script for RDS Leave Converter
# Run this manually or via cron

# Configuration
BACKUP_DIR="/home/streamlit/backups"
APP_DIR="/home/streamlit/leave_breakdown_app"
DATE=$(date +%Y%m%d_%H%M%S)
KEEP_DAYS=30

echo "=================================================="
echo "RDS Leave Converter - Backup Script"
echo "=================================================="
echo "Date: $(date)"
echo ""

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Backup employee data
if [ -f "$APP_DIR/employee_data.csv" ]; then
    cp "$APP_DIR/employee_data.csv" "$BACKUP_DIR/employee_data_$DATE.csv"
    echo "✅ Backed up employee_data.csv"
else
    echo "⚠️  employee_data.csv not found (may not exist yet)"
fi

# Backup user data
if [ -f "$APP_DIR/users.csv" ]; then
    cp "$APP_DIR/users.csv" "$BACKUP_DIR/users_$DATE.csv"
    echo "✅ Backed up users.csv"
else
    echo "⚠️  users.csv not found (may not exist yet)"
fi

# Clean up old backups (keep last 30 days)
DELETED=$(find "$BACKUP_DIR" -name "*.csv" -mtime +$KEEP_DAYS -delete -print | wc -l)
if [ $DELETED -gt 0 ]; then
    echo "🗑️  Deleted $DELETED old backup(s) (older than $KEEP_DAYS days)"
fi

# Show backup info
BACKUP_COUNT=$(ls -1 "$BACKUP_DIR"/*.csv 2>/dev/null | wc -l)
BACKUP_SIZE=$(du -sh "$BACKUP_DIR" 2>/dev/null | cut -f1)

echo ""
echo "📊 Backup Summary:"
echo "   Location: $BACKUP_DIR"
echo "   Files: $BACKUP_COUNT"
echo "   Size: $BACKUP_SIZE"
echo ""
echo "✅ Backup completed successfully!"
echo "=================================================="

# List recent backups
echo ""
echo "📁 Recent backups:"
ls -lth "$BACKUP_DIR" | head -n 6
