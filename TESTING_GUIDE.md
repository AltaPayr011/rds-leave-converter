# 🧪 Local Testing Guide - RDS PaySpace Leave Converter

## Quick Start Testing

### Option 1: Automated Quick Start (Recommended)

**On Mac/Linux:**
```bash
cd leave_breakdown_app
chmod +x start.sh
./start.sh
```

**On Windows:**
```
cd leave_breakdown_app
start.bat
```

The script will:
1. Check if Python is installed
2. Install dependencies automatically
3. Ask if you want to load seed data (34 employees)
4. Start the app
5. Open your browser to http://localhost:8501

### Option 2: Manual Testing

```bash
# 1. Navigate to the app folder
cd leave_breakdown_app

# 2. Install dependencies
pip install -r requirements.txt

# 3. (Optional) Load seed employee data
cp employee_data_seed.csv employee_data.csv

# 4. Run the app
streamlit run app.py
```

## Testing Checklist

### ✅ Phase 1: Authentication Testing

#### Test 1: Default Admin Login
1. Open http://localhost:8501
2. You should see:
   - ✅ RDS Logo at the top (centered, ~250px width)
   - ✅ "RDS PaySpace Leave Converter" heading
   - ✅ "for OpenTime" subheading
   - ✅ Username and Password fields
   - ✅ Login button
   - ✅ NO default credentials displayed (security feature)
3. Login with:
   - Username: `admin`
   - Password: `admin123`
4. **Expected**: Successfully logs in to main app

**Note**: Default credentials are not shown on login screen for security. You must know them or have them documented.

#### Test 2: Failed Login
1. Try logging in with wrong credentials:
   - Username: `admin`
   - Password: `wrong`
2. **Expected**: Red error message "❌ Invalid username or password"

#### Test 3: Empty Fields
1. Click Login without entering anything
2. **Expected**: Error message about required fields

### ✅ Phase 2: User Interface Testing

#### Test 4: Main App Layout
After logging in successfully, verify:
- ✅ RDS Logo visible in top-left
- ✅ App title in center: "RDS PaySpace Leave Converter for OpenTime"
- ✅ "Logged in as: System Administrator" in top-right
- ✅ Logout button visible
- ✅ Four tabs visible (admin user):
  - 👥 Manage Employees
  - 📊 Process Leave
  - ⚙️ Admin Panel
  - ℹ️ Help

#### Test 5: Logout Functionality
1. Click the "🚪 Logout" button
2. **Expected**: Returns to login screen

### ✅ Phase 3: Admin Panel Testing

#### Test 6: Add New User
1. Login as admin
2. Go to **Admin Panel** tab
3. Click "➕ Add New User"
4. Fill in:
   - Username: `testuser`
   - Password: `test123`
   - Confirm Password: `test123`
   - Full Name: `Test User`
   - Leave "Admin Access" unchecked
5. Click "Add User"
6. **Expected**: 
   - Success message
   - User appears in the list below

#### Test 7: Password Reset
1. Find the user you just created
2. Expand their section
3. In the "Reset Password" form:
   - New Password: `newpass123`
   - Confirm Password: `newpass123`
4. Click "Reset Password"
5. **Expected**: Success message

#### Test 8: Test New User Login
1. Logout
2. Login with:
   - Username: `testuser`
   - Password: `newpass123`
3. **Expected**: 
   - Successfully logs in
   - Only sees 3 tabs (no Admin Panel)

#### Test 9: Deactivate User
1. Logout and login as `admin` / `admin123`
2. Go to Admin Panel
3. Find `testuser`
4. Click "🔒 Deactivate User"
5. **Expected**: 
   - Success message
   - Status changes to "Inactive"
6. Logout and try to login as `testuser`
7. **Expected**: Login fails

#### Test 10: Reactivate User
1. Login as admin
2. Go to Admin Panel
3. Find `testuser` (now Inactive)
4. Click "🔓 Activate User"
5. **Expected**: Status changes back to "Active"

### ✅ Phase 4: Employee Management Testing

#### Test 11: Add Employee
1. Go to **Manage Employees** tab
2. Click "➕ Add New Employee"
3. Fill in:
   - Employee Number: `TEST001`
   - First Name: `John`
   - Last Name: `Doe`
   - Leave all hours as default (8.5 and 6.0)
