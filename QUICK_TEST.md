# 🚀 QUICK START - Test in 5 Minutes

## Prerequisites
- Python 3.8 or higher installed
- Terminal/Command Prompt access

## Step-by-Step Testing

### 1️⃣ Extract the Files
```bash
# Extract leave_breakdown_app.zip
# Navigate to the folder
cd leave_breakdown_app
```

### 2️⃣ Run Validation (Optional but Recommended)
```bash
python3 validate.py
# or
python validate.py
```
This checks that all files are present and validates the data structure.

### 3️⃣ Quick Start
**Mac/Linux:**
```bash
chmod +x start.sh
./start.sh
```

**Windows:**
```
start.bat
```

**What happens automatically:**
- Checks Python is installed
- Installs dependencies (if needed)
- Loads employee seed data (34 employees) - if not already present
- Starts the app
- Opens browser to http://localhost:8501

### 4️⃣ Open Your Browser
The app will automatically open at:
```
http://localhost:8501
```

### 5️⃣ Login
```
Username: admin
Password: admin123
```

**Note**: These default credentials are not shown on the login screen for security. Make sure to change the password after first login!

## What You'll See

### Login Screen
✅ RDS Logo at the top
✅ "RDS PaySpace Leave Converter for OpenTime" title
✅ Username and password fields

### After Login
✅ RDS Logo in header
✅ Your name shown (System Administrator)
✅ 4 tabs: Manage Employees, Process Leave, Admin Panel, Help
✅ Logout button

## Quick Test Scenarios

### Test 1: View Seed Data (1 minute)
1. Login
2. Click **Manage Employees** tab
3. You should see 34 employees listed
4. Try searching for "RDS00005"

### Test 2: Add a User (2 minutes)
1. Go to **Admin Panel** tab
2. Click "Add New User"
3. Enter:
   - Username: `testuser`
   - Password: `test123`
   - Confirm: `test123`
   - Full Name: `Test Person`
4. Click "Add User"
5. Logout and login as `testuser` / `test123`

### Test 3: Process Leave (2 minutes)
1. Login (any user)
2. Go to **Process Leave** tab
3. Upload `Leave_Transactions_648648.xlsx`
4. Read the warning about declined/cancelled leave
5. Check the confirmation box
6. Click "Process Leave Breakdown"
7. Click "Download Leave Breakdown"
8. Open the Excel file

## Stopping the App
Press `Ctrl + C` in the terminal where the app is running

## Common Issues

**Port already in use?**
```bash
streamlit run app.py --server.port 8502
```
Then open: http://localhost:8502

**Dependencies not installed?**
```bash
pip install -r requirements.txt
```

**Can't see logo?**
Make sure `RDS_Logo.jpg` is in the same folder as `app.py`

## Full Testing
For comprehensive testing, see **TESTING_GUIDE.md**

## Ready to Deploy?
See **DEPLOYMENT.md** for Streamlit Cloud deployment

---

**That's it!** If you can complete the 3 quick tests above, your app is working perfectly! 🎉
