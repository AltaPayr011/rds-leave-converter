# 🔧 File Upload Troubleshooting Guide

## Common Errors and How to Fix Them

---

## Error 1: "Error processing file: 'Emp. Number'"

### What it means:
The app couldn't find the "Emp. Number" column in your Excel file.

### ✅ Solution:
**You don't need to do anything!** The app now accepts these variations:
- Emp. Number
- Emp Number  
- Employee Number
- EmpNumber
- (and more...)

If you still get this error, check that row 8 of your Excel file has column headers.

---

## Error 2: "sequence item 7: expected str instance, datetime.datetime found"

### What it means:
One of your columns contains dates when it should contain text (or vice versa).

### ✅ Solution:

**Check these columns in your Excel file:**

1. **Emp. Number** - Should be TEXT or NUMBERS, not dates
   ```
   ❌ Wrong: 01/15/2024
   ✅ Right: RDS00001
   ```

2. **Start Date** - Should be DATES
   ```
   ❌ Wrong: "January 15, 2024" (as text)
   ✅ Right: 15/01/2024 (as date)
   ```

3. **End Date** - Should be DATES
   ```
   ❌ Wrong: "01-15-2024" (as text)
   ✅ Right: 15/01/2024 (as date)
   ```

4. **No Days** - Should be NUMBERS
   ```
   ❌ Wrong: "1 day" (as text)
   ✅ Right: 1 (as number)
   ```

### How to check in Excel:

1. Open your file
2. Click on a cell in "Start Date" column
3. Look at the format (Home → Number section)
4. It should say "Date" not "General" or "Text"

### How to fix:

1. Select the date column (Start Date or End Date)
2. Right-click → Format Cells
3. Choose "Date"
4. Click OK
5. Save the file
6. Upload again

---

## Error 3: "Missing required columns: [column names]"

### What it means:
Your Excel file is missing one or more required columns.

### ✅ Solution:

**Required columns (row 8):**
- Emp. Number (or variations)
- Employee Name
- Initials
- Leave Description
- Leave Type Description
- Start Date
- End Date
- No Days

**Check:**
1. Open your Excel file
2. Look at row 8
3. Make sure ALL these columns exist
4. Column names can have slight variations (see Error 1)

---

## Error 4: File format doesn't match

### What it means:
The structure of your Excel file is different than expected.

### ✅ Solution:

**The app expects:**
- Headers on **row 8** (not row 1)
- Data starts on row 9
- Specific column names (with variations accepted)

**To fix:**
1. Compare your file to the example `Leave_Transactions_648648.xlsx`
2. Make sure headers are on row 8
3. Make sure the columns match

---

## Error 5: "Group : All Groups" appears in data

### What it means:
The file contains grouping rows that need to be filtered out.

### ✅ Solution:
The app automatically filters these out! If you see this error, it means the filtering didn't work.

**Manual fix:**
1. Open Excel
2. Find rows with "Group : All Groups" in Emp. Number column
3. Delete these rows
4. Save and upload again

---

## Error 6: Declined or Cancelled leave included

### What it means:
You uploaded a file with declined or cancelled leave transactions.

### ✅ Solution:

**Before uploading:**
1. Open your Excel file
2. Find the "Status" column (if it exists)
3. Filter or delete rows where Status = "Declined" or "Cancelled"
4. Keep only "Approved" leave
5. Save and upload

**See DATA_PREPARATION.md for detailed instructions**

---

## Quick Diagnostic Steps

### Step 1: Check Row 8
```
Open Excel → Go to Row 8 → Should see column headers
```

### Step 2: Check Date Columns
```
Click Start Date cell → Home tab → Should show "Date" format
```

### Step 3: Check Employee Number
```
Click Emp. Number cell → Should NOT be a date → Should be text/number
```

### Step 4: Check No Days
```
Click No Days cell → Should be a number → Not text
```

### Step 5: Check for Blank Rows
```
Scroll through data → Delete any completely blank rows
```

---

## Still Having Issues?

### Try This Checklist:

- [ ] Headers are on row 8
- [ ] Column names match required columns (variations OK)
- [ ] Start Date and End Date are formatted as dates
- [ ] Emp. Number is NOT formatted as a date
- [ ] No Days contains only numbers
- [ ] No completely blank rows
- [ ] Declined/Cancelled leave removed
- [ ] No "Group : All Groups" rows
- [ ] File is saved as .xlsx

---

## Common Excel Issues

### Issue: Excel auto-converts employee numbers to dates

**Example:** "1015" becomes "10/15/2000"

**Fix:**
1. Select Emp. Number column (before entering data)
2. Format → Text
3. Enter employee numbers
4. They'll stay as text

### Issue: Dates show as numbers

**Example:** Start Date shows "44942" instead of "2024-01-15"

**Fix:**
1. Select date column
2. Format → Date
3. Choose your preferred date format

### Issue: "No Days" adds decimal places

**Example:** "1" becomes "1.000000"

**Fix:**
1. Select No Days column
2. Format → Number
3. Set decimal places to 1 or 2

---

## Testing Your File

Before uploading to the app, do this quick test:

1. **Open Excel file**
2. **Go to row 8** - See all column headers?
3. **Click Start Date** - Formatted as date?
4. **Click Emp. Number** - Text/number, not date?
5. **Click No Days** - Number format?
6. **Scan for blank rows** - None?
7. **Check for "Group"** - No grouping rows?

If all checks pass → Upload should work! ✅

---

## Error Message Reference

| Error Contains | Likely Cause | Quick Fix |
|----------------|--------------|-----------|
| "Emp. Number" | Column not found | Check row 8 has headers |
| "datetime" | Wrong data type | Check date formatting |
| "sequence" | Mixed data types | Check column formats |
| "Missing required" | Column missing | Add missing columns |
| "Group" | Grouping rows | Remove grouping rows |

---

## Get Help

If none of these solutions work:

1. **Check the error message** - It now provides specific guidance
2. **Review DATA_PREPARATION.md** - Complete data cleaning guide
3. **Compare with example file** - Match the structure
4. **Check CHANGELOG.md** - Recent fixes may address your issue

---

**Version:** 2.7  
**Last Updated:** January 18, 2026  
**Status:** All common errors have solutions! 🎯