4. Click "Add Employee"
5. **Expected**: 
   - Success message
   - Employee appears in the list

#### Test 12: Load Seed Data (if not already loaded)
1. If you copied `employee_data_seed.csv` to `employee_data.csv`
2. Refresh the page or restart the app
3. **Expected**: 34 employees should be listed

#### Test 13: Search Employee
1. In the search box, type: `RDS00005`
2. **Expected**: Only employees matching that number appear

#### Test 14: Edit Employee
1. Find an employee (e.g., TEST001 or RDS00005)
2. Click to expand their section
3. Change Friday hours to: `5.0`
4. Click "💾 Save"
5. **Expected**: Success message

#### Test 15: Delete Employee
1. Find TEST001 employee
2. Click "🗑️ Delete"
3. **Expected**: 
   - Success message
   - Employee removed from list

### ✅ Phase 5: Leave Processing Testing

#### Test 16: Upload Leave File
1. Go to **Process Leave** tab
2. You should see employee count (e.g., "📊 34 employees loaded")
3. Upload the provided `Leave_Transactions_648648.xlsx` file
4. **Expected**: 
   - Success message showing number of leave transactions found
   - ⚠️ Warning message appears about declined/cancelled leave
   - Warning includes checkboxes for data validation requirements
   - Confirmation checkbox appears
   - Preview section appears

#### Test 17: Data Validation Warning
1. After uploading a file, look for the warning box
2. **Expected**:
   - Orange warning box with "⚠️ IMPORTANT: Data Validation Required"
   - Lists requirements:
     - Remove Declined leave transactions
     - Remove Cancelled leave transactions  
     - Only Approved leave remains
   - Checkbox: "I confirm that all declined and cancelled leave transactions have been removed"
   - Info message: "Please confirm that declined/cancelled leave has been removed"
3. Try to find the Process button without checking the box
4. **Expected**: Button is not visible until checkbox is checked

#### Test 18: Preview Leave Transactions
1. Click to expand "📋 Preview Leave Transactions"
2. **Expected**: 
   - Table showing first 10 leave records
   - Columns: Emp. Number, Employee Name, Leave Description, Start Date, End Date, No Days

#### Test 19: Confirm and Process Leave
1. Check the confirmation checkbox
2. **Expected**: "Process Leave Breakdown" button appears
3. Click "🔄 Process Leave Breakdown" button
4. **Expected**: 
   - Processing spinner appears briefly
   - Success message with daily records count
   - Results preview table appears
   - Download button appears

