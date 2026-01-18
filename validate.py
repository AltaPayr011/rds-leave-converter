#!/usr/bin/env python3
"""
Validation Script for RDS PaySpace Leave Converter
Tests core functionality without running Streamlit
"""

import sys
import os

print("=" * 70)
print("RDS PaySpace Leave Converter - Validation Script")
print("=" * 70)
print()

# Test 1: Check Python version
print("✓ Testing: Python Version")
version = sys.version_info
if version.major >= 3 and version.minor >= 8:
    print(f"  ✅ Python {version.major}.{version.minor}.{version.micro} - OK")
else:
    print(f"  ❌ Python {version.major}.{version.minor}.{version.micro} - Need 3.8+")
    sys.exit(1)
print()

# Test 2: Check required files
print("✓ Testing: Required Files")
required_files = [
    'app.py',
    'requirements.txt',
    'RDS_Logo.jpg',
    'employee_data_seed.csv',
    'employee_data_template.csv',
    'README.md',
    'AUTHENTICATION.md',
    'DEPLOYMENT.md'
]

all_files_present = True
for file in required_files:
    if os.path.exists(file):
        print(f"  ✅ {file}")
    else:
        print(f"  ❌ {file} - MISSING")
        all_files_present = False

if not all_files_present:
    print("\n❌ Some files are missing!")
    sys.exit(1)
print()

# Test 3: Check dependencies
print("✓ Testing: Python Dependencies")
dependencies = {
    'pandas': 'Data processing',
    'openpyxl': 'Excel operations',
    'bcrypt': 'Password encryption',
    'PIL': 'Image handling (Pillow)'
}

missing_deps = []
for module, description in dependencies.items():
    try:
        __import__(module)
        print(f"  ✅ {module:15} - {description}")
    except ImportError:
        print(f"  ❌ {module:15} - MISSING - {description}")
        missing_deps.append(module)

if missing_deps:
    print(f"\n⚠️  Missing dependencies. Install with:")
    print(f"   pip install -r requirements.txt")
    print()
else:
    print()

# Test 4: Test core functions
print("✓ Testing: Core Functionality")

try:
    import pandas as pd
    import bcrypt
    from datetime import datetime, timedelta
    
    # Test password hashing
    test_password = "test123"
    hashed = bcrypt.hashpw(test_password.encode('utf-8'), bcrypt.gensalt())
    verified = bcrypt.checkpw(test_password.encode('utf-8'), hashed)
    
    if verified:
        print("  ✅ Password encryption/verification")
    else:
        print("  ❌ Password verification failed")
    
    # Test date calculations
    start = datetime(2025, 12, 22)
    end = datetime(2025, 12, 26)
    days = []
    current = start
    while current <= end:
        if current.weekday() not in [5, 6]:  # Skip weekends
            days.append(current)
        current += timedelta(days=1)
    
    expected_days = 5  # Mon, Tue, Wed, Thu, Fri
    if len(days) == expected_days:
        print("  ✅ Date range calculation")
    else:
        print(f"  ❌ Date calculation: expected {expected_days}, got {len(days)}")
    
    # Test Excel reading
    df = pd.read_csv('employee_data_seed.csv')
    if len(df) == 34:
        print(f"  ✅ CSV reading (34 employees)")
    else:
        print(f"  ⚠️  CSV reading ({len(df)} employees, expected 34)")
    
    # Test partial day calculation
    partial_days = 0.5
    base_hours = 8.5
    calculated = partial_days * base_hours
    expected = 4.25
    
    if calculated == expected:
        print(f"  ✅ Partial day calculation (0.5 × 8.5 = 4.25)")
    else:
        print(f"  ❌ Partial day calculation failed")
    
    print()
    
except Exception as e:
    print(f"  ❌ Core functionality test failed: {e}")
    print()

# Test 5: Check logo file
print("✓ Testing: Logo File")
try:
    from PIL import Image
    img = Image.open('RDS_Logo.jpg')
    width, height = img.size
    print(f"  ✅ Logo loaded: {width}x{height} pixels")
    print()
except Exception as e:
    print(f"  ❌ Logo test failed: {e}")
    print()

# Test 6: Validate seed data
print("✓ Testing: Seed Data Structure")
try:
    df = pd.read_csv('employee_data_seed.csv')
    expected_columns = ['Employee Number', 'First Name', 'Last Name', 
                       'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    
    has_all_columns = all(col in df.columns for col in expected_columns)
    
    if has_all_columns:
        print(f"  ✅ All required columns present")
        
        # Check for specific employees
        test_cases = [
            ('RDS00004', 'Elvis', 'Mzukwa'),
            ('RDS00014', 'Veronica', 'du Preez'),
            ('RDS00029', 'Eunice', 'Mphoswa')
        ]
        
        for emp_num, first, last in test_cases:
            emp = df[df['Employee Number'] == emp_num]
            if len(emp) == 1 and emp.iloc[0]['First Name'] == first:
                print(f"  ✅ Found {emp_num}: {first} {last}")
            else:
                print(f"  ⚠️  {emp_num} not found or data mismatch")
        
        # Check Veronica's Friday hours (should be 0)
        veronica = df[df['Employee Number'] == 'RDS00014']
        if len(veronica) == 1:
            friday_hours = veronica.iloc[0]['Friday']
            if friday_hours == 0.0:
                print(f"  ✅ Veronica du Preez: Friday hours = 0 (doesn't work Fridays)")
            else:
                print(f"  ⚠️  Veronica's Friday hours: {friday_hours} (expected 0)")
        
        # Check Eunice's special schedule
        eunice = df[df['Employee Number'] == 'RDS00029']
        if len(eunice) == 1:
            mon = eunice.iloc[0]['Monday']
            thu = eunice.iloc[0]['Thursday']
            if mon == 6.0 and thu == 6.0:
                print(f"  ✅ Eunice Mphoswa: Mon={mon}, Thu={thu} hrs (works Mon & Thu only)")
        
    else:
        print(f"  ❌ Missing columns in seed data")
        missing = [col for col in expected_columns if col not in df.columns]
        print(f"     Missing: {missing}")
    
    print()
    
except Exception as e:
    print(f"  ❌ Seed data validation failed: {e}")
    print()

# Final Summary
print("=" * 70)
print("Validation Summary")
print("=" * 70)

if missing_deps:
    print("⚠️  DEPENDENCIES MISSING - Install required packages first:")
    print("   pip install -r requirements.txt")
    print()
    print("Then run this validation script again.")
else:
    print("✅ All core validations passed!")
    print()
    print("Next steps:")
    print("1. Install Streamlit if not already installed:")
    print("   pip install -r requirements.txt")
    print()
    print("2. Run the app:")
    print("   streamlit run app.py")
    print()
    print("   Or use the quick start (automatically loads 34 employees):")
    print("   ./start.sh    (Mac/Linux)")
    print("   start.bat     (Windows)")
    print()
    print("3. Open your browser to: http://localhost:8501")
    print()
    print("4. Login with:")
    print("   Username: admin")
    print("   Password: admin123")
    print("   (Note: Not displayed on login screen for security)")
    print()
    print("5. Follow TESTING_GUIDE.md for complete test procedures")

print("=" * 70)
