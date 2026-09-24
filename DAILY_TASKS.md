# PrintApex Data Analytics Training Program
## Daily Task Tracker & Guide

**Trainer:** Apex AGI Solutions  
**Program Duration:** 7 Days  
**Last Updated:** September 23, 2026  
**Status:** Active Program

---

## 📌 IMPORTANT: How to Use This Document

This document is updated **daily by the trainer**. Check back each day for your specific tasks.

- **Day 1-7:** All tasks for that day are posted here
- **New tasks appear the day you need to do them**
- Follow the tasks in order
- Complete them before the day ends
- Commit your work to Git

---

## 🎯 Program Overview

**What You're Building:** A production-grade data analytics project using real shop data.

**Your Datasets:**
- `shops_raw_data_10k.csv` (10,000 shops, 3.91 MB)
- `shops_raw_data_25k.csv` (25,000 shops, 9.88 MB)

**Tools:** Python, Jupyter, pandas, SQLite, Git, LibreOffice Calc (all free)

**Final Deliverables:** 8 files (cleaned data, code, documentation, dashboard)

---

# 📅 DAILY TASKS

## ⏭️ DAY 0: SETUP & PREPARATION

**Status:** Complete before Day 1  
**Time Required:** 1 hour  
**Objective:** Get your environment ready

### Phase 0 Tasks

#### Task 0.1: Install Python & Verify
```bash
# Download from: https://www.python.org/downloads/
# Download Python 3.10 or higher
# IMPORTANT: Check "Add Python to PATH" during installation

# After install, verify in terminal:
python --version
# You should see: Python 3.10.x (or higher)
```

**Deliverable:** Confirmation that Python is installed  
**How to verify:** Run `python --version` in terminal

---

#### Task 0.2: Install Required Tools
```bash
# Download Git from: https://git-scm.com
# Download LibreOffice Calc from: https://www.libreoffice.org
# (Or use Excel if you have it)
# Download VS Code (optional): https://code.visualstudio.com
```

**Deliverable:** All tools installed  
**How to verify:** Each application opens without errors

---

#### Task 0.3: Create Project Folder & Initialize Git
```bash
# Open terminal and run:
mkdir PrintShopDataProject
cd PrintShopDataProject

# Initialize Git
git init
git config user.name "Your Name"
git config user.email "your.email@example.com"

# Verify:
git log
# (May show empty, but command should work)
```

**Deliverable:** Git initialized  
**How to verify:** `git log` command works, no errors

---

#### Task 0.4: Set Up Python Virtual Environment
```bash
# In your PrintShopDataProject folder:
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# You should see (venv) at start of terminal line

# Verify:
python --version
```

**Deliverable:** Virtual environment activated  
**How to verify:** You see `(venv)` before your terminal prompt

---

#### Task 0.5: Install Python Libraries
```bash
# With virtual environment activated, run:
pip install pandas jupyter matplotlib seaborn

# Verify installation:
python -c "import pandas; print(pandas.__version__)"
# Should print version number (e.g., 2.1.0)
```

**Deliverable:** All libraries installed  
**How to verify:** Version numbers print without errors

---

#### Task 0.6: Create Project Folder Structure
```bash
# Create folders:
mkdir data\raw data\cleaned data\processed notebooks scripts sql output\charts

# Or on Mac/Linux:
mkdir -p data/raw data/cleaned data/processed notebooks scripts sql output/charts

# Verify:
ls -la data/
# Should show: raw, cleaned, processed folders
```

**Deliverable:** Folder structure created  
**How to verify:** All folders exist and are empty

---

#### Task 0.7: Create .gitignore File
```bash
# Create file: .gitignore
# Add this content:
*.csv
*.xlsx
*.db
venv/
__pycache__/
.ipynb_checkpoints/
```

**Deliverable:** .gitignore created  
**How to verify:** File exists and contains entries

---

#### Task 0.8: First Git Commit
```bash
git add .gitignore
git commit -m "Initial project setup"

# Verify:
git log --oneline
# Should show: "Initial project setup"
```

**Deliverable:** First commit made  
**How to verify:** `git log` shows your commit

---

#### Task 0.9: Test Jupyter Notebook
```bash
# Activate virtual environment (if not already active)
# Windows:
venv\Scripts\activate

# Start Jupyter:
jupyter notebook

# A browser window should open showing http://localhost:8888

# Stop by pressing Ctrl+C in terminal
```

**Deliverable:** Jupyter works  
**How to verify:** Browser opens with Jupyter interface

---

