import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import io
import os
import bcrypt
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="RDS PaySpace Leave Converter",
    page_icon="📅",
    layout="wide"
)

# File paths
EMPLOYEE_DATA_FILE = "employee_data.csv"
USERS_FILE = "users.csv"

# ==================== HELPER FUNCTIONS ====================

def find_column(df, possible_names):
    """
    Find a column in the dataframe that matches one of the possible names.
    Handles variations in spacing, capitalization, and punctuation.
    """
    # Create a mapping of normalized names to actual column names
    col_map = {}
    for col in df.columns:
        # Normalize: strip whitespace, lowercase, remove extra spaces
        normalized = str(col).strip().lower()
        normalized = ' '.join(normalized.split())  # Remove extra spaces
        col_map[normalized] = col
    
    # Try each possible name
    for name in possible_names:
        normalized_name = str(name).strip().lower()
        normalized_name = ' '.join(normalized_name.split())
        
        if normalized_name in col_map:
            return col_map[normalized_name]
    
    return None

def normalize_leave_dataframe(df):
    """
    Normalize column names in the leave transactions dataframe.
    Maps various column name formats to standard names.
    """
    # Define column mappings
    column_mappings = {
        'Emp. Number': ['emp. number', 'emp number', 'employee number', 'empnumber', 'emp.number', 'emp . number'],
        'Employee Name': ['employee name', 'emp name', 'name', 'employeename', 'emp. name'],
        'Initials': ['initials', 'initial'],
        'Leave Description': ['leave description', 'leavedescription', 'description', 'leave desc'],
        'Leave Type Description': ['leave type description', 'leave type', 'leavetype', 'type description', 'leave type desc'],
        'Start Date': ['start date', 'startdate', 'from date', 'date from', 'start'],
        'End Date': ['end date', 'enddate', 'to date', 'date to', 'end'],
        'No Days': ['no days', 'nodays', 'days', 'number of days', 'no. days', 'no.days', 'no . days']
    }
    
    # Create new column name mapping
    rename_dict = {}
    missing_columns = []
    
    for standard_name, variations in column_mappings.items():
        found_col = find_column(df, [standard_name] + variations)
        if found_col:
            if found_col != standard_name:
                rename_dict[found_col] = standard_name
        else:
            missing_columns.append(standard_name)
    
    # Rename columns
    if rename_dict:
        df = df.rename(columns=rename_dict)
    
    # Check for missing required columns
    if missing_columns:
        available_cols = ', '.join(df.columns.tolist())
        raise ValueError(
            f"Missing required columns: {', '.join(missing_columns)}\n\n"
            f"Available columns in your file: {available_cols}\n\n"
            f"Please ensure your Excel file has these column headers."
        )
    
    return df

# ==================== USER AUTHENTICATION ====================

def hash_password(password):
    """Hash a password using bcrypt"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(password, hashed):
    """Verify a password against a hash"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