#### Test 20: Verify Calculations
Check the preview for:
1. **Full Day Leave**: 
   - Find a Monday entry
   - Should show 8.5 hours (or employee's Monday hours)
2. **Partial Day Leave**: 
   - Look for an entry where "Daily Hours" is not a full day
   - Verify calculation: e.g., 0.5 day × 8.5 hours = 4.25 hours
3. **Friday Hours**: 
   - Find a Friday entry
   - Should show different hours (e.g., 5.0 or 6.0)
4. **No Weekend Days**: 
   - Verify no Saturday or Sunday entries appear

#### Test 21: Download Report
1. Click "📥 Download Leave Breakdown"
2. **Expected**: 
   - Excel file downloads
   - Filename includes timestamp
3. Open the file
4. **Expected**: 
   - Professional formatting
   - Columns: Employee Number, Employee Name, Initials, Leave Description, Leave Type Description, Date, Day of Week, Daily Hours
   - All data properly formatted

### ✅ Phase 6: Help Documentation
1. Go to **Help** tab
2. Verify all sections are readable:
   - Overview
   - Getting Started
   - File Format
   - How It Works
   - Security
   - Tips

### ✅ Phase 7: Data Persistence Testing

#### Test 22: Employee Data Persistence
1. Add or edit an employee
2. Close the app (Ctrl+C in terminal)
3. Restart the app: `streamlit run app.py`
4. Login again
5. **Expected**: Your changes are still there

#### Test 23: User Data Persistence
1. Add a test user as admin
2. Close and restart the app
3. **Expected**: The user still exists and can login

#### Test 24: Session Management
1. Login to the app
2. Open a new browser tab
3. Go to http://localhost:8501
4. **Expected**: You're still logged in (same session)
5. Logout in one tab
6. **Expected**: Other tab also logs out (when refreshed)

## Testing Edge Cases

### Edge Case 1: Admin Password Change
1. Login as admin
2. Go to Admin Panel
3. Find admin user
4. Reset password to something new (e.g., `newadmin456`)
5. Logout
6. Login with new password
7. **Expected**: Works with new password

### Edge Case 2: Last Admin Protection
1. Create another admin user
2. Try to delete the original admin
3. **Expected**: Should work (since there's another admin)
4. Try to delete the last remaining admin
5. **Expected**: Warning message, cannot delete

### Edge Case 3: Empty Employee List
1. Delete all employees (or start fresh)
2. Go to Process Leave tab
3. **Expected**: Warning message "Please add employees first"
4. Upload leave file
5. **Expected**: Still shows warning

### Edge Case 4: Mismatched Leave Data
1. Upload a leave file with employees not in your system
2. Process the file
3. **Expected**: 
   - Only matching employees processed
   - Warning if no matches found

## Performance Testing

### Test 25: Large Employee List
- With 34 employees loaded from seed
- Navigate through all tabs
- **Expected**: Fast response times (< 1 second)

### Test 26: Large Leave File
- Upload the provided leave transactions file
- Process it
- **Expected**: 
  - Completes in < 5 seconds
  - All records processed correctly

## Common Issues & Solutions

### Issue: "Module not found" error
**Solution**: 
```bash
pip install -r requirements.txt
```

### Issue: Port 8501 already in use
**Solution**: 
```bash
streamlit run app.py --server.port 8502
```

### Issue: Logo not displaying
**Solution**: 
- Verify `RDS_Logo.jpg` is in the same folder as `app.py`
- Try refreshing the browser

### Issue: Cannot login after password change
**Solution**: 
- Delete `users.csv` file
- Restart app (creates new default admin)

### Issue: Employees not appearing
**Solution**: 
- Check if `employee_data.csv` exists
- If starting fresh, copy from `employee_data_seed.csv`

## Test Results Checklist

Use this checklist to track your testing:

- [ ] Test 1: Default Admin Login
- [ ] Test 2: Failed Login
- [ ] Test 3: Empty Fields
- [ ] Test 4: Main App Layout
- [ ] Test 5: Logout Functionality
- [ ] Test 6: Add New User
- [ ] Test 7: Password Reset
- [ ] Test 8: Test New User Login
- [ ] Test 9: Deactivate User
- [ ] Test 10: Reactivate User
- [ ] Test 11: Add Employee
- [ ] Test 12: Load Seed Data
- [ ] Test 13: Search Employee
- [ ] Test 14: Edit Employee
- [ ] Test 15: Delete Employee
- [ ] Test 16: Upload Leave File
- [ ] Test 17: Data Validation Warning
- [ ] Test 18: Preview Leave Transactions
- [ ] Test 19: Confirm and Process Leave
- [ ] Test 20: Verify Calculations
- [ ] Test 21: Download Report
- [ ] Test 22: Employee Data Persistence
- [ ] Test 23: User Data Persistence
- [ ] Test 24: Session Management
- [ ] Test 25: Large Employee List
- [ ] Test 26: Large Leave File

## Ready for Deployment?

✅ **You're ready to deploy if:**
- All core tests pass (Tests 1-20)
- No critical errors encountered
- Data persists correctly
- Calculations are accurate
- UI looks professional

⚠️ **Fix before deploying if:**
- Login doesn't work
- Logo doesn't display
- Calculations are incorrect
- Data doesn't persist
- Any critical functionality broken

## Next Steps After Testing

1. ✅ All tests passed? Great!
2. 📝 Document any issues found
3. 🔧 Fix any problems
4. 🚀 Follow DEPLOYMENT.md to publish on Streamlit Cloud
5. 👥 Add your team members through Admin Panel
6. 🎉 Start using the app!

---

**Need help?** Check the other documentation files:
- README.md - User guide
- AUTHENTICATION.md - Security guide
- DEPLOYMENT.md - Publishing guide
- PROJECT_OVERVIEW.md - Technical details
