# INTERN QUICK START CHECKLIST
## PrintApex Data Analytics Training — 7 Days

**Start Date:** ___________  
**Your Name:** ___________  
**GitHub Repo (optional):** ___________

---

## DAY 0: SETUP (Before You Start)

### Saturday Evening (30 minutes)

- [ ] Download Python 3.10+ from https://www.python.org/downloads/
  - [ ] During install: **CHECK "Add Python to PATH"**
  - [ ] Verify: Open terminal, run `python --version`

- [ ] Download VS Code (optional) from https://code.visualstudio.com

- [ ] Download Git from https://git-scm.com

- [ ] Download LibreOffice Calc from https://www.libreoffice.org
  - [ ] OR use Excel if you have it

### Verify Your Tools

```bash
# In terminal, run these commands:
python --version        # Should show 3.10+
git --version          # Should show version
```

---

## DAY 0: PROJECT FOLDER SETUP (30 minutes)

- [ ] Create folder: `PrintShopDataProject` in your Documents
- [ ] Open terminal in that folder
- [ ] Initialize Git:
  ```bash
  git init
  git config user.name "Your Name"
  git config user.email "your.email@example.com"
  ```

- [ ] Create virtual environment:
  ```bash
  python -m venv venv
  
  # Activate it (Windows):
  venv\Scripts\activate
  
  # Activate it (Mac/Linux):
  source venv/bin/activate
  ```

- [ ] Install Python libraries:
  ```bash
  pip install pandas jupyter matplotlib seaborn
  ```

- [ ] Verify installation:
  ```bash
  python -c "import pandas; print(pandas.__version__)"
  ```

- [ ] Create folder structure:
  ```bash
  mkdir data\raw data\cleaned data\processed notebooks scripts sql output\charts
  
  # OR on Mac/Linux:
  mkdir -p data/raw data/cleaned data/processed notebooks scripts sql output/charts
  ```

- [ ] Create `.gitignore` file with this content:
  ```
  *.csv
  *.xlsx
  *.db
  venv/
  __pycache__/
  .ipynb_checkpoints/
  ```

- [ ] First Git commit:
  ```bash
  git add .gitignore
  git commit -m "Initial project setup"
  ```

### Verify Your Setup

- [ ] Jupyter works: `jupyter notebook` (opens browser, then Ctrl+C to stop)
- [ ] Git works: `git log` (shows your first commit)
- [ ] Virtual env activated (you see `(venv)` in terminal)

---

## DAY 0 EVENING: COPY DATA FILES

- [ ] Copy `shops_raw_data_10k.csv` to `data/raw/`
- [ ] Copy `shops_raw_data_25k.csv` to `data/raw/`
- [ ] Verify files exist:
  ```bash
  ls data/raw/
  ```

**You're ready for Day 1.**

---

# PHASE 1: PROFILE & LOG ISSUES (Days 1-2)

## DAY 1 MORNING (3-4 hours)

### 1. Start Jupyter Notebook

```bash
jupyter notebook
```

This opens http://localhost:8888 in your browser.

### 2. Create New Notebook

- [ ] Click "New" → "Python 3"
- [ ] Name it `Phase1_Profile.ipynb`
- [ ] It opens in a new tab

### 3. Copy Phase 1 Template Code

The trainer gave you `Phase1_Profile_Template.py`.

- [ ] Open it in VS Code or Notepad
- [ ] Copy each "Cell" section
- [ ] Paste into Jupyter cells (one section per cell)
- [ ] Run each cell (Shift+Enter)

### 4. Review All Outputs

You should see:
- [ ] Dataset shapes (10,001 rows, 25,001 rows)
- [ ] Null value summary (which columns have missing data)
- [ ] Duplicate counts
- [ ] Date anomalies
- [ ] Phone format variations
- [ ] Business name inconsistencies
- [ ] Postal code issues
- [ ] GST mismatch examples

### 5. Save Your Notebook

- [ ] Ctrl+S in Jupyter
- [ ] In terminal:
  ```bash
  git add notebooks/Phase1_Profile.ipynb
  git commit -m "Phase 1: Initial data profiling"
  ```

---

## DAY 2 MORNING (4-5 hours)

