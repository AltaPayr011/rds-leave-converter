# 📋 Streamlit Deployment Checklist

## Print This Page and Check Off Each Step!

---

## PHASE 1: PREPARATION ⏱️ 5 minutes

- [ ] **1.1** App ZIP file downloaded and extracted to a folder
- [ ] **1.2** Know where the `leave_breakdown_app` folder is located
- [ ] **1.3** Have about 15-20 minutes available
- [ ] **1.4** Internet connection is working

---

## PHASE 2: GITHUB ACCOUNT ⏱️ 5 minutes

### If You Already Have GitHub:
- [ ] **2.1** Can login to https://github.com
- [ ] **SKIP to Phase 3**

### If You Need to Create GitHub Account:
- [ ] **2.2** Went to https://github.com
- [ ] **2.3** Clicked "Sign up"
- [ ] **2.4** Entered email address
- [ ] **2.5** Created password (8+ characters)
- [ ] **2.6** Chose username: ________________
- [ ] **2.7** Completed verification puzzle
- [ ] **2.8** Verified email (checked inbox, clicked link)
- [ ] **2.9** Selected "Free" plan
- [ ] **2.10** Successfully logged into GitHub

---

## PHASE 3: CREATE REPOSITORY ⏱️ 3 minutes

- [ ] **3.1** Logged into GitHub (https://github.com)
- [ ] **3.2** Clicked "+" icon → "New repository"
- [ ] **3.3** Repository name entered: `rds-leave-converter`
- [ ] **3.4** Description added (optional)
- [ ] **3.5** Selected "Private" visibility (RECOMMENDED)
- [ ] **3.6** Left all checkboxes UNCHECKED (README, .gitignore, license)
- [ ] **3.7** Clicked "Create repository"
- [ ] **3.8** Repository created successfully

**Write your repository URL here:**
```
https://github.com/____________/rds-leave-converter
```

---

## PHASE 4: UPLOAD FILES ⏱️ 5 minutes

### Core Files (Required):
- [ ] **4.1** Clicked "uploading an existing file" link
- [ ] **4.2** Uploaded: `app.py` ✅
- [ ] **4.3** Uploaded: `requirements.txt` ✅
- [ ] **4.4** Uploaded: `RDS_Logo.jpg` ✅
- [ ] **4.5** Uploaded: `.gitignore` ✅
- [ ] **4.6** Commit message: "Initial upload - Core app files"
- [ ] **4.7** Clicked "Commit changes"

### Data Files (Required):
- [ ] **4.8** Clicked "Add file" → "Upload files"
- [ ] **4.9** Uploaded: `employee_data_seed.csv` ✅
- [ ] **4.10** Uploaded: `employee_data_template.csv` ✅
- [ ] **4.11** Commit message: "Add employee data files"
- [ ] **4.12** Clicked "Commit changes"

### Documentation Files (Recommended):
- [ ] **4.13** Clicked "Add file" → "Upload files"
- [ ] **4.14** Uploaded all `.md` files (README, AUTHENTICATION, etc.)
- [ ] **4.15** Commit message: "Add documentation"
- [ ] **4.16** Clicked "Commit changes"

### Verification:
- [ ] **4.17** Went to repository main page
- [ ] **4.18** Can see `app.py` in file list ✅
- [ ] **4.19** Can see `requirements.txt` in file list ✅
- [ ] **4.20** Can see `RDS_Logo.jpg` in file list ✅

---

## PHASE 5: STREAMLIT CLOUD SETUP ⏱️ 2 minutes

- [ ] **5.1** Opened new tab: https://share.streamlit.io
- [ ] **5.2** Clicked "Continue with GitHub"
- [ ] **5.3** Logged into GitHub (if prompted)
- [ ] **5.4** Clicked "Authorize streamlit"
- [ ] **5.5** Reached Streamlit Cloud dashboard

---

## PHASE 6: DEPLOY APP ⏱️ 5-10 minutes

- [ ] **6.1** Clicked "New app" button
- [ ] **6.2** Selected repository: `rds-leave-converter`
- [ ] **6.3** Selected branch: `main` (or `master`)
- [ ] **6.4** Entered main file path: `app.py`
- [ ] **6.5** Customized app URL (optional): ________________
- [ ] **6.6** Clicked "Deploy!" button
- [ ] **6.7** Waiting for deployment (2-5 minutes)...
- [ ] **6.8** Saw "Your app is live!" message
- [ ] **6.9** App opened automatically

**Write your app URL here:**
```
https://________________________________.streamlit.app
```

---

## PHASE 7: FIRST LOGIN & SETUP ⏱️ 5 minutes

### Verify App Loaded:
- [ ] **7.1** RDS logo displays at top (centered)
- [ ] **7.2** "RDS PaySpace Leave Converter" heading visible
- [ ] **7.3** "for OpenTime" subheading visible
- [ ] **7.4** Login form shows (username + password fields)

### First Login:
- [ ] **7.5** Username: `admin`
- [ ] **7.6** Password: `admin123`
- [ ] **7.7** Clicked "Login"
- [ ] **7.8** Successfully logged in

### Critical Security Step:
- [ ] **7.9** Went to "Admin Panel" tab
- [ ] **7.10** Found "admin" user in list
- [ ] **7.11** Clicked to expand admin section
- [ ] **7.12** Reset Password form visible
- [ ] **7.13** Entered NEW strong password
- [ ] **7.14** Confirmed NEW password
- [ ] **7.15** Clicked "Reset Password"
- [ ] **7.16** Got success message

**Write your NEW admin password here (keep secure!):**
```
New Admin Password: ________________________________
```

### Load Employee Data:
- [ ] **7.17** Went to "Manage Employees" tab
- [ ] **7.18** Checked if 34 employees loaded automatically
  - [ ] YES - employees are there (SKIP to 7.21)
  - [ ] NO - need to add manually (continue to 7.19)
- [ ] **7.19** If no employees: Add them manually OR
- [ ] **7.20** Upload `employee_data.csv` to GitHub
- [ ] **7.21** Employees visible in list

---

## PHASE 8: ADD TEAM MEMBERS ⏱️ 2 minutes per user

### For Each Team Member:
- [ ] **8.1** Went to "Admin Panel" tab
- [ ] **8.2** Clicked "Add New User"
- [ ] **8.3** Entered username: ________________
- [ ] **8.4** Entered password: ________________
- [ ] **8.5** Confirmed password
- [ ] **8.6** Entered full name: ________________
- [ ] **8.7** Admin access? YES ☐  NO ☐
- [ ] **8.8** Clicked "Add User"
- [ ] **8.9** Got success message
- [ ] **8.10** User appears in list

Repeat for each team member!

---

## PHASE 9: TEST THE APP ⏱️ 5 minutes

- [ ] **9.1** Logged out
- [ ] **9.2** Logged back in with NEW admin password
- [ ] **9.3** Can access all tabs
- [ ] **9.4** Added a test employee successfully
- [ ] **9.5** Went to "Process Leave" tab
- [ ] **9.6** Uploaded a test leave file
- [ ] **9.7** Checked the confirmation box
- [ ] **9.8** Clicked "Process Leave Breakdown"
- [ ] **9.9** Processing completed
- [ ] **9.10** Downloaded Excel file
- [ ] **9.11** Opened Excel file - looks correct

---

## PHASE 10: SHARE WITH TEAM ⏱️ 2 minutes

- [ ] **10.1** Bookmarked app URL in browser
- [ ] **10.2** Shared URL with team (email, chat, etc.)
- [ ] **10.3** Shared login credentials securely (NOT via email!)
- [ ] **10.4** Told team to bookmark the URL
- [ ] **10.5** Sent instructions: "Login credentials in separate secure message"

---

## FINAL VERIFICATION ✅

Check ALL of these:

- [ ] ✅ App is accessible at URL
- [ ] ✅ Can login with new admin password
- [ ] ✅ Old admin password (admin123) no longer works
- [ ] ✅ Employees are loaded (34 or manually added)
- [ ] ✅ At least one additional user account created
- [ ] ✅ Can process leave transactions successfully
- [ ] ✅ Downloaded results are correct
- [ ] ✅ Team members know the URL
- [ ] ✅ Team members have credentials
- [ ] ✅ App URL is bookmarked

---

## TROUBLESHOOTING NOTES

If something didn't work, write notes here:

```
Issue: ___________________________________________________

What happened: ___________________________________________

___________________________________________________________

Solution tried: __________________________________________

___________________________________________________________

Result: ___________________________________________________
```

---

## IMPORTANT INFORMATION TO KEEP

**Write these down and keep secure:**

```
REPOSITORY URL:
https://github.com/_________________/rds-leave-converter

APP URL:
https://__________________________________.streamlit.app

ADMIN USERNAME: admin

NEW ADMIN PASSWORD: _____________________________________

GITHUB USERNAME: ________________________________________

GITHUB PASSWORD: ________________________________________

STREAMLIT CLOUD LOGIN: Same as GitHub (authorized)

DEPLOYMENT DATE: _____/_____/2026

WHO HAS ACCESS:
1. _____________________________ (Username: ____________)
2. _____________________________ (Username: ____________)
3. _____________________________ (Username: ____________)
4. _____________________________ (Username: ____________)
5. _____________________________ (Username: ____________)
```

---

## SUCCESS! 🎉

If all items are checked off:

✅ Your app is LIVE on the internet!
✅ Team members can access it!
✅ You're ready to start processing leave!

---

## NEXT STEPS

After successful deployment:

1. **Daily Use:**
   - Users go to app URL
   - Login with their credentials
   - Process leave transactions as needed

2. **Maintenance:**
   - Change passwords periodically
   - Add/remove users as team changes
   - Update employee data when needed

3. **Updates:**
   - Edit files on GitHub to make changes
   - Changes deploy automatically in 2 minutes

4. **Support:**
   - Check documentation in repository
   - Visit: https://docs.streamlit.io
   - See TROUBLESHOOTING section in STREAMLIT_DEPLOYMENT.md

---

**COMPLETED BY:** ___________________________

**DATE:** ______ / ______ / 2026

**TIME TAKEN:** __________ minutes

**NOTES:**
```
___________________________________________________________

___________________________________________________________

___________________________________________________________
```

---

**Keep this checklist for reference!**
Print a new copy when onboarding new team members.
