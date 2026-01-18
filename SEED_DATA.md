# Using Employee Seed Data

This repository includes a seed file (`employee_data_seed.csv`) with pre-populated employee data to help you get started quickly.

## Quick Start with Seed Data

### Option 1: Use Start Scripts (Automatic - Recommended)

The start scripts automatically load the seed data for you:

```bash
# Mac/Linux
./start.sh

# Windows
start.bat
```

**What happens:**
- Script checks if `employee_data.csv` exists
- If not, automatically copies `employee_data_seed.csv` to `employee_data.csv`
- Loads 34 employees automatically
- Starts the app

**Note:** If `employee_data.csv` already exists, it won't overwrite it (preserves your changes)

### Option 2: Manual Copy

1. Copy `employee_data_seed.csv` and rename it to `employee_data.csv`:
   ```bash
   cp employee_data_seed.csv employee_data.csv
   ```

2. Run the app:
   ```bash
   streamlit run app.py
   ```

3. The app will load with all 34 employees already configured!

### Option 2: Start Fresh

If you prefer to start with an empty employee list:

1. Simply run the app without creating `employee_data.csv`
2. The app will create an empty employee database
3. Add employees manually through the UI

## What's in the Seed File?

The seed file contains **34 employees** with their current working hours:

- Employee Number (e.g., RDS00004)
- First Name
- Last Name
- Working hours for Monday through Friday

**Examples:**
- Most employees work 8.5 hours Mon-Thu and 6 hours on Friday
- Veronica du Preez doesn't work Fridays (0 hours)
- Eunice Mphoswa works 6 hours on Monday and Thursday only

## Customizing the Data

After importing the seed data, you can:
- Edit any employee's hours through the app UI
- Add new employees
- Remove employees you don't need

All changes are automatically saved to `employee_data.csv`.

## Important Notes

- `employee_data.csv` is in `.gitignore` and won't be pushed to GitHub
- The seed file is just a starting point
- You can always delete `employee_data.csv` and start over
- On Streamlit Cloud, you'll need to re-add employees after app restarts (unless using external storage)

## File Locations

- `employee_data_seed.csv` - Starting data (34 employees) - **included in repo**
- `employee_data_template.csv` - Empty template showing format - **included in repo**
- `employee_data.csv` - Active data used by app - **created by app, not in repo**
