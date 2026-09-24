# PrintApex Data Analytics Training Program
## 7-Day Intensive: SQL + Python + Excel

**Status:** Ready for interns  
**Duration:** 7 days (Mon-Sun)  
**Cost:** $0 (100% free tools)  
**Outcome:** Production-ready data analyst capable of acing entry-level interviews

---

## What You're Building

You have two datasets:
- **shops_raw_data_10k.csv** (10,000 shops, 3.91 MB)
- **shops_raw_data_25k.csv** (25,000 shops, 9.88 MB)

Both are **real production exports** from our database—with intentional data quality issues interns must discover and fix. By Day 7, you'll have a complete ETL pipeline + analysis + Excel dashboard that proves you can handle real data engineering work.

---

## The Tools (All Free)

| Tool | Download | Why You Need It |
|------|----------|-----------------|
| **Python 3.10+** | https://www.python.org/downloads/ | Core language for data processing |
| **Jupyter Notebook** | `pip install jupyter` | Interactive development & documentation |
| **pandas** | `pip install pandas` | Data manipulation library (THE tool for analytics) |
| **SQLite** | Built into Python | Query your data like a real database |
| **VS Code** | https://code.visualstudio.com | Code editor (optional but recommended) |
| **LibreOffice Calc** | https://www.libreoffice.org | Excel alternative (or use Excel if you have it) |
| **Git** | https://git-scm.com | Version control + portfolio proof |

**Total install time:** ~30 minutes

---

## Phase Breakdown (Your 7-Day Sprint)

| Phase | Days | Goal | Deliverable |
|-------|------|------|-------------|
| **1: Profile** | 1-2 | Understand the raw data—what's broken? | `issue_log.txt` |
| **2: Missing & Dups** | 3-4 | Handle nulls and duplicate rows | Cleaned CSVs |
| **3: Standardize** | 5-6 | Fix format inconsistencies (phones, dates, etc.) | Standardized CSVs |
| **4: Validate** | 7-8 | Write validation rules, detect outliers | Validation report |
| **5: Analyze & Query** | 9-11 | Write SQL, Python analysis, create charts | SQL queries + Python notebook |
| **6: Dashboard** | 12 | Build Excel dashboard, final deliverables | `dashboard.xlsx` + all code |

---

## Before You Start

### Step 1: Download & Install (30 min)

```bash
# Check if Python is installed
python --version

# If not, download Python 3.10+ from https://www.python.org/downloads/
# During install: CHECK "Add Python to PATH"
```

### Step 2: Set Up Your Project Folder (15 min)

```bash
# Open terminal/command prompt and run:
mkdir PrintShopDataProject
cd PrintShopDataProject
git init

# Copy the raw data files here
# (You'll receive shops_raw_data_10k.csv and shops_raw_data_25k.csv)
```

### Step 3: Create Virtual Environment (10 min)

```bash
# Create isolated Python environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate

# You should see (venv) at the start of your terminal now
```

### Step 4: Install Libraries (5 min)

```bash
pip install pandas jupyter matplotlib seaborn

# Verify
python -c "import pandas; print(pandas.__version__)"
```

### Step 5: Start Jupyter (1 min)

```bash
jupyter notebook

# Opens http://localhost:8888 in your browser
# Create a new Python 3 notebook called "Phase1_Profile.ipynb"
```

---

## Phase 1: Profile & Log Issues (Days 1-2)

### What You'll Do

Load both raw datasets. Don't clean them yet—just understand what's there:
- How many nulls? Where?
- Duplicate rows? Duplicate IDs?
- Date anomalies? Future dates?
- Phone format inconsistencies?
- City/state mismatches?

### Your Deliverable

**File:** `output/issue_log.txt`

```
================================================================================
ISSUE LOG - 10K DATASET
================================================================================

contact_phone | MISSING | 2% (200 rows) | MEDIUM | Some shops accept email only
contact_phone | FORMAT_INCONSISTENT | 15% | MEDIUM | Mix of +91, 91-, plain digits
business_name | LEADING_TRAILING_SPACES | 5% | LOW | "  Copy Center  " needs trim
postal_code | INVALID_FORMAT | 1% | HIGH | Some are 5 or 7 digits, not 6
gst_number | MISSING | 3% | MEDIUM | Null when gst_status = 'not_applicable'
created_at | FUTURE_DATES | 0.5% | HIGH | A few rows have impossible dates
subscription_status | LOGIC_ERROR | 2% | HIGH | Status='active' but plan=null

[Continue for all fields...]
================================================================================
```

### Python Code Structure

**In Jupyter, create cells for:**

1. **Import libraries** → Load CSVs with pandas
2. **Basic stats** → `df.info()`, `df.describe()`, row/column counts
3. **Null analysis** → Count and % nulls per column
4. **Duplicates** → Check for exact duplicates + duplicate IDs
5. **Date validation** → Check date ranges, impossible dates
6. **Categorical analysis** → Status distribution, subscription plans
7. **Spot checks** → Open the CSV in LibreOffice Calc, manually verify 100 rows

