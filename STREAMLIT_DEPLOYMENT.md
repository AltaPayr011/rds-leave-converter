# 🚀 Complete Streamlit Cloud Deployment Guide

## Step-by-Step Instructions for RDS PaySpace Leave Converter

---

## 📋 Prerequisites Checklist

Before you start, make sure you have:

- [ ] GitHub account (we'll create one if you don't)
- [ ] The app ZIP file extracted on your computer
- [ ] About 15-20 minutes of time
- [ ] Internet connection

---

## Part 1: Setting Up GitHub (If You Don't Have an Account)

### Step 1.1: Create GitHub Account

1. **Go to GitHub:**
   - Open your web browser
   - Navigate to: https://github.com

2. **Sign Up:**
   - Click the **"Sign up"** button (top right)
   - Enter your email address
   - Click **"Continue"**

3. **Create Password:**
   - Enter a strong password (at least 15 characters or 8+ with a number and lowercase letter)
   - Click **"Continue"**

4. **Choose Username:**
   - Enter a username (e.g., "rds-surgical" or "your-company-name")
   - This will be part of your app URL
   - Click **"Continue"**

5. **Verify Account:**
   - Complete the verification puzzle
   - Click **"Create account"**

6. **Verify Email:**
   - Check your email inbox
   - Find the email from GitHub
   - Click the verification link
   - Enter the code shown in the email

7. **Choose Plan:**
   - Select **"Free"** (perfect for this app)
   - Click **"Continue for free"**

✅ **You now have a GitHub account!**

---

## Part 2: Creating Your Repository

### Step 2.1: Create New Repository

1. **Go to GitHub Homepage:**
   - Make sure you're logged in
   - You should see your dashboard

2. **Create New Repository:**
   - Click the **"+"** icon (top right corner)
   - Select **"New repository"**

   OR
   
   - Click the green **"New"** button (left side)

3. **Repository Settings:**

   **Owner:** (Your username - already selected)
   
   **Repository name:** 
   ```
   rds-leave-converter
   ```
   (Must be lowercase, no spaces - use hyphens)

   **Description:** (Optional but recommended)
   ```
   RDS PaySpace Leave Converter for OpenTime - Converts leave transactions to daily breakdowns
   ```

   **Visibility:**
   - ⚪ Public (Anyone can see, but only you can edit)
   - 🔘 **Private** ← **RECOMMENDED for company data**
   
   **Initialize repository:**
   - ⬜ Add a README file (Leave UNCHECKED - we have our own)
   - ⬜ Add .gitignore (Leave UNCHECKED - we have our own)
   - ⬜ Choose a license (Leave UNCHECKED)

4. **Create Repository:**
   - Click the green **"Create repository"** button

✅ **Your repository is created!**

You should see a page with instructions for uploading code.

---

## Part 3: Uploading Your App Files

### Step 3.1: Upload Files via Web Interface (Easiest Method)

1. **You should see a page that says "Quick setup"**
   
