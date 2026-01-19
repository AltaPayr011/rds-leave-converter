# 🔐 Authentication System - Quick Reference

## Default Admin Credentials

**First-time login:**
- Username: `admin`
- Password: `admin123`

⚠️ **CRITICAL**: 
- Change this password immediately after first login!
- These credentials are NOT displayed on the login screen for security
- Document these credentials securely for your team's initial setup
- After changing the password, ensure at least one person always has admin access

## User Roles

### Regular Users
- Can access all employee management features
- Can process leave transactions
- Can view and download reports
- **Cannot** access the Admin Panel

### Admin Users
- All regular user permissions, plus:
- Access to the Admin Panel
- Can add new users
- Can reset passwords for any user
- Can activate/deactivate user accounts
- Can delete users (except themselves and the last admin)

## Admin Panel Features

### Adding a New User
1. Login as admin
2. Go to **Admin Panel** tab
3. Click **"Add New User"**
4. Fill in:
   - Username (unique, will be used for login)
   - Password (minimum 6 characters)
   - Confirm Password
   - Full Name (display name)
   - Admin Access checkbox (optional)
5. Click **"Add User"**

### Resetting a User Password
1. Go to **Admin Panel** tab
2. Find the user in the list
3. Expand their section
4. In the "Reset Password" form:
   - Enter new password (minimum 6 characters)
   - Confirm the password
5. Click **"Reset Password"**

### Deactivating a User
1. Go to **Admin Panel** tab
2. Find the user in the list
3. Expand their section
4. Click **"Deactivate User"**
5. The user can no longer login (but data is preserved)

### Reactivating a User
1. Go to **Admin Panel** tab
2. Find the deactivated user (status shows "Inactive")
3. Expand their section
4. Click **"Activate User"**

### Deleting a User
1. Go to **Admin Panel** tab
2. Find the user in the list
3. Expand their section
4. Click **"Delete User"**
5. **Warning**: This permanently removes the user

## My Profile - Self-Service Password Change

**All users** (including admins) can manage their own passwords without admin intervention.

### Accessing My Profile

1. Login to the app
2. Click on the **"My Profile"** tab
3. View your account information
4. Use the "Change Password" section

### Changing Your Password

1. Go to **My Profile** tab
2. In the "Change Password" section:
   - Enter your **current password**
   - Enter your **new password** (minimum 6 characters)
   - **Confirm** your new password
3. Click "Change Password"

**Security Notes:**
- You must know your current password to change it
- New password must be different from current password
- Password change takes effect immediately
- You'll need the new password for your next login

**Password Requirements:**
- Minimum 6 characters
- Should be different from your current password
- Recommended: Use a mix of letters, numbers, and special characters

### Account Information Display

In My Profile, you can view:
- Your username
- Your full name
- Account type (Administrator or Regular User)
- Account status (Active/Inactive)
- Account creation date

**Note:** You cannot change your username or full name. Contact an administrator if these need to be updated.

## Security Features

✅ **Password Encryption**: All passwords are hashed using bcrypt (one-way encryption)
✅ **Session Management**: Authentication state persists during your session
✅ **Admin Protection**: Cannot delete or deactivate the last admin account
✅ **Self-Protection**: Users cannot modify their own admin status or delete themselves
✅ **Secure Storage**: User credentials stored in `users.csv` (excluded from Git)

## Best Practices

### For Admins:
1. **Change default password immediately**
2. Create individual accounts for each user (don't share login credentials)
3. Use strong passwords (8+ characters, mix of letters/numbers/symbols)
4. Regularly review active users
5. Deactivate accounts for users who no longer need access (instead of deleting)
6. Have at least 2 admin accounts (backup admin)

### For All Users:
1. Keep your password confidential
2. Use a unique password (don't reuse from other sites)
3. Logout when finished using the app
4. Report any suspicious activity to your admin

## Password Requirements

- **Minimum length**: 6 characters
- **Recommended**: 8+ characters with mix of:
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters

## Troubleshooting

### "Invalid username or password"
- Check username spelling (case-sensitive)
- Verify password (case-sensitive)
- Ensure account is active (ask admin)

### "Cannot deactivate the last admin"
- At least one active admin must exist
- Add another admin first, or restore a deactivated admin

### "Username already exists"
- Choose a different username
- Check if the user was previously deactivated (reactivate instead of creating new)

### Forgot Password
- Contact your system administrator
- Admin can reset your password through the Admin Panel

### Locked Out (Admin lost password)
- If you have database/file access:
  1. Delete `users.csv`
  2. Restart the app (creates new default admin)
- Otherwise, restore from backup

## Data Files

### users.csv
Contains encrypted user credentials:
- username
- password (bcrypt hash)
- full_name
- is_admin (True/False)
- active (True/False)
- created_date

**Important**: 
- Never edit this file manually
- Never commit to Git (it's in .gitignore)
- Backup regularly

## Security Notes

### What's Protected:
✅ Passwords are never stored in plain text
✅ All admin functions require admin authentication
✅ Sessions expire when you close the browser
✅ User credentials never appear in Git repository

### What's Not Protected:
⚠️ No rate limiting on login attempts (consider adding for production)
⚠️ No password reset via email (manual reset by admin only)
⚠️ No two-factor authentication (consider adding for production)
⚠️ Data files reset on Streamlit Cloud app restart

## For Production Deployment

Consider adding:
1. **Environment variables** for initial admin password
2. **Database storage** instead of CSV files
3. **Email verification** for new accounts
4. **Password reset functionality** via email
5. **Two-factor authentication (2FA)**
6. **Login attempt rate limiting**
7. **Session timeout** after inactivity
8. **Audit logging** for user actions

---

**Need Help?** Contact your system administrator or refer to the main README.md file.