#### Task 0.10: Copy Data Files
**Get files:** Download `shops_raw_data_10k.csv` and `shops_raw_data_25k.csv`

```bash
# Copy files to: PrintShopDataProject/data/raw/
# Verify:
ls data/raw/
# Should show both CSV files
```

**Deliverable:** Both data files in `data/raw/`  
**How to verify:** Files exist and are correct size (3.91 MB + 9.88 MB)

---

### Day 0 Checklist
- [ ] Python installed and working
- [ ] Git, LibreOffice, VS Code installed
- [ ] Project folder created
- [ ] Git initialized
- [ ] Virtual environment created and activated
- [ ] Python libraries installed
- [ ] Folder structure created
- [ ] .gitignore created
- [ ] First Git commit made
- [ ] Jupyter tested
- [ ] Data files copied to `data/raw/`

**Status:** ✅ READY FOR DAY 1

---

---

# 🔶 PHASE 1: DATA PROFILING & ISSUE IDENTIFICATION

## 📅 DAYS 1-2: Profile Your Data

**Status:** Days 1-2 (Mon-Tue)  
**Time Required:** 8-10 hours  
**Objective:** Understand the raw data completely, document all issues

**What You'll Learn:** How to profile large datasets, identify data quality problems, think like a data engineer

---

## DAY 1 MORNING: Get Started with Profiling

### Task 1.1: Create Phase 1 Jupyter Notebook
```bash
# Start Jupyter:
jupyter notebook

# In browser:
# Click "New" → "Python 3"
# Name it: Phase1_Profile.ipynb
# Save to: notebooks/ folder
```

**Deliverable:** `notebooks/Phase1_Profile.ipynb` created  
**Time:** 5 minutes

---

### Task 1.2: Load Data & Get Basic Info
In your Jupyter notebook, create cells with this code:

**Cell 1: Import Libraries**
```python
import pandas as pd
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

print("✅ Libraries imported successfully")
```

**Cell 2: Load Both Datasets**
```python
df_10k = pd.read_csv('../../data/raw/shops_raw_data_10k.csv')
df_25k = pd.read_csv('../../data/raw/shops_raw_data_25k.csv')

print(f"✅ 10k dataset: {df_10k.shape[0]:,} rows × {df_10k.shape[1]} columns")
print(f"✅ 25k dataset: {df_25k.shape[0]:,} rows × {df_25k.shape[1]} columns")
```

**Cell 3: Preview Data**
```python
print("\n" + "="*80)
print("10K DATASET - FIRST 5 ROWS")
print("="*80)
print(df_10k.head())

print("\n" + "="*80)
print("COLUMN NAMES")
print("="*80)
print(df_10k.columns.tolist())
```

**Deliverable:** Code runs, data loads successfully  
**Expected Output:** Shows 10,001 rows × 32 columns and 25,001 rows × 32 columns  
**Time:** 15 minutes

---

### Task 1.3: Get Basic Statistics
Add this cell to your notebook:

```python
print("\n" + "="*80)
print("BASIC STATISTICS - 10K DATASET")
print("="*80)
print(f"Total rows: {df_10k.shape[0]:,}")
print(f"Total columns: {df_10k.shape[1]}")
print(f"Memory usage: {df_10k.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
print(f"Rows with NO missing values: {len(df_10k.dropna())}")
print(f"Exact duplicate rows: {df_10k.duplicated().sum()}")

print("\n" + "-"*80)
print("BASIC STATISTICS - 25K DATASET")
print("-"*80)
print(f"Total rows: {df_25k.shape[0]:,}")
print(f"Total columns: {df_25k.shape[1]}")
print(f"Memory usage: {df_25k.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
print(f"Rows with NO missing values: {len(df_25k.dropna())}")
print(f"Exact duplicate rows: {df_25k.duplicated().sum()}")
```

**Deliverable:** Code runs and shows statistics  
**Expected Output:** Two datasets loaded successfully with stats displayed  
**Time:** 10 minutes

---

### Task 1.4: Analyze Null Values
Add this cell:

```python
def null_summary(df, dataset_name):
    """Generate comprehensive null value report"""
    null_data = {
        'Column': df.columns,
        'Null_Count': df.isnull().sum(),
        'Null_Percent': round((df.isnull().sum() / len(df)) * 100, 2)
    }
    summary_df = pd.DataFrame(null_data).sort_values('Null_Percent', ascending=False)
    
    print(f"\n{dataset_name} - NULL VALUES SUMMARY")
    print(f"Columns with nulls: {(summary_df['Null_Count'] > 0).sum()}")
    print(summary_df.to_string(index=False))
    
    return summary_df

null_10k = null_summary(df_10k, "10K DATASET")
null_25k = null_summary(df_25k, "25K DATASET")
```