### 1. Review Phase 1 Outputs

- [ ] Re-run all Phase 1 cells
- [ ] Copy all findings into a text editor

### 2. Create Issue Log

**File:** `output/issue_log.txt`

Write one issue per line. Format:

```
COLUMN_NAME | ISSUE_TYPE | COUNT/PERCENT | SEVERITY | NOTES

contact_phone | MISSING | 200 rows (2%) | MEDIUM | Some shops use email only
contact_phone | FORMAT_INCONSISTENT | 1500 rows (15%) | MEDIUM | +91 vs 91- vs plain digits
business_name | LEADING_TRAILING_SPACES | 500 rows (5%) | LOW | "  Copy Center  " needs trim
postal_code | INVALID_FORMAT | 100 rows (1%) | HIGH | Should be 6 digits, some are 5-7
postal_code | MISSING | 300 rows (3%) | HIGH | Required field, can't validate city
created_at | FUTURE_DATES | 50 rows (0.5%) | HIGH | A few shops have impossible dates
subscription_status | LOGIC_ERROR | 200 rows (2%) | HIGH | Active shops with null plan
gst_number | MISMATCH | 300 rows (3%) | MEDIUM | Registered status but no number
```

### 3. Review 100 Rows Manually

- [ ] Open `data/raw/shops_raw_data_10k.csv` in LibreOffice Calc
- [ ] Scroll through and spot-check 100 random rows
- [ ] Verify Python findings match manual observation
- [ ] Look for issues Python might have missed

### 4. Final Git Commit for Phase 1

```bash
git add output/issue_log.txt
git commit -m "Phase 1 complete: Issue log documented"
```

### ✅ PHASE 1 DONE

You should have:
- [ ] `notebooks/Phase1_Profile.ipynb` (working code)
- [ ] `output/issue_log.txt` (all issues documented)
- [ ] Git commits tracking your work
- [ ] Understanding of every data quality issue

**Time spent so far:** ~8-9 hours  
**Remaining:** ~38-39 hours

---

# PHASE 2: MISSING & DUPLICATES (Days 3-4)

## DAY 3 (4-5 hours)

### 1. Create Phase 2 Notebook

- [ ] In Jupyter: New → Python 3 → Name it `Phase2_Missing_Duplicates.ipynb`

### 2. Load Data

```python
import pandas as pd

df_10k = pd.read_csv('../data/raw/shops_raw_data_10k.csv')
df_25k = pd.read_csv('../data/raw/shops_raw_data_25k.csv')

print(f"10k: {len(df_10k)} rows")
print(f"25k: {len(df_25k)} rows")
```

### 3. For Each Issue in Your Log, Make a Decision

**Example: contact_phone is 2% null**

```python
# Decision: KEEP nulls (some shops use email only)
# Action: None
decision_log = [{
    'field': 'contact_phone',
    'issue': 'MISSING',
    'count': df_10k['contact_phone'].isna().sum(),
    'decision': 'KEEP',
    'reason': 'Business logic: email-only shops'
}]
```

**Example: postal_code is 3% null**

```python
# Decision: REMOVE rows (required field)
rows_before = len(df_10k)
df_10k = df_10k.dropna(subset=['postal_code'])
rows_removed = rows_before - len(df_10k)

decision_log.append({
    'field': 'postal_code',
    'issue': 'MISSING',
    'count': rows_removed,
    'decision': 'REMOVE_ROWS',
    'reason': 'Required for validation'
})
```

**Example: printer_make is 15% null**

```python
# Decision: FILL with 'Not_Set' (not configured yet)
df_10k['printer_make'] = df_10k['printer_make'].fillna('Not_Set')

decision_log.append({
    'field': 'printer_make',
    'issue': 'MISSING',
    'count': (df_10k['printer_make'] == 'Not_Set').sum(),
    'decision': 'FILL',
    'reason': 'Printer not yet configured by shop'
})
```

### 4. Handle Duplicates

```python
# Remove exact duplicate rows
df_10k = df_10k.drop_duplicates(keep='first')

decision_log.append({
    'field': 'ALL',
    'issue': 'DUPLICATE_ROWS',
    'count': <number removed>,
    'decision': 'REMOVE',
    'reason': 'Kept first, removed subsequent'
})
```