### First Git Commit

```bash
git add -A
git commit -m "Phase 1 complete: Data profiling and issue identification"
```

**By end of Day 2, you should have:**
- ✅ `Phase1_Profile.ipynb` with full analysis code
- ✅ `output/issue_log.txt` documenting every anomaly
- ✅ Both raw CSVs loaded and analyzed
- ✅ Spot-check verification in LibreOffice

---

## Phase 2: Handle Missing & Duplicates (Days 3-4)

### What You'll Do

For every issue you logged, make a decision:

- **Null contact_phone?** → Keep it (some shops use email only)
- **Null postal_code?** → Remove the row (required for validation)
- **Duplicate rows?** → Remove duplicates, keep first occurrence
- **Duplicate IDs?** → Investigate—should never happen

### Your Deliverable

**File:** `output/transformation_log.txt`

```
================================================================================
TRANSFORMATION LOG
================================================================================

DATASET: 10K
Start: 10,000 rows

Action 1: Removed rows with missing postal_code
  - Count: 300 rows removed
  - Reason: Postal code required for city/state validation
  - After: 9,700 rows

Action 2: Filled missing printer_make with 'Not_Set'
  - Count: 1,455 rows affected
  - Reason: Indicates printer not yet configured by shop

Action 3: Removed exact duplicate rows
  - Count: 15 rows removed
  - Method: Kept first, removed subsequent

FINAL: 9,385 rows from original 10,000 (6.15% removed)
```

### Second Git Commit

```bash
git commit -m "Phase 2: Missing values and duplicates handled"
```

---

## Phase 3: Standardize & Convert (Days 5-6)

### What You'll Do

Make all data consistent:

- **Phones:** Standardize to 10 digits (remove +91, 91, spaces, dashes)
- **Names:** Title Case, trim leading/trailing spaces
- **Postal codes:** Validate exactly 6 digits
- **Dates:** Convert to ISO format (YYYY-MM-DD HH:MM:SS)
- **GST numbers:** Validate 15 characters
- **Data types:** Convert text categories to efficient types

### Python Code: Example (Phone Standardization)

```python
import re
import pandas as pd

def standardize_phone(phone):
    """Standardize to 10 digits: 9876543210"""
    if pd.isna(phone):
        return None
    
    phone = str(phone).strip()
    phone_clean = re.sub(r'^(\+91|91)[-\s]?', '', phone)  # Remove +91, 91, spaces
    phone_clean = re.sub(r'\D', '', phone_clean)  # Remove all non-digits
    
    if len(phone_clean) == 10 and phone_clean.isdigit():
        return phone_clean
    else:
        return None  # Invalid → null

# Apply to your data
df['contact_phone'] = df['contact_phone'].apply(standardize_phone)
```

### Third Git Commit

```bash
git commit -m "Phase 3: Data standardization and format validation"
```

---

## Phase 4: Validation Rules (Days 7-8)

### What You'll Do

Write business logic rules to catch errors:

```python
# Rule 1: created_at must be before updated_at
fails_1 = df[df['created_at'] > df['updated_at']]

# Rule 2: Active shops must have a subscription plan
fails_2 = df[(df['status'] == 'active') & (df['subscription_plan'].isna())]

# Rule 3: approved_at should be after created_at
fails_3 = df[(df['approved_at'].notna()) & (df['approved_at'] < df['created_at'])]
```

### Fourth Git Commit

```bash
git commit -m "Phase 4: Validation rules and outlier detection"
```

---

## Phase 5: SQL Analysis + Python Insights (Days 9-11)

### What You'll Do

Write SQL queries to answer business questions:

```sql
-- Query 1: Shops by State
SELECT state, COUNT(*) as count,
       SUM(CASE WHEN status='active' THEN 1 ELSE 0 END) as active
FROM shops
GROUP BY state
ORDER BY count DESC;

-- Query 2: Printer Distribution
SELECT printer_make, COUNT(*) as count
FROM shops
WHERE printer_make IS NOT NULL
GROUP BY printer_make
ORDER BY count DESC;

-- Query 3: Subscription Plans (Active Shops)
SELECT subscription_plan, COUNT(*) as count
FROM shops
WHERE status='active'
GROUP BY subscription_plan;

-- Query 4: UPI Configuration
SELECT COUNT(CASE WHEN payout_upi_id IS NOT NULL THEN 1 END) as configured,
       COUNT(CASE WHEN payout_upi_id IS NULL THEN 1 END) as not_configured
FROM shops;

-- Query 5: GST Registration Status
SELECT gst_status, COUNT(*) as count,
       ROUND(100.0*COUNT()/(SELECT COUNT(*) FROM shops),2) as percent
FROM shops
GROUP BY gst_status;
```

