# 📋 Data Preparation Guide

## Before Uploading Leave Transactions

### ⚠️ CRITICAL: Data Must Be Clean

The RDS PaySpace Leave Converter requires **clean data** to produce accurate calculations. Before uploading your leave transactions file, you **MUST** prepare it properly.

---

## Required Data Cleanup

### ✅ Step 1: Remove Declined Leave

**What to Remove:**
- All leave requests with status: "Declined"
- All leave requests with status: "Rejected"
- All leave requests marked as "Not Approved"

**Why:**
- Declined leave was never actually taken
- Including it will inflate leave calculations
- It will appear in your final report incorrectly

**How to Filter in Excel:**
1. Open your leave transactions file
2. Find the "Status" column (if present)
3. Filter or sort by status
4. Delete all rows with "Declined" or "Rejected"
5. Save the file

### ✅ Step 2: Remove Cancelled Leave

**What to Remove:**
- All leave requests with status: "Cancelled"
- All leave requests with status: "Withdrawn"
- All leave that was approved but later cancelled

**Why:**
- Cancelled leave was approved but not actually taken
- Including it creates incorrect leave balances
- It doesn't represent actual time off

**How to Filter in Excel:**
1. Look for "Status" or "Cancellation" columns
2. Filter to show only cancelled requests
3. Delete these rows
4. Save the file

### ✅ Step 3: Keep Only Approved Leave

**What to Keep:**
- Leave with status: "Approved"
- Leave with status: "Granted"
- Leave with status: "Confirmed"
- Any leave that was actually taken

**Why:**
- This is the only leave that should appear in calculations
- This represents actual time off work
- This is what needs to be converted for OpenTime

---

## Quick Checklist

Before uploading your file, verify:

- [ ] All declined leave removed
- [ ] All cancelled leave removed  
- [ ] All rejected leave removed
- [ ] Only approved/granted leave remains
- [ ] File saved after cleanup
- [ ] No duplicate entries

---

## What the App Will Check

When you upload your file, the app will display:

```
⚠️ IMPORTANT: Data Validation Required

Before processing this file, please ensure you have:
✅ Removed all Declined leave transactions
✅ Removed all Cancelled leave transactions
✅ Verified that only Approved leave transactions remain

Processing declined or cancelled leave will result in incorrect calculations.

☐ I confirm that all declined and cancelled leave transactions 
  have been removed from this file
```

You **must** check this box to proceed with processing.

---

## Common Mistakes

### ❌ Mistake 1: Including All Leave
**Problem:** Uploading the raw export with all statuses
**Solution:** Filter and clean first

### ❌ Mistake 2: Manual Deletion Without Filtering
**Problem:** Scrolling through and deleting rows manually
**Solution:** Use Excel's filter feature to find all at once

### ❌ Mistake 3: Forgetting to Save
**Problem:** Cleaning the data but not saving the file
**Solution:** Save after each cleanup step

### ❌ Mistake 4: Uploading Wrong File
**Problem:** Uploading the original instead of cleaned version
**Solution:** Use clear file naming (e.g., "Leave_Transactions_CLEANED.xlsx")

---

## Excel Filtering Guide

### Method 1: AutoFilter

1. **Select your data range** (including headers)
2. **Click:** Data → Filter (or press Ctrl+Shift+L)
3. **Click** the dropdown arrow in the Status column
4. **Uncheck** "Select All"
5. **Check only:** "Declined", "Cancelled", "Rejected"
6. **Click** OK
7. **Select all visible rows** (except header)
8. **Right-click** → Delete rows
9. **Clear the filter** to see remaining data
10. **Save the file**

### Method 2: Manual Sort

1. **Click** anywhere in your data
2. **Click:** Data → Sort
3. **Sort by:** Status column
4. **Click** OK
5. All declined/cancelled leave will be grouped together
6. **Select and delete** these rows
7. **Save the file**

---

## Example: Before and After