### 5. Save Checkpoint Data

```python
df_10k.to_csv('../data/cleaned/shops_10k_after_missing_handling.csv', index=False)
df_25k.to_csv('../data/cleaned/shops_25k_after_missing_handling.csv', index=False)

print(f"Saved: 10k has {len(df_10k)} rows (from 10,000)")
print(f"Saved: 25k has {len(df_25k)} rows (from 25,000)")
```

### 6. Save Decisions to CSV

```python
import pandas as pd

decisions_df = pd.DataFrame(decision_log)
decisions_df.to_csv('../output/decisions_made.csv', index=False)
```

### 7. Git Commit

```bash
git add notebooks/Phase2_Missing_Duplicates.ipynb output/decisions_made.csv
git commit -m "Phase 2: Missing values and duplicates handled"
```

---

## DAY 4 (4-5 hours)

### 1. Create Transformation Log

**File:** `output/transformation_log.txt`

Document every change you made:

```
================================================================================
TRANSFORMATION LOG - PHASE 2
================================================================================

DATASET: 10K
Start: 10,000 rows

Action 1: Removed rows with missing postal_code
  - Count: 300 rows removed
  - Reason: Required for validation
  - After: 9,700 rows

Action 2: Filled missing printer_make with 'Not_Set'
  - Count: 1,455 affected
  - Value: 'Not_Set'
  - Reason: Not yet configured

Action 3: Removed exact duplicate rows
  - Count: 15 removed
  - Method: Kept first occurrence
  - After: 9,685 rows

FINAL: 9,385 rows (from 10,000 original)
Removed: 615 rows total (6.15%)

================================================================================
DATASET: 25K
[Repeat same format...]
```

### 2. Review & Verify

- [ ] Check row counts match your transformation log
- [ ] Open cleaned CSV in LibreOffice Calc
- [ ] Spot-check 50 rows for quality
- [ ] Verify no data corruption

### 3. Git Commit

```bash
git add output/transformation_log.txt
git commit -m "Phase 2 complete: Transformation log documented"
```

### ✅ PHASE 2 DONE

You should have:
- [ ] `Phase2_Missing_Duplicates.ipynb` (working code)
- [ ] `output/decisions_made.csv` (decisions tracked)
- [ ] `output/transformation_log.txt` (all changes documented)
- [ ] Cleaned checkpoint data saved

**Time spent:** ~16-18 hours  
**Remaining:** ~32-34 hours

---

# PHASE 3: STANDARDIZE & FORMAT (Days 5-6)

## DAY 5 (4-5 hours)

### 1. Create Phase 3 Notebook

- [ ] New → Python 3 → `Phase3_Standardize.ipynb`

### 2. Load Phase 2 Output

```python
import pandas as pd
import re

df_10k = pd.read_csv('../data/cleaned/shops_10k_after_missing_handling.csv')
df_25k = pd.read_csv('../data/cleaned/shops_25k_after_missing_handling.csv')
```

### 3. Standardize Phone Numbers

```python
def standardize_phone(phone):
    """Convert to 10 digits: 9876543210"""
    if pd.isna(phone) or phone == '':
        return None
    
    phone = str(phone).strip()
    # Remove +91, 91, spaces, dashes
    phone_clean = re.sub(r'^(\+91|91)[-\s]?', '', phone)
    phone_clean = re.sub(r'\D', '', phone_clean)
    
    if len(phone_clean) == 10 and phone_clean.isdigit():
        return phone_clean
    else:
        return None

df_10k['contact_phone'] = df_10k['contact_phone'].apply(standardize_phone)
df_25k['contact_phone'] = df_25k['contact_phone'].apply(standardize_phone)

print(f"Phones standardized: {df_10k['contact_phone'].notna().sum()} valid")
```

### 4. Standardize Business Names

```python
def standardize_name(name):
    """Title case, trim spaces"""
    if pd.isna(name):
        return None
    return str(name).strip().title()

df_10k['business_name'] = df_10k['business_name'].apply(standardize_name)
df_25k['business_name'] = df_25k['business_name'].apply(standardize_name)
```

### 5. Standardize Postal Codes