2. **Upload Files:**
   - Look for the text: "Get started by creating a new file or uploading an existing file"
   - Click **"uploading an existing file"** (it's a clickable link)

3. **Drag and Drop Files:**
   
   **IMPORTANT:** Upload these files in this order:
   
   **First, upload these core files:**
   - `app.py` ← REQUIRED
   - `requirements.txt` ← REQUIRED
   - `RDS_Logo.jpg` ← REQUIRED
   - `.gitignore` ← RECOMMENDED

   **How to upload:**
   - Open your `leave_breakdown_app` folder on your computer
   - Select the files listed above
   - Drag them into the upload area in your browser
   
   OR
   
   - Click "choose your files"
   - Navigate to your folder
   - Select the files
   - Click Open

4. **Commit First Upload:**
   - Scroll down to "Commit changes"
   - In the text box, type:
     ```
     Initial upload - Core app files
     ```
   - Click the green **"Commit changes"** button

5. **Upload Data Files:**
   - Click **"Add file"** → **"Upload files"**
   - Select and upload:
     - `employee_data_seed.csv`
     - `employee_data_template.csv`
   - Commit message: `Add employee data files`
   - Click **"Commit changes"**

6. **Upload Documentation (Optional but Recommended):**
   - Click **"Add file"** → **"Upload files"**
   - Select and upload all `.md` files:
     - `README.md`
     - `AUTHENTICATION.md`
     - `DEPLOYMENT.md`
     - `TESTING_GUIDE.md`
     - `QUICK_TEST.md`
     - `CHANGELOG.md`
     - `DATA_PREPARATION.md`
     - `SETUP_CREDENTIALS.md`
     - `SEED_DATA.md`
     - `PROJECT_OVERVIEW.md`
     - All other documentation files
   - Commit message: `Add documentation`
   - Click **"Commit changes"**

7. **Upload Start Scripts (Optional):**
   - Click **"Add file"** → **"Upload files"**
   - Upload:
     - `start.sh`
     - `start.bat`
     - `validate.py`
   - Commit message: `Add utility scripts`
   - Click **"Commit changes"**

✅ **All files uploaded!**

**CRITICAL FILES CHECK:**
Go to your repository main page and verify you see:
- ✅ `app.py`
- ✅ `requirements.txt`
- ✅ `RDS_Logo.jpg`
- ✅ `.gitignore`
- ✅ `employee_data_seed.csv`

If these 5 files are there, you're ready to deploy!

---

## Part 4: Deploying to Streamlit Cloud

### Step 4.1: Access Streamlit Cloud

1. **Go to Streamlit Cloud:**
   - Open a new tab
   - Navigate to: https://share.streamlit.io

2. **Sign Up with GitHub:**
   - Click **"Continue with GitHub"**
   - If not logged into GitHub, log in
   - Click **"Authorize streamlit"** (to allow Streamlit to access your repositories)

3. **Streamlit Cloud Dashboard:**
   - You'll see your dashboard (empty if first time)

### Step 4.2: Deploy Your App

1. **Create New App:**
   - Click the **"New app"** button (top right)
   - OR if this is your first app, click **"Deploy an app"**

2. **Configure Deployment:**

   **Repository:**
   - Dropdown shows your GitHub username
   - Select your repository: `rds-leave-converter` (or whatever you named it)

   **Branch:**
   - Select: `main` (or `master` if that's what GitHub created)

   **Main file path:**
   ```
   app.py
   ```
   (Type this exactly - it's the filename of your main application)

   **App URL:**
   - This will be auto-generated
   - Format: `https://[username]-rds-leave-converter.streamlit.app`
   - You can customize the subdomain if you want:
     - Example: `rds-payspace-leave` → `https://rds-payspace-leave.streamlit.app`

3. **Advanced Settings (Optional but Recommended):**

   Click **"Advanced settings"** at the bottom:

   **Python version:**
   - Select: `3.12` (or latest available)

   **Secrets:**
   - Leave empty for now (we'll add if needed)

4. **Deploy:**
   - Click the blue **"Deploy!"** button

### Step 4.3: Wait for Deployment

You'll see a deployment screen with logs:

```
Preparing system...
Cloning repository...
Installing dependencies...
Running app...
```

**This takes 2-5 minutes.** Be patient!

You'll see:
- ⏳ Yellow "Preparing..." message
- 📦 Installation progress
- ✅ Green "Your app is live!" when done

---

## Part 5: First Time Setup

### Step 5.1: Access Your Live App

1. **App is Live:**
   - Once deployment completes, your app opens automatically
   - Bookmark this URL: `https://[your-app-name].streamlit.app`

2. **You Should See:**
   - RDS Logo at the top (centered, ~250px)
   - "RDS PaySpace Leave Converter" heading
   - "for OpenTime" subheading
   - Username and Password fields
   - Login button
   - No default credentials shown (security feature)

3. **First Login:**
   - Username: `admin`
   - Password: `admin123`
   - Click "Login"

✅ **You're in!**

### Step 5.2: Critical First Steps

**IMMEDIATELY do these 3 things:**

1. **Change Admin Password:**
   - Go to **Admin Panel** tab
   - Find "admin" user
   - Expand the section
   - Enter a strong new password
   - Confirm the password
   - Click "Reset Password"
   - **WRITE DOWN THE NEW PASSWORD!**

2. **Load Employee Data:**
   - The app may not have `employee_data.csv` yet
   - Go to **Manage Employees** tab
   - If no employees show:
     - You'll need to add them manually
     - OR see "Troubleshooting" section below

3. **Add Your Team:**
   - Go to **Admin Panel** tab
   - Click "Add New User"
   - Create accounts for your team members
   - Share credentials securely (not via email!)

---

## Part 6: Sharing Your App

### Step 6.1: Share the URL

Your app URL is:
```
https://[your-app-name].streamlit.app
```

**Share this with your team!**

### Step 6.2: Important Notes for Users

Tell your team:

1. **Bookmark the URL** - They'll use it daily

2. **Login Credentials:**
   - They'll need the username and password you create for them
   - Each person should have their own account

3. **No Software Installation:**
   - Just open the URL in any browser
   - Works on desktop, tablet, or phone

4. **Internet Required:**
   - Must be online to use
   - Data is processed in real-time

---

## Part 7: Managing Your Deployed App

### Step 7.1: Streamlit Cloud Dashboard

Access your dashboard at: https://share.streamlit.io

You can:
- ✅ View app logs
- ✅ Restart the app
- ✅ Update settings
- ✅ Check usage analytics
- ✅ Manage multiple apps

### Step 7.2: Updating Your App

When you need to make changes:

1. **Edit Files on GitHub:**
   - Go to your repository
   - Click on the file you want to edit
   - Click the pencil icon (Edit)
   - Make your changes
   - Scroll down and commit changes

2. **Automatic Redeployment:**
   - Streamlit Cloud detects changes automatically
   - App rebuilds (takes 1-2 minutes)
   - Changes go live automatically

**Example: Updating logo:**
1. Go to your GitHub repository
2. Click on `RDS_Logo.jpg`
3. Click "Delete file"
4. Upload new logo file
5. Wait for automatic redeployment

### Step 7.3: Restarting the App

If the app seems stuck or has issues:

1. Go to https://share.streamlit.io
2. Find your app in the list
3. Click the **"⋮"** (three dots) menu
4. Click **"Reboot app"**
5. Wait 1-2 minutes

---

## Part 8: Important Considerations

### 8.1: Data Persistence

⚠️ **CRITICAL LIMITATION:**

On Streamlit Cloud's free tier:
- Employee data **will reset** when the app restarts
- User credentials **will reset** when the app restarts
- The app restarts when:
  - You push changes to GitHub
  - The app is inactive for a while
  - Streamlit performs maintenance

**Solutions:**

**Option 1: Re-add data after restarts** (Simple)
- Keep a list of employees in Excel/Google Sheets
- Add them back through the UI after restart
- Change admin password again after restart

**Option 2: Store seed data in GitHub** (Better)
- The `employee_data_seed.csv` will always be there
- Copy it manually to `employee_data.csv` when needed
- See "Advanced: Data Persistence" section

**Option 3: Upgrade to Streamlit Cloud Pro** (Best for production)
- $20/month per developer
- Persistent storage
- Better performance
- Custom domains
- Visit: https://streamlit.io/cloud

### 8.2: Security Considerations

For **PRIVATE** repositories:
- ✅ Your code is not public
- ✅ Only you can see the repository
- ✅ App is still publicly accessible at its URL

For **PUBLIC** repositories:
- ⚠️ Anyone can see your code
- ⚠️ Do NOT commit sensitive data
- ✅ App is publicly accessible at its URL

**Best Practices:**
1. Keep repository **PRIVATE** ✅
2. Share app URL only with authorized users
3. Create separate user accounts (don't share passwords)
4. Change default admin password immediately
5. Use strong passwords (8+ characters)

### 8.3: Free Tier Limits

Streamlit Cloud Free includes:
- ✅ 1 private app
- ✅ Unlimited public apps
- ✅ Community support
- ✅ Basic resources
- ⚠️ May sleep after inactivity
- ⚠️ No persistent storage

**If you need more:**
- Consider Streamlit Cloud Pro
- Or self-host on your own server

---

## Part 9: Troubleshooting

### Issue 1: "No employees found" after deployment

**Problem:** Employee data file not loading

**Solution A (Quick):**
1. Login as admin
2. Go to Manage Employees
3. Manually add employees through the UI

**Solution B (Automated):**
1. Create a file called `employee_data.csv` on your computer
2. Copy content from `employee_data_seed.csv`
3. Upload to GitHub repository
4. Wait for app to redeploy

### Issue 2: "App failed to load"

**Problem:** Error in code or missing files

**Solution:**
1. Go to https://share.streamlit.io
2. Click on your app
3. Click "App logs" (bottom)
4. Look for red error messages
5. Common issues:
   - Missing `requirements.txt` → Upload it to GitHub
   - Missing `app.py` → Upload it to GitHub
   - Missing `RDS_Logo.jpg` → Upload it to GitHub

### Issue 3: App is very slow

**Solutions:**
1. Check your internet connection
2. App may be "waking up" (first load after inactivity)
3. Wait 30 seconds and try again
4. If persistent, reboot app from Streamlit dashboard

### Issue 4: Lost admin password

**Solution:**
1. Go to your GitHub repository
2. Find and delete `users.csv` (if it exists)
3. App will recreate default admin (admin/admin123)
4. Login and set new password immediately

### Issue 5: Can't find my app URL

**Find it here:**
1. Go to https://share.streamlit.io
2. Your apps are listed
3. Click on your app name
4. URL is shown at the top
5. Format: `https://[username]-[repo-name].streamlit.app`

### Issue 6: Changes not appearing

**Solution:**
1. Make sure you committed changes on GitHub
2. Wait 2-3 minutes for redeployment
3. Hard refresh browser (Ctrl + Shift + R or Cmd + Shift + R)
4. Check app logs on Streamlit dashboard

---

## Part 10: Testing Your Deployed App

### Quick Test Checklist

After deployment, test these:

- [ ] Can access the app URL
- [ ] RDS logo displays correctly
- [ ] Can login with admin credentials
- [ ] Can change admin password
- [ ] Can add a test employee
- [ ] Can add a test user (in Admin Panel)
- [ ] Can upload a leave transactions file
- [ ] Can process leave breakdown
- [ ] Can download results
- [ ] Excel file opens correctly

**If all checkboxes are checked: ✅ Your app is working perfectly!**

---

## Part 11: Custom Domain (Optional Advanced)

If you want a custom domain like `leave.robdyersurgical.com`:

**Requirements:**
- Streamlit Cloud **Pro** or **Enterprise** plan
- Your own domain name
- DNS configuration access

**Steps:**
1. Upgrade to Pro plan
2. Go to app settings
3. Add custom domain
4. Update your domain's DNS records
5. Wait for SSL certificate

**Note:** This requires technical knowledge or IT support.

---

## Quick Reference Card

**Print and keep this handy:**

```
┌─────────────────────────────────────────────────────────┐
│           RDS LEAVE CONVERTER - QUICK REFERENCE         │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  APP URL:                                               │
│  https://[your-app-name].streamlit.app                 │
│                                                          │
│  GITHUB REPOSITORY:                                     │
│  https://github.com/[username]/rds-leave-converter     │
│                                                          │
│  STREAMLIT DASHBOARD:                                   │
│  https://share.streamlit.io                            │
│                                                          │
│  DEFAULT LOGIN (Change immediately!):                   │
│  Username: admin                                        │
│  Password: admin123                                     │
│                                                          │
│  TO UPDATE APP:                                         │
│  1. Edit files on GitHub                               │
│  2. Commit changes                                      │
│  3. Wait 2 minutes for auto-redeploy                   │
│                                                          │
│  TO RESTART APP:                                        │
│  1. Go to share.streamlit.io                           │
│  2. Find your app                                       │
│  3. Click ⋮ → Reboot app                               │
│                                                          │
│  SUPPORT:                                               │
│  - Check DEPLOYMENT.md in your repository              │
│  - Visit docs.streamlit.io                             │
│  - Community forum: discuss.streamlit.io               │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

---

## Congratulations! 🎉

Your RDS PaySpace Leave Converter is now live on the internet!

**What you've accomplished:**
✅ Created a GitHub repository  
✅ Uploaded your app code  
✅ Deployed to Streamlit Cloud  
✅ Made it accessible to your team  
✅ Secured with authentication  

**Next steps:**
1. Share the URL with your team
2. Create user accounts for everyone
3. Start processing leave transactions!

**Remember:**
- Change the default admin password
- Keep the app URL bookmarked
- Add employees through the UI or seed data
- Use strong passwords for all accounts

---

**Need help?** 
- Check the troubleshooting section above
- Visit: https://docs.streamlit.io
- Community: https://discuss.streamlit.io

**Questions about the app itself?**
- Check README.md in your repository
- Review AUTHENTICATION.md for security
- See TESTING_GUIDE.md for full features

---

**Deployment Date:** January 2026  
**App Version:** 2.3  
**Deployment Method:** Streamlit Cloud  
**Status:** 🟢 Production Ready