**Deliverable:** Null value report generated  
**Expected Output:** Shows which columns have missing values and percentages  
**Time:** 10 minutes

---

### Task 1.5: Check for Duplicates
Add this cell:

```python
print("\n" + "="*80)
print("DUPLICATE ANALYSIS")
print("="*80)

print("\n10K DATASET:")
print(f"  Exact duplicate rows: {df_10k.duplicated().sum()}")
print(f"  Duplicate IDs: {df_10k['id'].duplicated().sum()}")
print(f"  Duplicate slugs: {df_10k['slug'].duplicated().sum()}")

print("\n25K DATASET:")
print(f"  Exact duplicate rows: {df_25k.duplicated().sum()}")
print(f"  Duplicate IDs: {df_25k['id'].duplicated().sum()}")
print(f"  Duplicate slugs: {df_25k['slug'].duplicated().sum()}")

# Show examples if any
if df_10k.duplicated().sum() > 0:
    print("\nExample duplicate rows (10k):")
    print(df_10k[df_10k.duplicated(keep=False)].head(2))
```

**Deliverable:** Duplicate analysis displayed  
**Expected Output:** Shows count of exact duplicates and duplicate IDs  
**Time:** 10 minutes

---

### Task 1.6: Analyze Dates
Add this cell:

```python
print("\n" + "="*80)
print("DATE FIELD ANALYSIS")
print("="*80)

date_cols = ['created_at', 'updated_at', 'approved_at', 'suspended_at', 'expired_at']

for col in date_cols:
    if col in df_10k.columns:
        print(f"\n{col} (10K):")
        print(f"  Non-null: {df_10k[col].notna().sum():,}")
        print(f"  Min: {df_10k[col].min()}")
        print(f"  Max: {df_10k[col].max()}")

# Check for impossible dates (created > updated)
try:
    df_10k['created_dt'] = pd.to_datetime(df_10k['created_at'], errors='coerce')
    df_10k['updated_dt'] = pd.to_datetime(df_10k['updated_at'], errors='coerce')
    
    impossible = (df_10k['created_dt'] > df_10k['updated_dt']).sum()
    print(f"\n10K - Rows where created_at > updated_at: {impossible}")
    
    df_10k.drop(['created_dt', 'updated_dt'], axis=1, inplace=True)
except Exception as e:
    print(f"Error: {e}")
```

**Deliverable:** Date analysis displayed  
**Expected Output:** Shows date ranges and impossible date logic errors  
**Time:** 10 minutes

---

### Task 1.7: Categorical Fields
Add this cell:

```python
print("\n" + "="*80)
print("CATEGORICAL FIELDS - DISTRIBUTION")
print("="*80)

categorical_fields = ['status', 'subscription_plan', 'subscription_status', 'gst_status']

for field in categorical_fields:
    if field in df_10k.columns:
        print(f"\n{field} (10K):")
        print(df_10k[field].value_counts(dropna=False))
```

**Deliverable:** Categorical distribution shown  
**Expected Output:** Shows value counts for status fields  
**Time:** 5 minutes

---

### Task 1.8: Phone Number Analysis
Add this cell:

```python
print("\n" + "="*80)
print("PHONE NUMBER FORMAT ANALYSIS")
print("="*80)

no_phone = df_10k['contact_phone'].isna().sum()
with_plus91 = df_10k['contact_phone'].astype(str).str.contains(r'^\+91', na=False).sum()
with_91_dash = df_10k['contact_phone'].astype(str).str.contains(r'^91-', na=False).sum()
plain_10 = df_10k['contact_phone'].astype(str).str.match(r'^\d{10}$', na=False).sum()

print(f"\n10K Phone format breakdown:")
print(f"  Missing: {no_phone}")
print(f"  Format +91: {with_plus91}")
print(f"  Format 91-: {with_91_dash}")
print(f"  Plain 10 digits: {plain_10}")

print("\nSample phone numbers:")
for phone in df_10k['contact_phone'].dropna().head(10):
    print(f"  {phone}")
```

**Deliverable:** Phone format analysis displayed  
**Expected Output:** Shows phone format variations  
**Time:** 5 minutes

---

### Day 1 Commit
```bash
git add notebooks/Phase1_Profile.ipynb
git commit -m "Day 1: Phase 1 profiling code written and tested"
```

---

## DAY 1 EVENING/DAY 2: Review Findings & Create Issue Log