### Create Charts in Python

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Chart 1: Shops by State (Top 10)
top_states = df['state'].value_counts().head(10)
plt.figure(figsize=(12, 6))
top_states.plot(kind='bar')
plt.title('Top 10 States by Shop Count')
plt.xlabel('State')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('output/chart_states.png', dpi=300)

# Chart 2: Subscription Plans
sub_plans = df[df['status']=='active']['subscription_plan'].value_counts()
plt.figure(figsize=(8, 6))
sub_plans.plot(kind='pie', autopct='%1.1f%%')
plt.title('Subscription Plans (Active Shops)')
plt.ylabel('')
plt.tight_layout()
plt.savefig('output/chart_subscription_plans.png', dpi=300)
```

### Fifth Git Commit

```bash
git commit -m "Phase 5: SQL queries and Python analysis"
```

---

## Phase 6: Build Excel Dashboard (Day 12)

### What You'll Do

Open LibreOffice Calc and create `output/dashboard.xlsx` with:

**Tab 1: Summary**
- Total shops: 9,385
- Active shops: X
- Inactive shops: Y
- Shops with printer: Z

**Tab 2: State Distribution** (with a chart)
**Tab 3: Subscription Analysis** (with a pie chart)
**Tab 4: Validation Summary** (issues found & fixed)

### Export from Python

```python
# Load your analysis results
state_summary = df['state'].value_counts().reset_index()
state_summary.columns = ['State', 'Count']

# Write to Excel
writer = pd.ExcelWriter('output/dashboard.xlsx', engine='openpyxl')
state_summary.to_excel(writer, sheet_name='State Distribution', index=False)
writer.save()
```

### Sixth Git Commit

```bash
git commit -m "Final deliverables: Excel dashboard and all analysis complete"
```

---

## Final Deliverables Checklist

By end of Day 12, you must have:

- ✅ **Cleaned Datasets** (2 files)
  - `data/processed/shops_10k_final.csv`
  - `data/processed/shops_25k_final.csv`

- ✅ **Documentation** (3 files)
  - `output/issue_log.txt`
  - `output/transformation_log.txt`
  - `output/validation_rules.txt`

- ✅ **Code** (3 files)
  - `notebooks/Phase1_Profile.ipynb`
  - `notebooks/Phase5_Analysis.ipynb`
  - `scripts/cleaning.py` (reproducible pipeline)

- ✅ **Analysis** (2 files)
  - `sql/queries.sql`
  - `output/dashboard.xlsx`

- ✅ **Version Control** (Git commits)
  - One commit per phase
  - Push to GitHub (if you have one)

---

## Interview Talking Points

After completing this project, you can confidently say:

> "I profiled 25,000 production shop records using pandas, identified and documented 15+ data quality issues, standardized phone numbers and dates using regex, wrote 5 SQL queries to answer business questions, created validation rules, and delivered an Excel dashboard—all in one week. Here's my GitHub repo."

Then show them your code. They'll hire you.

---

## Common Issues & Fixes

**Issue:** `ModuleNotFoundError: No module named 'pandas'`
**Fix:** Run `pip install pandas` (with `venv` activated)

**Issue:** Jupyter notebook won't start
**Fix:** Run `pip install jupyter` then `jupyter notebook`

**Issue:** CSV won't open in Jupyter
**Fix:** Ensure the file is in the same directory or provide full path: `pd.read_csv('c:/Users/ABDUL/Documents/Printing Automation/shops_raw_data_10k.csv')`

**Issue:** Git commands not recognized
**Fix:** Download Git from https://git-scm.com/download and restart terminal

---

## Resources

- **pandas documentation:** https://pandas.pydata.org/docs/
- **SQLite tutorial:** https://www.sqlitetutorial.net/
- **Jupyter cheatsheet:** https://www.cheatsheetworld.com/jupyter/
- **Git beginner guide:** https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F

---

## Questions?

This is a self-guided project. You will struggle. That's intentional. When stuck:

1. **Google the error message** (95% of errors are already answered on Stack Overflow)
2. **Check pandas documentation** (https://pandas.pydata.org)
3. **Review the Phase outline** (re-read the goals and code examples)
4. **Ask another intern** (collaboration is part of learning)

Do not ask for answers to Phase problems. Ask for hints, not solutions. The struggle is where learning happens.

---

## Your Success Criteria

**Day 2:** You understand the data problems. Your issue_log.txt shows you discovered real issues.

**Day 4:** You've removed/filled nulls and removed duplicates. Transformation log shows your decisions.

**Day 6:** All data is standardized. Phones are 10 digits. Dates are ISO format.

**Day 8:** Validation rules written and documented.

**Day 11:** SQL queries run successfully. Charts generated. Analysis documented.

**Day 12:** Excel dashboard created. All code committed to Git. You can explain every step.

---

**Now go. Start Phase 1 tomorrow morning. You've got this.**

---

*Generated: 2026-09-23*  
*Training Program v1.0*  
*Apex AGI Solutions*
