# 📅 RDS PaySpace Leave Converter for OpenTime

A secure, authenticated Streamlit web application for processing employee leave transactions and generating detailed daily breakdowns with precise working hours calculations.

## Features

- 🔐 **Secure Authentication**: Login system with encrypted passwords
- 👑 **Admin Panel**: System administrators can manage user access
- 👥 **Employee Management**: Add, edit, and remove employees with customizable working hours per day
- 📊 **Leave Processing**: Upload leave transaction files and generate detailed breakdowns
- ⏰ **Flexible Hours**: Set different working hours for each day of the week
- 📥 **Easy Export**: Download processed leave breakdowns as Excel files
- 💾 **Data Persistence**: Employee and user data automatically saved

## Quick Start

### Default Admin Login

When you first run the app, use these credentials:
- **Username**: `admin`
- **Password**: `admin123`

⚠️ **Important**: 
- These credentials are NOT displayed on the login screen for security reasons
- Change the admin password immediately after first login!
- Store these credentials securely for initial setup

## Installation

### Local Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/leave-breakdown-app.git
cd leave-breakdown-app
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
streamlit run app.py
```

Or use the quick start scripts (automatically loads 34 employees from seed data):
```bash
./start.sh    # Mac/Linux
start.bat     # Windows
```

4. Open your browser to `http://localhost:8501`

### Deploy to Streamlit Cloud

1. Fork this repository to your GitHub account

2. Go to [share.streamlit.io](https://share.streamlit.io)

3. Sign in with GitHub

4. Click "New app"

5. Select:
   - **Repository**: Your forked repository
   - **Branch**: main
   - **Main file path**: app.py

6. Click "Deploy"

Your app will be live in a few minutes!

## How to Use

### 1. Login

First-time setup:
1. Run the app
2. Login with `admin` / `admin123`
3. Go to the Admin Panel
4. Change the admin password
5. Add users for your team

### 2. Manage Users (Admin Only)

Administrators can:
- Add new users
- Reset passwords for any user
- Activate/deactivate user accounts
- Delete users (except the last admin)

All regular users have the same access to employee and leave management features.

### 3. Manage Employees

- Navigate to the **Manage Employees** tab
- Click "Add New Employee" and fill in:
  - Employee Number
  - First Name
  - Last Name
  - Working hours for each day (Monday-Friday)
- Set hours to 0 for days an employee doesn't work
- Click "Add Employee" to save

**Editing Employees:**
- Find the employee in the list
- Click on their name to expand
- Modify the fields
- Click "Save" to update

**Deleting Employees:**
- Expand the employee's section
- Click "Delete"

### 4. Process Leave Transactions

- Go to the **Process Leave** tab
- Upload your leave transactions Excel file
- **IMPORTANT**: Ensure you have removed all declined and cancelled leave transactions from the file before uploading
- Check the confirmation box to proceed
- Click "Process Leave Breakdown"
- Review the preview
- Click "Download Leave Breakdown" to get your Excel file

### 5. File Format

Your leave transactions Excel file should have these columns (starting at row 8):
- Emp. Number
- Employee Name
- Initials
- Leave Description
- Leave Type Description
- Start Date
- End Date
- No Days

### 6. Data Preparation Requirements

**Before uploading your leave transactions file, you MUST:**

✅ **Remove Declined Leave Transactions**
- Filter or delete all leave requests with "Declined" status
- These should not be included in the final calculations

✅ **Remove Cancelled Leave Transactions**  
- Filter or delete all leave requests with "Cancelled" status
- These should not be included in the final calculations

✅ **Keep Only Approved Leave**
- Only approved/granted leave should remain in the file
- This ensures accurate leave calculations

**The app will prompt you to confirm this before processing.**

## Special Cases

**Partial Day Leave:**
- Hours calculated as: `Fraction of Day × Daily Working Hours`
- Example: 0.5 day leave on an 8.5 hour day = 4.25 hours

**Non-Working Days:**
- Set hours to 0 for days an employee doesn't work
- Example: Employee doesn't work Fridays → Set Friday hours to 0

**Specific Work Days:**
- Set hours to 0 for non-working weekdays
- Example: Employee only works Monday & Thursday → Set Tue/Wed/Fri to 0

**Weekends:**
- Automatically excluded from all calculations

## Data Storage

- **Employee data** is stored in `employee_data.csv`
- **User credentials** are stored in `users.csv` with bcrypt-encrypted passwords
- These files are created automatically when you run the app
- Uploaded leave transaction files are processed in memory and not stored
- Downloaded breakdown files are temporary and can be deleted

**Security Notes:**
- Passwords are hashed using bcrypt (never stored in plain text)
- `users.csv` is excluded from Git via `.gitignore`
- Session-based authentication ensures secure access
- Admin accounts have additional privileges for user management

## Tech Stack

- **Frontend**: Streamlit
- **Data Processing**: Pandas
- **Excel Operations**: OpenPyXL
- **Storage**: CSV file (local)

## Configuration

No additional configuration needed! The app creates `employee_data.csv` automatically.

## Support

For issues or questions, please open an issue on GitHub.

## License

MIT License - feel free to use and modify as needed!

---

Built with ❤️ using Streamlit