### Task 1.9: Review All Outputs
**Action:** Run all cells from Task 1.1-1.8 again and take notes of findings.

**Questions to answer:**
- How many null values per column?
- Any duplicate rows or duplicate IDs?
- Any impossible dates?
- Phone format inconsistencies?
- Status distribution?

**Time:** 30 minutes  
**Deliverable:** List of findings noted

---

### Task 1.10: Create Issue Log
**Create file:** `output/issue_log.txt`

**Format:** (Copy the template below and fill in your findings)

```
================================================================================
DATA QUALITY ISSUE LOG
Project: PrintApex Shop Data Analysis
Created: [Today's Date]
Analyzed by: [Your Name]
================================================================================

DATASET: 10K (10,000 rows)
================================================================================

Column Name | Issue Type | Count/Percent | Severity | Notes
------------|------------|---------------|----------|------

contact_phone | MISSING | [X] rows ([Y]%) | MEDIUM | Some shops may use email only
contact_phone | FORMAT_INCONSISTENT | [X] rows ([Y]%) | MEDIUM | Mix of +91, 91-, plain digits
business_name | LEADING_TRAILING_SPACES | [X] rows ([Y]%) | LOW | "  Copy Center  " needs trim
business_name | CASE_INCONSISTENT | [X] rows ([Y]%) | LOW | "print shop" vs "Print Shop"
postal_code | MISSING | [X] rows ([Y]%) | HIGH | Required for validation
postal_code | INVALID_FORMAT | [X] rows ([Y]%) | HIGH | Should be 6 digits
created_at | FUTURE_DATES | [X] rows ([Y]%) | HIGH | A few impossible dates
gst_number | MISSING | [X] rows ([Y]%) | MEDIUM | When gst_status = not_applicable
subscription_status | LOGIC_ERROR | [X] rows ([Y]%) | HIGH | Active status but no plan
printer_make | MISSING | [X] rows ([Y]%) | MEDIUM | Not yet configured by shop
city | [ISSUE] | [X] rows ([Y]%) | [SEV] | [NOTES]
[Continue for other columns...]

================================================================================
DATASET: 25K (25,000 rows)
================================================================================

[Repeat analysis format above for 25k dataset]

================================================================================
SUMMARY
================================================================================

Total issues identified (10k): [X]
Total issues identified (25k): [Y]
Most critical issues: [List top 3]
Next steps: Move to Phase 2 - Handle missing values and duplicates

================================================================================
```

**Instructions:**
1. Fill in the actual numbers from your profiling analysis
2. For each column with nulls/issues, add one row
3. Save as text file

**Deliverable:** `output/issue_log.txt` created  
**Time:** 45 minutes

---

### Task 1.11: Spot-Check Data in LibreOffice Calc
**Action:** 
1. Open `data/raw/shops_raw_data_10k.csv` in LibreOffice Calc
2. Scroll through ~100 rows
3. Verify that issues from your profiling match what you see
4. Note any additional issues

**Deliverable:** Manual verification complete  
**Time:** 30 minutes

---

### Task 1.12: Final Commit for Phase 1
```bash
git add output/issue_log.txt
git commit -m "Day 2: Phase 1 complete - Data profiling and issue log created"

# Verify:
git log --oneline | head -3
# Should show your commits
```

**Deliverable:** Phase 1 complete and committed  
**Time:** 5 minutes

---

### Phase 1 Checklist (Days 1-2)
- [ ] Jupyter notebook created and profiling code working
- [ ] Null values analyzed for both datasets
- [ ] Duplicates identified
- [ ] Date anomalies found
- [ ] Phone format issues documented
- [ ] Issue log created with detailed findings
- [ ] Data spot-checked in LibreOffice Calc
- [ ] All work committed to Git
- [ ] At least 2 Git commits made

**Status:** ✅ PHASE 1 COMPLETE

---

---

## [COMING TOMORROW - Day 3]

### Phase 2: Handle Missing Values & Duplicates (Days 3-4)

Tasks for Days 3-4 will be posted tomorrow. Come back to this document to see your new tasks.

**Preview of what's coming:**
- Remove or fill null values based on business logic
- Handle duplicate rows
- Save cleaned checkpoint data
- Document all decisions
- Create transformation log

---

## [TO BE UPDATED ON DAY 5]

### Phase 3: Standardize & Format (Days 5-6)

Tasks for Days 5-6 will be posted on Day 5.

**Preview of what's coming:**
- Standardize phone numbers (10 digits)
- Standardize names (Title case, trim spaces)
- Standardize dates (ISO format)
- Standardize postal codes (6 digits)
- Convert data types