```python
def standardize_postal(code):
    """Must be exactly 6 digits"""
    if pd.isna(code):
        return None
    
    code_clean = str(code).strip()
    if len(code_clean) == 6 and code_clean.isdigit():
        return code_clean
    else:
        return None

df_10k['postal_code'] = df_10k['postal_code'].apply(standardize_postal)
df_25k['postal_code'] = df_25k['postal_code'].apply(standardize_postal)
```

### 6. Standardize Dates

```python
def standardize_date(date_str):
    """ISO format: YYYY-MM-DD HH:MM:SS"""
    if pd.isna(date_str):
        return None
    try:
        dt = pd.to_datetime(date_str)
        return dt.strftime('%Y-%m-%d %H:%M:%S')
    except:
        return None

date_columns = ['created_at', 'updated_at', 'approved_at', 'suspended_at', 'expired_at']
for col in date_columns:
    if col in df_10k.columns:
        df_10k[col] = df_10k[col].apply(standardize_date)
        df_25k[col] = df_25k[col].apply(standardize_date)
```

### 7. Standardize GST Numbers

```python
def standardize_gst(gst):
    """Must be exactly 15 characters"""
    if pd.isna(gst) or gst == 'N/A':
        return gst
    
    gst_clean = str(gst).strip().upper()
    if len(gst_clean) == 15:
        return gst_clean
    else:
        return None

df_10k['gst_number'] = df_10k['gst_number'].apply(standardize_gst)
df_25k['gst_number'] = df_25k['gst_number'].apply(standardize_gst)
```

### 8. Standardize UPI IDs

```python
def standardize_upi(upi):
    """Lowercase, trim, basic validation"""
    if pd.isna(upi) or upi == '':
        return None
    
    upi_clean = str(upi).strip().lower()
    if '@' in upi_clean and len(upi_clean) >= 5:
        return upi_clean
    else:
        return None

df_10k['payout_upi_id'] = df_10k['payout_upi_id'].apply(standardize_upi)
df_25k['payout_upi_id'] = df_25k['payout_upi_id'].apply(standardize_upi)
```

### 9. Save Standardized Data

```python
df_10k.to_csv('../data/cleaned/shops_10k_standardized.csv', index=False)
df_25k.to_csv('../data/cleaned/shops_25k_standardized.csv', index=False)

print(f"Standardized data saved")
print(f"10k: {len(df_10k)} rows")
print(f"25k: {len(df_25k)} rows")
```

### 10. Git Commit

```bash
git add notebooks/Phase3_Standardize.ipynb
git commit -m "Phase 3: Data standardization complete"
```

---

## DAY 6 (3-4 hours)

### 1. Verification

- [ ] Open standardized CSVs in LibreOffice Calc
- [ ] Verify phones are all 10 digits
- [ ] Verify names are Title Case
- [ ] Verify dates are ISO format
- [ ] Spot-check 50 rows

### 2. Document Changes

**Update** `output/transformation_log.txt`:

```
Phase 3 Changes:
================

Phones: Standardized to 10 digits
  - Removed +91, 91-, spaces, dashes
  - Invalid phones → null
  - Valid: 9,200 (25k: 22,800)

Business names: Title case, trimmed
  - All leading/trailing spaces removed
  - All names now consistent casing

Postal codes: Validated 6 digits
  - Already done in Phase 2
  - No further changes

Dates: ISO format (YYYY-MM-DD HH:MM:SS)
  - All dates now consistent

GST numbers: Validated 15 characters
  - Invalid → null

UPI IDs: Lowercase, basic validation
  - All lowercase
  - Valid: 7,200 (25k: 18,100)
```

### 3. Git Commit

```bash
git add output/transformation_log.txt
git commit -m "Phase 3 complete: Standardization documented"
```

### ✅ PHASE 3 DONE

**Time spent:** ~24-26 hours  
**Remaining:** ~24-26 hours

---

# PHASE 4: VALIDATION RULES (Days 7-8)

## DAY 7 (4 hours)

### 1. Create Phase 4 Notebook

- [ ] New → Python 3 → `Phase4_Validation.ipynb`

### 2. Load Standardized Data

