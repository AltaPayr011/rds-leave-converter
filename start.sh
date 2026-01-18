#!/bin/bash

echo "🚀 Leave Breakdown Manager - Quick Start"
echo "=========================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Python 3 found"

# Check if streamlit is installed
if ! python3 -c "import streamlit" &> /dev/null; then
    echo "📦 Installing dependencies..."
    pip3 install -r requirements.txt
else
    echo "✅ Dependencies already installed"
fi

# Automatically load seed data if employee_data.csv doesn't exist
if [ ! -f "employee_data.csv" ]; then
    if [ -f "employee_data_seed.csv" ]; then
        cp employee_data_seed.csv employee_data.csv
        echo "✅ Employee seed data loaded (34 employees ready)"
    else
        echo "⚠️  Seed file not found. Starting with empty employee list."
    fi
else
    echo "✅ Employee data already exists"
fi

echo ""
echo "🎉 Starting the app..."
echo "📍 App will open at: http://localhost:8501"
echo "⚠️  Press Ctrl+C to stop the app"
echo ""

# Run the app
streamlit run app.py