---

## [TO BE UPDATED ON DAY 7]

### Phase 4: Validation Rules (Days 7-8)

Tasks for Days 7-8 will be posted on Day 7.

**Preview of what's coming:**
- Write business logic validation rules
- Detect outliers and invalid data
- Generate validation report
- Final processed datasets

---

## [TO BE UPDATED ON DAY 9]

### Phase 5: SQL Analysis & Python Insights (Days 9-11)

Tasks for Days 9-11 will be posted on Day 9.

**Preview of what's coming:**
- Write SQL queries
- Load data into SQLite
- Create Python visualizations
- Generate insights

---

## [TO BE UPDATED ON DAY 12]

### Phase 6: Excel Dashboard (Day 12)

Tasks for Day 12 will be posted on Day 12.

**Preview of what's coming:**
- Create Excel dashboard
- Add charts and summaries
- Final deliverables checklist
- Project review

---

---

# 📋 REFERENCE: Program Structure

## All 8 Final Deliverables

By Day 12, you will deliver:

1. **Cleaned 10k Dataset** — `data/processed/shops_10k_final.csv`
2. **Cleaned 25k Dataset** — `data/processed/shops_25k_final.csv`
3. **Issue Log** — `output/issue_log.txt`
4. **Transformation Log** — `output/transformation_log.txt`
5. **Validation Rules** — `output/validation_rules.txt`
6. **Python Analysis Notebook** — `notebooks/Phase5_Analysis.ipynb`
7. **SQL Queries** — `sql/queries.sql`
8. **Excel Dashboard** — `output/dashboard.xlsx`

**Plus:** 6+ Git commits showing daily progress

---

## Tools You're Using

| Tool | Why | Cost |
|------|-----|------|
| Python | Data processing | Free |
| Jupyter | Interactive coding | Free |
| pandas | Data manipulation | Free |
| SQLite | Database queries | Free |
| Git | Version control | Free |
| LibreOffice Calc | Excel alternative | Free |

**Total Program Cost: $0**

---

## What You're Learning

✅ Data profiling (understand raw data)  
✅ Data cleaning (remove/fix bad data)  
✅ Data standardization (make formats consistent)  
✅ Data validation (check for errors)  
✅ SQL analysis (query databases)  
✅ Python analysis (analyze with code)  
✅ Data visualization (create charts)  
✅ Excel dashboards (business reporting)  
✅ Git version control (professional practice)  

**By Day 7, you're interview-ready.**

---

## Daily Time Commitment

- Day 0: 1 hour (setup)
- Day 1-2: 8-10 hours (profiling)
- Day 3-4: 8-10 hours (cleaning)
- Day 5-6: 8-10 hours (standardization)
- Day 7-8: 8-10 hours (validation)
- Day 9-11: 12-15 hours (analysis)
- Day 12: 4-5 hours (dashboard)

**Total: ~50-60 hours across 7 days**

---

## Git Commit Pattern

Each day, make at least one commit:

```bash
# Day 1 example:
git commit -m "Day 1: Phase 1 profiling complete"

# Day 2 example:
git commit -m "Day 2: Issue log created"

# Day 3 example:
git commit -m "Day 3: Phase 2 missing values handled"
```

**By Day 12: You'll have 7+ commits showing your progress**

---

## FAQ

**Q: What if I get stuck?**  
A: Check the code examples in this document, Google the error, or ask a peer.

**Q: Can I skip a day?**  
A: No. Each day builds on the previous one. Make them up if needed.

**Q: How do I know I'm on track?**  
A: Follow the tasks in order, commit daily, check off the checklists.

**Q: What if I finish early?**  
A: Great! Refactor your code, add more charts, write notes explaining your approach.

**Q: Will I really be ready for interviews?**  
A: Yes. You'll have a real project with clean code, documentation, and Git history to show.

---

## Getting Help

1. **Check this document** — Most answers are here
2. **Google your error** — 95% of errors are answered on Stack Overflow
3. **Ask a peer** — Collaboration helps learning
4. **Ask the trainer** — For hints, not answers

**Remember:** The struggle is where the learning happens.

---

---

# 📞 Trainer Notes

**Program Version:** 1.0  
**Updated:** September 23, 2026  
**Next Update:** Tomorrow at 9 AM (Days 3-4 tasks)  

**Interns:** Check back tomorrow for your next tasks.

**Trainer:** Copy/paste the next phase tasks here tomorrow. Update this file daily.

---

**Status: ACTIVE PROGRAM - DAY 1 TASKS LIVE** ✅

