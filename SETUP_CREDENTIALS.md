# 🔐 Initial Setup - Default Admin Credentials

## IMPORTANT: READ THIS FIRST

This file contains the **default administrator credentials** for the RDS PaySpace Leave Converter application. These credentials are required for first-time setup.

---

## Default Admin Login

**Username:** `admin`  
**Password:** `admin123`

---

## ⚠️ SECURITY NOTICE

1. **These credentials are NOT displayed on the login screen** for security reasons
2. **You MUST change this password immediately** after first login
3. **Delete this file** after noting the credentials securely
4. **Store the new password** in your organization's password manager

---

## First-Time Setup Steps

### 1. Run the Application
```bash
# Mac/Linux
./start.sh

# Windows
start.bat

# Or manually
streamlit run app.py
```

### 2. Access the Login Screen
- Open your browser to: http://localhost:8501
- You will see the RDS logo and login form
- **No default credentials will be shown** (this is intentional)

### 3. Login as Admin
- Username: `admin`
- Password: `admin123`
- Click "Login"

### 4. Change Admin Password (IMMEDIATELY!)
1. Click on the **Admin Panel** tab
2. Find the "admin" user in the list
3. Expand their section
4. In the "Reset Password" form:
   - Enter a strong new password (8+ characters)
   - Confirm the password
5. Click "Reset Password"
6. **Document the new password securely**

### 5. Add Your Team Members
1. Still in the Admin Panel
2. Click "Add New User"
3. Create accounts for your team:
   - Enter their details
   - Set initial passwords
   - Choose if they need admin access
4. Share their credentials securely

### 6. Load Employee Data
1. Go to **Manage Employees** tab
2. Either:
   - Copy `employee_data_seed.csv` to `employee_data.csv` (34 employees)
   - Or add employees manually through the interface

### 7. Test the System
1. Go to **Process Leave** tab
2. Upload a test leave transactions file
3. Process and download the results
4. Verify calculations are correct

---

## Production Deployment

### Before Deploying to Streamlit Cloud:

1. ✅ Change the default admin password
2. ✅ Create individual user accounts for your team
3. ✅ Test all functionality locally
4. ✅ Delete or secure this SETUP_CREDENTIALS.md file
5. ✅ Ensure `.gitignore` excludes `users.csv`
6. ✅ Document the new admin password in your password manager

### Deployment Checklist:

- [ ] Admin password changed from default
- [ ] At least 2 admin accounts created (backup)
- [ ] All team members have accounts
- [ ] Employee data loaded and verified
- [ ] Test leave file processed successfully
- [ ] This credentials file deleted or secured
- [ ] Password documentation updated

---

## Security Best Practices

### Strong Password Requirements:
- **Minimum 8 characters**
- Mix of uppercase and lowercase letters
- Include numbers
- Include special characters (!@#$%^&*)
- Don't reuse passwords from other sites

### Examples of Strong Passwords:
- `RDS@2024!Secure`
- `Leave$Converter#2024`
- `PaySpace!Admin99`

### Password Management:
- Use a password manager (LastPass, 1Password, Bitwarden)
- Never share passwords via email or unencrypted chat
- Change passwords if you suspect compromise
- Have at least 2 people with admin access (backup)

---

## Forgot Admin Password?

If you lose the admin password and get locked out:

### Option 1: Reset via File System
1. Stop the application
2. Delete the `users.csv` file
3. Restart the application
4. It will recreate the default admin account
5. Login with `admin` / `admin123`
6. Set a new password immediately

### Option 2: Restore from Backup
1. If you have a backup of `users.csv`, restore it
2. Try any documented admin credentials

---

## Support Contact

For assistance with initial setup or password issues:
- Contact your IT administrator
- Refer to AUTHENTICATION.md for detailed security documentation
- See README.md for general usage information

---

## ⚠️ DELETE THIS FILE AFTER SETUP

Once you have:
1. Changed the admin password
2. Created user accounts
3. Documented passwords securely

**Delete this file** to prevent unauthorized access to the default credentials.

---

**Document Version:** 1.0  
**Last Updated:** January 2026  
**Application:** RDS PaySpace Leave Converter for OpenTime