def load_users():
    """Load users from CSV file"""
    if os.path.exists(USERS_FILE):
        return pd.read_csv(USERS_FILE)
    else:
        # Create default admin user
        default_users = pd.DataFrame([{
            'username': 'admin',
            'password': hash_password('admin123'),
            'full_name': 'System Administrator',
            'is_admin': True,
            'active': True,
            'created_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }])
        default_users.to_csv(USERS_FILE, index=False)
        return default_users

def save_users(df):
    """Save users to CSV file"""
    df.to_csv(USERS_FILE, index=False)

def authenticate(username, password):
    """Authenticate a user"""
    users_df = load_users()
    user = users_df[users_df['username'] == username]
    
    if len(user) == 0:
        return False, None
    
    user = user.iloc[0]
    
    if not user['active']:
        return False, None
    
    if verify_password(password, user['password']):
        return True, user
    
    return False, None

def add_user(username, password, full_name, is_admin=False):
    """Add a new user"""
    users_df = load_users()
    
    # Check if user already exists
    if username in users_df['username'].values:
        return False, "Username already exists"
    
    new_user = pd.DataFrame([{
        'username': username,
        'password': hash_password(password),
        'full_name': full_name,
        'is_admin': is_admin,
        'active': True,
        'created_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }])
    
    users_df = pd.concat([users_df, new_user], ignore_index=True)
    save_users(users_df)
    return True, "User added successfully"

# ==================== EMPLOYEE DATA FUNCTIONS ====================

def load_employee_data():
    """Load employee data from CSV file"""
    if os.path.exists(EMPLOYEE_DATA_FILE):
        return pd.read_csv(EMPLOYEE_DATA_FILE)
    else:
        return pd.DataFrame(columns=[
            'Employee Number', 'First Name', 'Last Name', 
            'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'
        ])

def save_employee_data(df):
    """Save employee data to CSV file"""
    df.to_csv(EMPLOYEE_DATA_FILE, index=False)

def process_leave_breakdown(leave_df, employee_df):
    """Process leave transactions and create daily breakdown"""
    breakdown_data = []
    
    hours_dict = {}
    for _, row in employee_df.iterrows():
        emp_num = row['Employee Number']
        hours_dict[emp_num] = {
            'first_name': row['First Name'],
            'last_name': row['Last Name'],
            'monday': row['Monday'],
            'tuesday': row['Tuesday'],
            'wednesday': row['Wednesday'],
            'thursday': row['Thursday'],
            'friday': row['Friday']
        }
    
    for idx, row in leave_df.iterrows():
        emp_num = row['Emp. Number']
        emp_name = row['Employee Name']
        initials = row['Initials']
        leave_desc = row['Leave Description']
        leave_type = row['Leave Type Description']
        start_date = pd.to_datetime(row['Start Date'])
        end_date = pd.to_datetime(row['End Date'])
        no_days = row['No Days']
        
        if emp_num in hours_dict:
            emp_hours = hours_dict[emp_num]
        else:
            continue
        
        is_partial_day = (start_date == end_date) and (no_days < 1)
        
        current_date = start_date
        while current_date <= end_date:
            day_of_week = current_date.weekday()
            
            if day_of_week not in [5, 6]:
                day_names = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
                base_daily_hours = emp_hours[day_names[day_of_week]]
                
                if is_partial_day and pd.notna(base_daily_hours):
                    daily_hours = no_days * base_daily_hours
                else:
                    daily_hours = base_daily_hours if pd.notna(base_daily_hours) else 0
                
                breakdown_data.append({
                    'Employee Number': emp_num,
                    'Employee Name': emp_name,
                    'Initials': initials,
                    'Leave Description': leave_desc,
                    'Leave Type Description': leave_type,
                    'Date': current_date.strftime('%Y-%m-%d'),
                    'Day of Week': current_date.strftime('%A'),
                    'Daily Hours': daily_hours
                })
            
            current_date += timedelta(days=1)
    
    return pd.DataFrame(breakdown_data)

# ==================== LOGIN SCREEN ====================

def show_login():
    """Display login screen"""
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Display logo (centered and smaller)
        if os.path.exists('RDS_Logo.jpg'):
            logo = Image.open('RDS_Logo.jpg')
            # Create three columns to center the logo
            logo_col1, logo_col2, logo_col3 = st.columns([1, 2, 1])
            with logo_col2:
                st.image(logo, width=250)  # Fixed width for smaller logo
        
        st.markdown("<h1 style='text-align: center;'>RDS PaySpace Leave Converter</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: #666;'>for OpenTime</h3>", unsafe_allow_html=True)
        st.markdown("---")
        
        with st.form("login_form"):
            username = st.text_input("Username", key="login_username")
            password = st.text_input("Password", type="password", key="login_password")
            submit = st.form_submit_button("Login", type="primary", width="stretch")
            
            if submit:
                if username and password:
                    success, user_data = authenticate(username, password)
                    if success:
                        st.session_state['authenticated'] = True
                        st.session_state['username'] = username
                        st.session_state['full_name'] = user_data['full_name']
                        st.session_state['is_admin'] = user_data['is_admin']
                        st.rerun()
                    else:
                        st.error("❌ Invalid username or password")
                else:
                    st.error("❌ Please enter both username and password")

# ==================== MAIN APP ====================

def show_main_app():
    """Display main application after login"""
    
    # Header with logout
    col1, col2, col3 = st.columns([2, 3, 2])
    with col1:
        if os.path.exists('RDS_Logo.jpg'):
            logo = Image.open('RDS_Logo.jpg')
            st.image(logo, width=120)  # Smaller header logo
    with col2:
        st.markdown("<h2 style='text-align: center; margin-top: 20px;'>RDS PaySpace Leave Converter for OpenTime</h2>", unsafe_allow_html=True)
    with col3:
        st.write(f"**Logged in as:** {st.session_state['full_name']}")
        if st.button("🚪 Logout", type="secondary"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
    
    st.markdown("---")
    
    # Create tabs based on admin status
    if st.session_state.get('is_admin', False):
        tabs = st.tabs(["👥 Manage Employees", "📊 Process Leave", "⚙️ Admin Panel", "👤 My Profile", "ℹ️ Help"])
        tab1, tab2, tab3, tab4, tab5 = tabs
    else:
        tabs = st.tabs(["👥 Manage Employees", "📊 Process Leave", "👤 My Profile", "ℹ️ Help"])
        tab1, tab2, tab4, tab5 = tabs
        tab3 = None
    
    # Tab 1: Employee Management
    with tab1:
        st.header("Employee Management")
        
        employee_df = load_employee_data()
        
        # Add new employee section
        with st.expander("➕ Add New Employee", expanded=False):
            col1, col2 = st.columns(2)
            with col1:
                new_emp_num = st.text_input("Employee Number", key="new_emp_num")
                new_first_name = st.text_input("First Name", key="new_first")
                new_last_name = st.text_input("Last Name", key="new_last")
            
            with col2:
                st.write("**Working Hours per Day**")
                new_mon = st.number_input("Monday", min_value=0.0, max_value=24.0, value=8.5, step=0.25, key="new_mon")
                new_tue = st.number_input("Tuesday", min_value=0.0, max_value=24.0, value=8.5, step=0.25, key="new_tue")
                new_wed = st.number_input("Wednesday", min_value=0.0, max_value=24.0, value=8.5, step=0.25, key="new_wed")
                new_thu = st.number_input("Thursday", min_value=0.0, max_value=24.0, value=8.5, step=0.25, key="new_thu")
                new_fri = st.number_input("Friday", min_value=0.0, max_value=24.0, value=6.0, step=0.25, key="new_fri")
            
            if st.button("Add Employee", type="primary"):
                if new_emp_num and new_first_name and new_last_name:
                    if new_emp_num in employee_df['Employee Number'].values:
                        st.error(f"Employee {new_emp_num} already exists!")
                    else:
                        new_row = pd.DataFrame([{
                            'Employee Number': new_emp_num,
                            'First Name': new_first_name,
                            'Last Name': new_last_name,
                            'Monday': new_mon,
                            'Tuesday': new_tue,
                            'Wednesday': new_wed,
                            'Thursday': new_thu,
                            'Friday': new_fri
                        }])
                        employee_df = pd.concat([employee_df, new_row], ignore_index=True)
                        save_employee_data(employee_df)
                        st.success(f"✅ Employee {new_emp_num} added successfully!")
                        st.rerun()
                else:
                    st.error("Please fill in all required fields!")
        
        st.markdown("---")
        
        # Display and edit existing employees
        st.subheader("Current Employees")
        
        if len(employee_df) == 0:
            st.info("No employees found. Add your first employee above!")
        else:
            st.write(f"**Total Employees:** {len(employee_df)}")
            
            search = st.text_input("🔍 Search by Employee Number or Name", "")
            if search:
                mask = (
                    employee_df['Employee Number'].astype(str).str.contains(search, case=False) |
                    employee_df['First Name'].astype(str).str.contains(search, case=False) |
                    employee_df['Last Name'].astype(str).str.contains(search, case=False)
                )
                display_df = employee_df[mask]
            else:
                display_df = employee_df
            
            for idx, row in display_df.iterrows():
                with st.expander(f"{row['Employee Number']} - {row['First Name']} {row['Last Name']}"):
                    col1, col2, col3 = st.columns([2, 3, 1])
                    
                    with col1:
                        st.text_input("Employee Number", value=row['Employee Number'], disabled=True, key=f"emp_{idx}")
                        edit_first = st.text_input("First Name", value=row['First Name'], key=f"first_{idx}")
                        edit_last = st.text_input("Last Name", value=row['Last Name'], key=f"last_{idx}")
                    
                    with col2:
                        st.write("**Working Hours**")
                        edit_mon = st.number_input("Monday", value=float(row['Monday']), min_value=0.0, max_value=24.0, step=0.25, key=f"mon_{idx}")
                        edit_tue = st.number_input("Tuesday", value=float(row['Tuesday']), min_value=0.0, max_value=24.0, step=0.25, key=f"tue_{idx}")
                        edit_wed = st.number_input("Wednesday", value=float(row['Wednesday']), min_value=0.0, max_value=24.0, step=0.25, key=f"wed_{idx}")
                        edit_thu = st.number_input("Thursday", value=float(row['Thursday']), min_value=0.0, max_value=24.0, step=0.25, key=f"thu_{idx}")
                        edit_fri = st.number_input("Friday", value=float(row['Friday']), min_value=0.0, max_value=24.0, step=0.25, key=f"fri_{idx}")
                    
                    with col3:
                        st.write("")
                        st.write("")
                        if st.button("💾 Save", key=f"save_{idx}", type="primary"):
                            employee_df.at[idx, 'First Name'] = edit_first
                            employee_df.at[idx, 'Last Name'] = edit_last
                            employee_df.at[idx, 'Monday'] = edit_mon
                            employee_df.at[idx, 'Tuesday'] = edit_tue
                            employee_df.at[idx, 'Wednesday'] = edit_wed
                            employee_df.at[idx, 'Thursday'] = edit_thu
                            employee_df.at[idx, 'Friday'] = edit_fri
                            save_employee_data(employee_df)
                            st.success("✅ Updated!")
                            st.rerun()
                        
                        if st.button("🗑️ Delete", key=f"del_{idx}"):
                            employee_df = employee_df.drop(idx).reset_index(drop=True)
                            save_employee_data(employee_df)
                            st.success("✅ Deleted!")
                            st.rerun()
    
    # Tab 2: Process Leave
    with tab2:
        st.header("Process Leave Transactions")
        
        employee_df = load_employee_data()
        
        if len(employee_df) == 0:
            st.warning("⚠️ Please add employees first in the 'Manage Employees' tab before processing leave transactions.")
        else:
            st.info(f"📊 {len(employee_df)} employees loaded and ready for processing")
            
            uploaded_file = st.file_uploader(
                "Upload Leave Transactions Excel File",
                type=['xlsx'],
                help="Upload your leave transactions file (same format as Leave_Transactions_648648.xlsx)"
            )
            
            if uploaded_file is not None:
                try:
                    # Read the Excel file
                    leave_df = pd.read_excel(uploaded_file, sheet_name=0, header=7)
                    
                    # Normalize column names to handle variations
                    leave_df = normalize_leave_dataframe(leave_df)
                    
                    # Filter out group headers and invalid rows
                    leave_df = leave_df[leave_df['Emp. Number'] != 'Group : All Groups'].reset_index(drop=True)
                    leave_df = leave_df[leave_df['No Days'] >= 0].reset_index(drop=True)
                    
                    st.success(f"✅ File uploaded successfully! Found {len(leave_df)} leave transactions.")
                    
                    # Warning message about declined/cancelled leave
                    st.warning("⚠️ **IMPORTANT: Data Validation Required**")
                    st.markdown("""
                    Before processing this file, please ensure you have:
                    - ✅ Removed all **Declined** leave transactions
                    - ✅ Removed all **Cancelled** leave transactions
                    - ✅ Verified that only **Approved** leave transactions remain
                    
                    Processing declined or cancelled leave will result in incorrect calculations.
                    """)
                    
                    # Confirmation checkbox
                    confirmed = st.checkbox(
                        "✓ I confirm that all declined and cancelled leave transactions have been removed from this file",
                        key="confirm_data_cleanup"
                    )
                    
                    with st.expander("📋 Preview Leave Transactions"):
                        st.dataframe(
                            leave_df[['Emp. Number', 'Employee Name', 'Leave Description', 
                                     'Start Date', 'End Date', 'No Days']].head(10),
                            width="stretch"
                        )
                    
                    # Only enable processing if confirmed
                    if confirmed:
                        if st.button("🔄 Process Leave Breakdown", type="primary"):
                            with st.spinner("Processing leave breakdown..."):
                                breakdown_df = process_leave_breakdown(leave_df, employee_df)
                                
                                if len(breakdown_df) > 0:
                                    st.success(f"✅ Successfully created {len(breakdown_df)} daily leave records!")
                                    
                                    st.subheader("Results Preview")
                                    st.dataframe(breakdown_df.head(20), width="stretch")
                                    
                                    output = io.BytesIO()
                                    with pd.ExcelWriter(output, engine='openpyxl') as writer:
                                        breakdown_df.to_excel(writer, index=False, sheet_name='Leave Breakdown')
                                    
                                    st.download_button(
                                        label="📥 Download Leave Breakdown",
                                        data=output.getvalue(),
                                        file_name=f"Leave_Breakdown_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
                                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                                        type="primary"
                                    )
                                else:
                                    st.warning("No matching employees found in the leave transactions.")
                    else:
                        st.info("👆 Please confirm that declined/cancelled leave has been removed before processing.")
                    
                except Exception as e:
                    error_message = str(e)
                    st.error(f"❌ Error processing file:")
                    st.code(error_message)
                    
                    # Provide helpful guidance based on error type
                    if "Missing required columns" in error_message:
                        st.info("""
                        📝 **Column Name Issue**
                        
                        The app couldn't find the required columns in your Excel file. This usually happens when:
                        - Column names have been changed
                        - The file format is different than expected
                        - Data starts on a different row
                        
                        **Required columns:**
                        - Emp. Number (or Employee Number)
                        - Employee Name
                        - Initials
                        - Leave Description
                        - Leave Type Description
                        - Start Date
                        - End Date
                        - No Days (or Number of Days)
                        
                        **The app accepts variations of these names** (e.g., "Emp. Number", "Emp Number", "Employee Number" all work).
                        
                        Please check your Excel file has these column headers (row 8 typically).
                        """)
                    else:
                        st.info("""
                        📝 **Troubleshooting Tips:**
                        1. Make sure your Excel file has column headers on **row 8**
                        2. Check that column names include: "Emp. Number", "Employee Name", "Start Date", etc.
                        3. Ensure dates are in proper date format (not text)
                        4. Remove any completely blank rows
                        5. Make sure "No Days" column contains numbers
                        
                        If the problem persists, please check the file format matches the example Leave_Transactions file.
                        """)
    
    # Tab 3: Admin Panel (only for admins)
    if tab3 is not None:
        with tab3:
            st.header("⚙️ Admin Panel - User Management")
            
            users_df = load_users()
            
            # Add new user
            with st.expander("➕ Add New User", expanded=False):
                new_username = st.text_input("Username", key="new_username")
                new_password = st.text_input("Password", type="password", key="new_password")
                new_password_confirm = st.text_input("Confirm Password", type="password", key="new_password_confirm")
                new_full_name = st.text_input("Full Name", key="new_full_name")
                new_is_admin = st.checkbox("Admin Access", key="new_is_admin")
                
                if st.button("Add User", type="primary"):
                    if new_username and new_password and new_full_name:
                        if new_password != new_password_confirm:
                            st.error("❌ Passwords do not match!")
                        elif len(new_password) < 6:
                            st.error("❌ Password must be at least 6 characters!")
                        else:
                            success, message = add_user(new_username, new_password, new_full_name, new_is_admin)
                            if success:
                                st.success(f"✅ {message}")
                                st.rerun()
                            else:
                                st.error(f"❌ {message}")
                    else:
                        st.error("❌ Please fill in all required fields!")
            
            st.markdown("---")
            
            # Display existing users
            st.subheader("Current Users")
            st.write(f"**Total Users:** {len(users_df)}")
            
            for idx, user in users_df.iterrows():
                with st.expander(f"{'👑 ' if user['is_admin'] else '👤 '}{user['username']} - {user['full_name']}"):
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.write(f"**Username:** {user['username']}")
                        st.write(f"**Full Name:** {user['full_name']}")
                        st.write(f"**Admin:** {'Yes' if user['is_admin'] else 'No'}")
                        st.write(f"**Status:** {'Active' if user['active'] else 'Inactive'}")
                        st.write(f"**Created:** {user['created_date']}")
                    
                    with col2:
                        # Reset password
                        with st.form(f"reset_password_{idx}"):
                            st.write("**Reset Password**")
                            new_pwd = st.text_input("New Password", type="password", key=f"pwd_{idx}")
                            new_pwd_confirm = st.text_input("Confirm Password", type="password", key=f"pwd_confirm_{idx}")
                            
                            if st.form_submit_button("Reset Password"):
                                if new_pwd and new_pwd == new_pwd_confirm:
                                    if len(new_pwd) >= 6:
                                        users_df.at[idx, 'password'] = hash_password(new_pwd)
                                        save_users(users_df)
                                        st.success("✅ Password reset successfully!")
                                        st.rerun()
                                    else:
                                        st.error("❌ Password must be at least 6 characters!")
                                else:
                                    st.error("❌ Passwords do not match!")
                    
                    # Deactivate/Activate user (cannot deactivate self or last admin)
                    col3, col4 = st.columns(2)
                    with col3:
                        if user['username'] != st.session_state['username']:
                            if user['active']:
                                # Check if deactivating last admin
                                active_admins = users_df[(users_df['is_admin'] == True) & (users_df['active'] == True)]
                                if user['is_admin'] and len(active_admins) <= 1:
                                    st.warning("⚠️ Cannot deactivate the last admin")
                                else:
                                    if st.button("🔒 Deactivate User", key=f"deactivate_{idx}"):
                                        users_df.at[idx, 'active'] = False
                                        save_users(users_df)
                                        st.success("✅ User deactivated!")
                                        st.rerun()
                            else:
                                if st.button("🔓 Activate User", key=f"activate_{idx}"):
                                    users_df.at[idx, 'active'] = True
                                    save_users(users_df)
                                    st.success("✅ User activated!")
                                    st.rerun()
                        else:
                            st.info("ℹ️ Cannot modify your own account")
                    
                    with col4:
                        # Delete user (cannot delete self)
                        if user['username'] != st.session_state['username']:
                            # Check if deleting last admin
                            active_admins = users_df[(users_df['is_admin'] == True) & (users_df['active'] == True)]
                            if user['is_admin'] and len(active_admins) <= 1:
                                st.warning("⚠️ Cannot delete the last admin")
                            else:
                                if st.button("🗑️ Delete User", key=f"delete_user_{idx}"):
                                    users_df = users_df.drop(idx).reset_index(drop=True)
                                    save_users(users_df)
                                    st.success("✅ User deleted!")
                                    st.rerun()
    
    # Tab 4: My Profile (for all users)
    with tab4:
        st.header("👤 My Profile")
        
        current_username = st.session_state.get('username')
        users_df = load_users()
        
        if current_username:
            user_row = users_df[users_df['username'] == current_username]
            
            if len(user_row) > 0:
                user_info = user_row.iloc[0]
                
                # Display account information
                st.subheader("Account Information")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.info(f"""
                    **Username:** {user_info['username']}  
                    **Full Name:** {user_info['full_name']}  
                    **Account Type:** {'Administrator' if user_info['is_admin'] else 'Regular User'}  
                    **Status:** {'Active' if user_info['active'] else 'Inactive'}  
                    **Created:** {user_info['created_date']}
                    """)
                
                st.markdown("---")
                
                # Change Password Section
                st.subheader("🔒 Change Password")
                st.write("Update your password to keep your account secure.")
                
                with st.form("change_password_form"):
                    current_password = st.text_input("Current Password", type="password", key="current_pwd")
                    new_password = st.text_input("New Password", type="password", key="new_pwd")
                    confirm_password = st.text_input("Confirm New Password", type="password", key="confirm_pwd")
                    
                    st.caption("💡 Tip: Use a strong password with at least 8 characters")
                    
                    submit_change = st.form_submit_button("🔄 Change Password", type="primary")
                    
                    if submit_change:
                        if not all([current_password, new_password, confirm_password]):
                            st.error("❌ All fields are required")
                        elif new_password != confirm_password:
                            st.error("❌ New passwords do not match")
                        elif len(new_password) < 6:
                            st.error("❌ New password must be at least 6 characters")
                        elif new_password == current_password:
                            st.error("❌ New password must be different from current password")
                        else:
                            # Verify current password
                            if bcrypt.checkpw(current_password.encode('utf-8'), user_info['password'].encode('utf-8')):
                                # Hash new password
                                new_hashed = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
                                
                                # Update password
                                users_df.loc[users_df['username'] == current_username, 'password'] = new_hashed
                                save_users(users_df)
                                
                                st.success("✅ Password changed successfully!")
                                st.info("💡 Please remember your new password. You will need it for your next login.")
                            else:
                                st.error("❌ Current password is incorrect")
            else:
                st.error("User information not found")
        else:
            st.error("Session error. Please logout and login again.")
    
    # Tab 5: Help
    with tab5:
        st.header("How to Use This App")
        
        st.markdown("""
        ### 📋 Overview
        The **RDS PaySpace Leave Converter for OpenTime** processes leave transaction files and creates detailed daily breakdowns showing exact hours for each employee's leave.
        
        ### 🚀 Getting Started
        
        #### 1. Login
        - Use your credentials to login
        - Default admin: username `admin`, password `admin123`
        - Change the admin password immediately after first login
        
        #### 2. Manage Employees
        - Navigate to the **Manage Employees** tab
        - Add employees with their working hours for each day of the week
        - Edit or delete employees as needed
        - Employee data is automatically saved
        
        #### 3. Process Leave Transactions
        - Go to the **Process Leave** tab
        - **Important:** Before uploading, ensure all declined and cancelled leave transactions are removed from the file
        - Upload your leave transactions Excel file
        - Read and confirm the data validation requirements
        - Click "Process Leave Breakdown"
        - Download the generated breakdown Excel file
        
        #### 4. Admin Panel (Admin Only)
        - Add new users to the system
        - Reset user passwords
        - Activate/deactivate users
        - Delete users (except last admin)
        
        ### 📊 File Format
        
        The leave transactions file should have these columns (starting at row 8):
        - Emp. Number
        - Employee Name
        - Initials
        - Leave Description
        - Leave Type Description
        - Start Date
        - End Date
        - No Days
        
        ### ⚙️ How It Works
        
        **Working Hours:**
        - Set different hours for each day of the week
        - Set hours to 0 for days an employee doesn't work
        - Example: Friday = 0 for employees who don't work Fridays
        
        **Partial Day Leave:**
        - For leave less than 1 day, hours are calculated as: `Fraction × Daily Hours`
        - Example: 0.5 day leave on a 8.5 hour day = 4.25 hours
        
        **Weekend Handling:**
        - Saturdays and Sundays are automatically excluded
        - Only weekdays (Monday-Friday) appear in the breakdown
        
        ### 🔐 Security
        - All passwords are encrypted using bcrypt
        - Session-based authentication
        - Admins can manage all users
        - Cannot delete or deactivate the last admin
        
        ### 💡 Tips
        - Keep employee data up to date for accurate calculations
        - Review the preview before downloading
        - Downloaded files are temporary - only employee data is retained
        - Change default admin password immediately
        - Create separate user accounts for each person
        """)
        
        st.markdown("---")
        st.info("💾 Data is stored locally in `employee_data.csv` and `users.csv`")

# ==================== MAIN APPLICATION LOGIC ====================

def main():
    """Main application entry point"""
    
    # Initialize session state
    if 'authenticated' not in st.session_state:
        st.session_state['authenticated'] = False
    
    # Show login or main app based on authentication status
    if not st.session_state['authenticated']:
        show_login()
    else:
        show_main_app()

if __name__ == "__main__":
    main()

# Footer
if st.session_state.get('authenticated', False):
    st.markdown("---")
    st.caption("RDS PaySpace Leave Converter for OpenTime | Built with Streamlit")