### ❌ BEFORE (Raw Data - DO NOT UPLOAD)
```
Emp. Number | Employee Name | Start Date | End Date | No Days | Status
RDS00001   | John Doe      | 2025-12-22 | 2025-12-26 | 5.0    | Approved
RDS00002   | Jane Smith    | 2025-12-23 | 2025-12-24 | 2.0    | Declined  ← REMOVE
RDS00003   | Bob Jones     | 2025-12-20 | 2025-12-22 | 3.0    | Cancelled ← REMOVE
RDS00004   | Alice Brown   | 2026-01-05 | 2026-01-10 | 4.0    | Approved
```

### ✅ AFTER (Clean Data - READY TO UPLOAD)
```
Emp. Number | Employee Name | Start Date | End Date | No Days | Status
RDS00001   | John Doe      | 2025-12-22 | 2025-12-26 | 5.0    | Approved
RDS00004   | Alice Brown   | 2026-01-05 | 2026-01-10 | 4.0    | Approved
```

---

## Impact of Not Cleaning Data

### If you upload uncleaned data:

**❌ Incorrect Calculations:**
- Declined leave counted as actual leave
- Cancelled leave inflates totals
- Wrong hours calculated

**❌ Misleading Reports:**
- Shows leave that never happened
- Incorrect daily breakdowns
- Wrong OpenTime data

**❌ Processing Errors:**
- May include invalid dates
- Could have negative days (from cancelled leave)
- Confusion for payroll

**❌ Wasted Time:**
- Have to re-process after cleaning
- Manual corrections needed
- Delays in getting accurate reports

---

## Status Column Names

Your file might use different column names for status. Look for:

- "Status"
- "Approval Status"
- "Request Status"
- "Leave Status"
- "State"
- "Workflow State"

The exact name varies by system, but the concept is the same: **remove anything not approved**.

---

## No Status Column?

If your file doesn't have a status column:

**Option 1: Check with HR/Payroll**
- They may have filtered it already
- Ask if the export includes only approved leave

**Option 2: Contact Your System Admin**
- Request an export that includes status
- Or request a pre-filtered approved-only export

**Option 3: Manual Verification**
- Review each entry
- Confirm with leave records that all entries are approved

---

## Best Practices

### ✅ Create a Clean Copy
- Keep original export file as backup
- Work on a copy named "..._CLEANED.xlsx"
- Never delete your raw data

### ✅ Document Your Process
- Note the date you cleaned the data
- Record how many rows were removed
- Keep track of which statuses you filtered

### ✅ Verify Before Upload
- Spot-check a few entries
- Confirm date ranges make sense
- Ensure no obvious errors

### ✅ Save Multiple Times
- Save after removing declined leave
- Save after removing cancelled leave
- Save final clean version

---

## Need Help?

**Can't find status column?**
→ Check with HR or your leave system administrator

**Not sure what counts as "approved"?**
→ Err on the side of caution - only include leave you're certain was taken

**Made a mistake?**
→ Go back to your original file and start over

**File too large to filter?**
→ Use Excel's advanced filter or ask IT for help

---

## Quick Reference Card

Print and keep this handy:

```
┌─────────────────────────────────────────────┐
│  LEAVE DATA PREPARATION CHECKLIST          │
├─────────────────────────────────────────────┤
│                                             │
│  BEFORE UPLOADING TO APP:                  │
│                                             │
│  ☐ Remove all DECLINED leave               │
│  ☐ Remove all CANCELLED leave              │
│  ☐ Remove all REJECTED leave               │
│  ☐ Keep only APPROVED leave                │
│  ☐ Save cleaned file                       │
│  ☐ Verify no duplicates                    │
│                                             │
│  FILE NAMING:                              │
│  Original: Leave_Transactions.xlsx         │
│  Cleaned: Leave_Transactions_CLEANED.xlsx  │
│                                             │
│  REMEMBER:                                 │
│  The app will ask you to confirm cleanup!  │
│                                             │
└─────────────────────────────────────────────┘
```

---

**Last Updated:** January 18, 2026  
**Version:** 2.1  
**For:** RDS PaySpace Leave Converter for OpenTime
