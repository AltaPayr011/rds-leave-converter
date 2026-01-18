# Deployment Guide

## Option 1: Deploy to Streamlit Cloud (Recommended)

### Step 1: Prepare Your GitHub Repository

1. Create a new repository on GitHub:
   - Go to https://github.com/new
   - Name it `leave-breakdown-app` (or your preferred name)
   - Set it to **Public**
   - Click "Create repository"

2. Upload files to your repository:
   - You can drag and drop these files directly on GitHub:
     - `app.py`
     - `requirements.txt`
     - `README.md`
     - `.gitignore`
     - `employee_data_template.csv`
   - Or use git commands (see below)

### Step 2: Deploy to Streamlit Cloud

1. Go to https://share.streamlit.io

2. Sign in with your GitHub account

3. Click **"New app"**

4. Fill in the deployment form:
   - **Repository**: Select your repository (e.g., `yourusername/leave-breakdown-app`)
   - **Branch**: `main` (or `master`)
   - **Main file path**: `app.py`

5. Click **"Deploy!"**

6. Wait 2-3 minutes for deployment

7. Your app will be live at: `https://yourusername-leave-breakdown-app.streamlit.app`

## Option 2: Using Git Commands

If you prefer using git from command line:

```bash
# Initialize git in your app folder
cd leave_breakdown_app
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: Leave Breakdown Manager"

# Add your GitHub repository as remote
git remote add origin https://github.com/yourusername/leave-breakdown-app.git

# Push to GitHub
git branch -M main
git push -u origin main
```

Then follow Step 2 above to deploy to Streamlit Cloud.

## Important Notes

### Data Persistence
- Employee data is stored in `employee_data.csv`
- User credentials are stored in `users.csv` (bcrypt-encrypted)
- On Streamlit Cloud, these files will reset when the app restarts
- **Important**: Change the default admin password before deploying to production
- For production use, consider using:
  - Streamlit Cloud secrets for initial admin credentials
  - Google Sheets as a backend
  - A database (PostgreSQL, MongoDB, etc.)
  - Environment variables for configuration

### Privacy
- The `.gitignore` file ensures `employee_data.csv` is not pushed to GitHub
- Only the template file is included in the repository

## Updating Your Deployed App

When you push changes to GitHub, Streamlit Cloud will automatically redeploy your app:

```bash
git add .
git commit -m "Description of changes"
git push
```

## Troubleshooting

### App won't deploy
- Check that `requirements.txt` is in the root directory
- Ensure `app.py` is in the root directory
- Verify your repository is public

### Data not persisting
- This is expected on Streamlit Cloud free tier
- Consider upgrading to Streamlit Cloud Pro or using external storage

### Import errors
- Verify all packages are listed in `requirements.txt`
- Check package versions are compatible

## Next Steps

After deployment:
1. Share your app URL with users
2. Add employees through the UI
3. Test with a sample leave transactions file
4. Bookmark the app for easy access

Need help? Open an issue on GitHub!
