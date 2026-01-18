@echo off
echo 🚀 Leave Breakdown Manager - Quick Start
echo ==========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.8 or higher.
    pause
    exit /b 1
)

echo ✅ Python found

REM Install dependencies
echo 📦 Installing dependencies...
pip install -r requirements.txt

REM Automatically load seed data if employee_data.csv doesn't exist
if not exist employee_data.csv (
    if exist employee_data_seed.csv (
        copy employee_data_seed.csv employee_data.csv >nul
        echo ✅ Employee seed data loaded (34 employees ready)
    ) else (
        echo ⚠️  Seed file not found. Starting with empty employee list.
    )
) else (
    echo ✅ Employee data already exists
)

echo.
echo 🎉 Starting the app...
echo 📍 App will open at: http://localhost:8501
echo ⚠️  Press Ctrl+C to stop the app
echo.

REM Run the app
streamlit run app.py