```python
import pandas as pd

df_10k = pd.read_csv('../data/cleaned/shops_10k_standardized.csv')
```

### 3. Write Validation Rules

```python
validation_results = {}

# Rule 1: created_at before updated_at
rule_1 = df_10k[pd.to_datetime(df_10k['created_at'], errors='coerce') > 
                  pd.to_datetime(df_10k['updated_at'], errors='coerce')]
validation_results['rule_1_date_order'] = {
    'count': len(rule_1),
    'rule': 'created_at must be <= updated_at',
    'fails': rule_1
}

# Rule 2: Active shops must have subscription plan
rule_2 = df_10k[(df_10k['status'] == 'active') & (df_10k['subscription_plan'].isna())]
validation_results['rule_2_active_plan'] = {
    'count': len(rule_2),
    'rule': 'Active status requires subscription_plan',
    'fails': rule_2
}

# Rule 3: Registered GST must have GST number
rule_3 = df_10k[(df_10k['gst_status'] == 'registered') & (df_10k['gst_number'].isna())]
validation_results['rule_3_gst_registered'] = {
    'count': len(rule_3),
    'rule': 'Registered GST status requires gst_number',
    'fails': rule_3
}

# Rule 4: Postal code cannot be null
rule_4 = df_10k[df_10k['postal_code'].isna()]
validation_results['rule_4_postal_null'] = {
    'count': len(rule_4),
    'rule': 'postal_code cannot be null',
    'fails': rule_4
}

# Rule 5: City cannot be null
rule_5 = df_10k[df_10k['city'].isna()]
validation_results['rule_5_city_null'] = {
    'count': len(rule_5),
    'rule': 'city cannot be null',
    'fails': rule_5
}
```

### 4. Document Validation Rules

**File:** `output/validation_rules.txt`

```
================================================================================
VALIDATION RULES
================================================================================

Rule 1: Date Logic
  Check: created_at <= updated_at
  Fails: <count> rows
  Action: Remove or investigate

Rule 2: Active Subscription
  Check: status='active' THEN subscription_plan NOT NULL
  Fails: <count> rows
  Action: Remove or fix subscription_plan

Rule 3: GST Registration
  Check: gst_status='registered' THEN gst_number NOT NULL
  Fails: <count> rows
  Action: Remove or verify GST status

Rule 4: Required Postal Code
  Check: postal_code NOT NULL
  Fails: <count> rows
  Action: Remove (should be zero after Phase 2)

Rule 5: Required City
  Check: city NOT NULL
  Fails: <count> rows
  Action: Remove if null

================================================================================
```

### 5. Save Validation Results

```python
# Save rows that failed validation
failed_rows = pd.concat([v['fails'] for v in validation_results.values()])
failed_rows.to_csv('../output/validation_failures.csv', index=False)

# Save summary
summary = pd.DataFrame([
    {'Rule': k, 'Failed_Rows': v['count']}
    for k, v in validation_results.items()
])
summary.to_csv('../output/validation_summary.csv', index=False)

print(summary)
```

### 6. Git Commit

```bash
git add notebooks/Phase4_Validation.ipynb output/validation_rules.txt output/validation_summary.csv
git commit -m "Phase 4: Validation rules and failure detection"
```

---

## DAY 8 (4 hours)

### 1. Review Validation Results

- [ ] How many rows failed each rule?
- [ ] Are failures acceptable or must be removed?

### 2. Make Decisions

