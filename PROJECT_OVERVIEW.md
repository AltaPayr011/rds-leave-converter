# 📅 RDS PaySpace Leave Converter for OpenTime - Project Overview

## 📦 What's Included

Your complete authenticated Streamlit app is ready! Here's what's in the package:

### Core Application Files
- **`app.py`** - Main Streamlit application (350+ lines)
- **`requirements.txt`** - Python dependencies
- **`.gitignore`** - Git configuration (excludes user data)

### Data Files
- **`employee_data_seed.csv`** - Pre-populated with 34 employees
- **`employee_data_template.csv`** - Empty template showing format
- **`employee_data.csv`** - Created automatically by the app (not included in git)
- **`users.csv`** - User credentials (created automatically, not in git)
- **`RDS_Logo.jpg`** - Rob Dyer Surgical company logo

### Documentation
- **`README.md`** - Complete user guide
- **`DEPLOYMENT.md`** - Step-by-step deployment instructions
- **`SEED_DATA.md`** - How to use the seed data
- **`PROJECT_OVERVIEW.md`** - This file

### Quick Start Scripts
- **`start.sh`** - Quick start for Mac/Linux
- **`start.bat`** - Quick start for Windows

## 🎯 Features

### Authentication & Security
✅ Secure login system with bcrypt password encryption
✅ Session-based authentication
✅ Admin panel for user management
✅ Role-based access (Admin / Regular User)
✅ Default admin account with mandatory password change

### Employee Management
✅ Add, edit, and delete employees
✅ Customize working hours for each day of the week
✅ Search and filter employees
✅ Automatic data persistence
✅ Support for non-standard work schedules

### Leave Processing
✅ Upload Excel leave transaction files
✅ Automatic daily breakdown generation
✅ Partial day leave calculations
✅ Weekend exclusion (automatic)
✅ Excel export with formatting

### User Interface
✅ Clean, modern design with tabs
✅ Responsive layout
✅ Real-time data updates
✅ Preview before download
✅ Built-in help documentation

## 🚀 Three Ways to Get Started

### 1. Test Locally (Fastest)

**Mac/Linux:**
```bash
cd leave_breakdown_app
./start.sh
```

**Windows:**
```
cd leave_breakdown_app
start.bat
```

**Manual:**
```bash
pip install -r requirements.txt
streamlit run app.py
```

### 2. Deploy to Streamlit Cloud (Recommended for Production)

1. Create a GitHub repository
2. Upload all files from `leave_breakdown_app` folder
3. Go to https://share.streamlit.io
4. Connect your repository
5. Deploy!

See `DEPLOYMENT.md` for detailed instructions.

### 3. Deploy to Other Platforms

The app works on any platform that supports Streamlit:
- Heroku
- Google Cloud Run
- AWS EC2
- Azure App Service

## 📊 How It Works

```
User Flow:
1. Login with credentials → Session created
2. (Admin) Manage users → Stored in users.csv
3. Add/manage employees → Stored in employee_data.csv
4. Upload leave transactions → Processed in memory
5. Click "Process" → Algorithm runs
6. Download results → Excel file generated
7. Results discarded → Only employee/user data persists
```

### Processing Logic

```python
For each leave transaction:
  For each day in date range:
    If not weekend:
      If partial day:
        hours = fraction × daily_hours
      Else:
        hours = daily_hours
      Add to breakdown
```

## 📋 File Format Requirements

### Leave Transactions File
Excel file with columns starting at row 8:
- Emp. Number
- Employee Name
- Initials
- Leave Description
- Leave Type Description
- Start Date
- End Date
- No Days

### Employee Data File (CSV)
- Employee Number
- First Name
- Last Name
- Monday (hours)
- Tuesday (hours)
- Wednesday (hours)
- Thursday (hours)
- Friday (hours)

## 🔧 Technical Details

### Dependencies
- **Streamlit 1.28+** - Web framework
- **Pandas 2.0+** - Data processing
- **OpenPyXL 3.1+** - Excel operations
- **bcrypt 4.0+** - Password encryption
- **Pillow 10.0+** - Image handling (for logo)

### Data Storage
- **Development**: Local CSV file
- **Production**: Consider cloud storage for persistence

### Security
- **Authentication**: Login required with username/password
- **Password encryption**: bcrypt hashing (industry standard)
- **Session management**: Streamlit session state
- **Admin panel**: User management restricted to admins
- **Data protection**: User credentials never committed to Git

## 🎨 Customization Ideas

Want to extend the app? Consider adding:

1. **Authentication**
   - Streamlit auth
   - Google OAuth
   - Custom login

2. **Cloud Storage**
   - Google Sheets backend
   - PostgreSQL database
   - Firebase

3. **Advanced Features**
   - Email notifications
   - Calendar integration
   - Approval workflows
   - Analytics dashboard

4. **Export Options**
   - PDF reports
   - CSV exports
   - Email delivery

## 📱 Deployment Recommendations

### For Personal Use
- Run locally with `start.sh` or `start.bat`
- No deployment needed

### For Small Team (< 10 users)
- Deploy to Streamlit Cloud (free)
- Share the URL
- Users add employees as needed

### For Organization (> 10 users)
- Consider Streamlit Cloud Pro
- Add authentication
- Use cloud database
- Regular backups

## 🐛 Troubleshooting

### App won't start
```bash
# Reinstall dependencies
pip install -r requirements.txt --upgrade

# Check Python version (need 3.8+)
python --version
```

### Employee data not saving
- Check file permissions
- Ensure `employee_data.csv` can be created
- Check disk space

### Upload errors
- Verify file format matches requirements
- Check Excel file isn't corrupted
- Ensure headers start at row 8

### Calculation issues
- Verify employee hours are set correctly
- Check for missing employee numbers
- Review partial day calculations

## 📞 Support

- **Documentation**: Check README.md and other .md files
- **Issues**: Open issue on GitHub (if published)
- **Enhancements**: Fork and customize!

## 📄 License

MIT License - Free to use and modify

## 🙏 Credits

Built with:
- Streamlit framework
- Pandas library
- OpenPyXL library
- Python 3.8+

---

**Ready to get started?**
1. Choose your deployment method above
2. Follow the instructions
3. Start managing leave breakdowns!

Questions? Check the documentation files or reach out for support.