For each rule failure, decide:
- **REMOVE** the row (if data is corrupted)
- **INVESTIGATE** (if it's a business logic edge case)
- **ACCEPT** (if it's valid despite the rule)

```python
# Example: If Rule 1 fails (dates out of order) → REMOVE
df_10k = df_10k[pd.to_datetime(df_10k['created_at'], errors='coerce') <= 
                 pd.to_datetime(df_10k['updated_at'], errors='coerce')]

# Example: If Rule 2 fails (active with no plan) → INVESTIGATE
# (This might be a race condition; investigate with business owner)
```

### 3. Save Final Clean Data

```python
df_10k.to_csv('../data/processed/shops_10k_final.csv', index=False)
df_25k.to_csv('../data/processed/shops_25k_final.csv', index=False)

print(f"Final clean data saved")
print(f"10k: {len(df_10k)} rows")
print(f"25k: {len(df_25k)} rows")
```

### 4. Update Transformation Log

Add Phase 4 summary to `output/transformation_log.txt`

### 5. Git Commit

```bash
git add data/processed/ output/validation_failures.csv
git commit -m "Phase 4 complete: Validation and final clean data"
```

### ✅ PHASE 4 DONE

**Time spent:** ~32-34 hours  
**Remaining:** ~16-18 hours

---

# PHASE 5: SQL ANALYSIS (Days 9-11)

## DAY 9 (4 hours)

### 1. Load Final Data into SQLite

```python
import pandas as pd
import sqlite3

# Load cleaned data
df_10k = pd.read_csv('../data/processed/shops_10k_final.csv')

# Create SQLite database
conn = sqlite3.connect('../data/shops_analysis.db')
df_10k.to_sql('shops', conn, if_exists='replace', index=False)

print("Data loaded into SQLite")
```

### 2. Write SQL Queries

**File:** `sql/queries.sql`

```sql
-- Query 1: Shops by State
SELECT state, COUNT(*) as total_shops,
       SUM(CASE WHEN status='active' THEN 1 ELSE 0 END) as active
FROM shops
GROUP BY state
ORDER BY total_shops DESC
LIMIT 20;

-- Query 2: Top 10 Printer Makes
SELECT printer_make, COUNT(*) as count,
       ROUND(100.0*COUNT()/(SELECT COUNT(*) FROM shops),2) as percent
FROM shops
WHERE printer_make != 'Not_Set'
GROUP BY printer_make
ORDER BY count DESC
LIMIT 10;

-- Query 3: Subscription Plans (Active Only)
SELECT subscription_plan, COUNT(*) as count,
       ROUND(100.0*COUNT()/(SELECT COUNT(*) FROM shops WHERE status='active'),2) as percent
FROM shops
WHERE status='active'
GROUP BY subscription_plan;

-- Query 4: UPI Configuration Rate
SELECT 
  COUNT(CASE WHEN payout_upi_id IS NOT NULL THEN 1 END) as with_upi,
  COUNT(CASE WHEN payout_upi_id IS NULL THEN 1 END) as without_upi,
  COUNT(*) as total,
  ROUND(100.0*COUNT(CASE WHEN payout_upi_id IS NOT NULL THEN 1 END)/COUNT(*),2) as configured_percent
FROM shops;

-- Query 5: GST Registration Status
SELECT gst_status, COUNT(*) as count,
       ROUND(100.0*COUNT()/(SELECT COUNT(*) FROM shops),2) as percent
FROM shops
GROUP BY gst_status
ORDER BY count DESC;
```

### 3. Run Queries in Python

```python
import sqlite3
import pandas as pd

conn = sqlite3.connect('../data/shops_analysis.db')

# Query 1
result_1 = pd.read_sql_query(
    "SELECT state, COUNT(*) as count FROM shops GROUP BY state ORDER BY count DESC LIMIT 15;",
    conn
)
print("Query 1 - Top States:")
print(result_1)
result_1.to_csv('../output/query_1_states.csv', index=False)

# Query 2
result_2 = pd.read_sql_query(
    "SELECT printer_make, COUNT(*) as count FROM shops WHERE printer_make != 'Not_Set' GROUP BY printer_make ORDER BY count DESC LIMIT 10;",
    conn
)
print("\nQuery 2 - Printer Makes:")
print(result_2)
result_2.to_csv('../output/query_2_printers.csv', index=False)

# Continue for remaining queries...

conn.close()
```

### 4. Git Commit

```bash
git add sql/queries.sql output/query_*.csv
git commit -m "Phase 5: SQL queries executed"
```

---

## DAY 10 (4 hours)

### 1. Create Visualizations

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../data/processed/shops_10k_final.csv')

# Chart 1: Top 15 States
fig, ax = plt.subplots(figsize=(12, 6))
df['state'].value_counts().head(15).plot(kind='barh', ax=ax)
plt.title('Top 15 States by Shop Count')
plt.xlabel('Number of Shops')
plt.tight_layout()
plt.savefig('../output/charts/chart_01_states.png', dpi=300)
print("Chart 1 saved")

# Chart 2: Subscription Plans
fig, ax = plt.subplots(figsize=(8, 6))
df[df['status']=='active']['subscription_plan'].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=ax)
plt.title('Subscription Plans (Active Shops)')
plt.ylabel('')
plt.tight_layout()
plt.savefig('../output/charts/chart_02_subscription_plans.png', dpi=300)
print("Chart 2 saved")

# Chart 3: Printer Availability
fig, ax = plt.subplots(figsize=(8, 6))
printer_status = [
    (df['printer_make'] == 'Not_Set').sum(),
    (df['printer_make'] != 'Not_Set').sum()
]
ax.pie(printer_status, labels=['No Printer', 'Printer Configured'], autopct='%1.1f%%')
plt.title('Printer Configuration Status')
plt.tight_layout()
plt.savefig('../output/charts/chart_03_printers.png', dpi=300)
print("Chart 3 saved")

# Chart 4: UPI Configuration
fig, ax = plt.subplots(figsize=(8, 6))
upi_status = [
    df['payout_upi_id'].notna().sum(),
    df['payout_upi_id'].isna().sum()
]
ax.pie(upi_status, labels=['UPI Configured', 'UPI Not Configured'], autopct='%1.1f%%')
plt.title('UPI Configuration Rate')
plt.tight_layout()
plt.savefig('../output/charts/chart_04_upi.png', dpi=300)
print("Chart 4 saved")

# Chart 5: Shop Status Distribution
fig, ax = plt.subplots(figsize=(10, 6))
df['status'].value_counts().plot(kind='bar', ax=ax)
plt.title('Shop Status Distribution')
plt.xlabel('Status')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('../output/charts/chart_05_status.png', dpi=300)
print("Chart 5 saved")
```

### 2. Git Commit

```bash
git add output/charts/
git commit -m "Phase 5: Data visualizations created"
```

---

## DAY 11 (4 hours)

### 1. Create Python Analysis Notebook

- [ ] New → Python 3 → `Phase5_Analysis.ipynb`
- [ ] Include: All SQL queries + Python analysis + Visualizations
- [ ] Add narrative: "What does this tell us about the business?"

### 2. Key Insights to Document

```python
# Example insights:
print("""
KEY INSIGHTS:

1. Geographic Distribution:
   - Shops concentrated in <top 3 states>
   - <X>% of shops in India

2. Subscription Plans:
   - <Y>% use enterprise plan
   - <Z>% still on trial

3. Printer Configuration:
   - <A>% of shops have printers set
   - Top 3 printer makes: <B>, <C>, <D>

4. Payment Setup:
   - <E>% have UPI configured
   - <F>% missing UPI (need to follow up)

5. Business Health:
   - <G>% shops active
   - <H>% suspended (need investigation)

6. Data Quality:
   - Started with 10,000 records
   - Removed <I> rows due to quality issues
   - Final: <J> production-ready records
""")
```

### 3. Final Git Commit

```bash
git add notebooks/Phase5_Analysis.ipynb
git commit -m "Phase 5 complete: SQL analysis and Python insights"
```

### ✅ PHASE 5 DONE

**Time spent:** ~40-42 hours  
**Remaining:** ~6-8 hours

---

# PHASE 6: EXCEL DASHBOARD (Day 12)

## DAY 12 MORNING (4-5 hours)

### 1. Create Excel Dashboard

Open LibreOffice Calc (or Excel) and create `output/dashboard.xlsx` with these tabs:

**Tab 1: Summary**
```
KEY METRICS
Total Shops: 9,385
Active Shops: X
Suspended: Y
Trial Subscriptions: Z

Data Quality:
  Started: 10,000 records
  Removed: 615 (issues)
  Final: 9,385 (production-ready)
```

**Tab 2: Geography**
- Table: Top 20 states, count, active %
- Chart: Bar chart of top 15 states

**Tab 3: Subscriptions**
- Table: Plans, counts, percentages
- Chart: Pie chart of subscription plans

**Tab 4: Equipment**
- Table: Printer makes, counts
- Chart: Bar chart of top printers

**Tab 5: Validation**
- Summary of issues found
- Summary of fixes applied

### 2. Add Charts in LibreOffice

- [ ] Insert Chart for each tab
- [ ] Format professionally (titles, legends, colors)

### 3. Create Python Export (Alternative)

```python
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill

# Create workbook
wb = Workbook()

# Remove default sheet
wb.remove(wb.active)

# Tab 1: Summary
ws1 = wb.create_sheet('Summary')
ws1['A1'] = 'Key Metrics'
ws1['A2'] = 'Total Shops'
ws1['B2'] = 9385
ws1['A3'] = 'Active Shops'
ws1['B3'] = 7200  # Example

# Tab 2: Query Results
ws2 = wb.create_sheet('State Analysis')
state_data = pd.read_csv('../output/query_1_states.csv')
for r, row in enumerate(state_data.values):
    for c, val in enumerate(row):
        ws2.cell(row=r+1, column=c+1).value = val

# Save
wb.save('../output/dashboard.xlsx')
print("Dashboard created: output/dashboard.xlsx")
```

### 4. Final Verification

- [ ] Dashboard opens in Excel/LibreOffice
- [ ] All tabs visible
- [ ] All charts display correctly
- [ ] Numbers match your analysis

### 5. FINAL GIT COMMITS

```bash
# Commit dashboard
git add output/dashboard.xlsx
git commit -m "Phase 6: Excel dashboard created"

# Final summary commit
git add -A
git commit -m "Training project complete: All 8 deliverables ready"

# View all commits
git log --oneline
```

### 6. FINAL CHECKLIST

- [ ] **Cleaned Datasets** (2 files)
  - ✅ `data/processed/shops_10k_final.csv`
  - ✅ `data/processed/shops_25k_final.csv`

- [ ] **Documentation** (3 files)
  - ✅ `output/issue_log.txt`
  - ✅ `output/transformation_log.txt`
  - ✅ `output/validation_rules.txt`

- [ ] **Code** (5 files)
  - ✅ `notebooks/Phase1_Profile.ipynb`
  - ✅ `notebooks/Phase2_Missing_Duplicates.ipynb`
  - ✅ `notebooks/Phase3_Standardize.ipynb`
  - ✅ `notebooks/Phase4_Validation.ipynb`
  - ✅ `notebooks/Phase5_Analysis.ipynb`

- [ ] **Analysis** (2 files)
  - ✅ `sql/queries.sql`
  - ✅ `output/dashboard.xlsx`

- [ ] **Git History**
  - ✅ At least 6 commits (one per phase)
  - ✅ Commit messages describe work done
  - ✅ Can do `git log` to see all phases

---

# FINAL: INTERVIEW PREP

When an interviewer asks, "Show us your data work," you pull up your GitHub repo and say:

> "I profiled 25,000 production shop records using pandas. I identified 15+ data quality issues including formatting inconsistencies, missing values, and logical errors. I standardized phone numbers, dates, and postal codes using regex. I removed 615 corrupted rows after validation. I wrote 5 SQL queries to analyze geographic distribution, subscription plans, and equipment configuration. I created Python visualizations and an Excel dashboard. Here's my GitHub repo with all code, documentation, and final deliverables."

**Then show them:**
1. One Jupyter notebook (walk through the logic)
2. Your issue_log.txt (shows you found real problems)
3. Your SQL queries (shows you can write SQL)
4. Your Excel dashboard (shows business communication skill)
5. Your Git commits (shows you version-controlled your work)

**They will hire you.**

---

## You've Got This 💪

**Day 0:** 1 hour (setup)  
**Days 1-2:** 8 hours (profiling)  
**Days 3-4:** 8 hours (cleaning)  
**Days 5-6:** 8 hours (standardization)  
**Days 7-8:** 8 hours (validation)  
**Days 9-11:** 12 hours (analysis)  
**Day 12:** 4 hours (dashboard)  

**Total: ~49 hours across 7 days**

That's professional-grade data engineering work.

Now go build your portfolio.

---

*Questions? Your issue log, transformation log, SQL queries, and code are your answers.*

*Good luck.*

---

*Training Program v1.0*  
*Apex AGI Solutions*  
*2026-09-23*
