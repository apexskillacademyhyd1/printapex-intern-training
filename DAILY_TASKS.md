# Your Daily Tasks

I update this file each morning with your tasks for the day. Check back here every morning to see what you need to work on.

You're working with real production data from our system. A CSV file with quality problems you need to identify and fix. By the end of this week, you'll have completed a full data analytics project.

---

## DAY 0 - Setup (Complete Before Day 1)

Get your environment ready today so you can start real work tomorrow.

### Step 1: Install Tools

Download and install these (all free):

**Python 3.10+** - https://www.python.org/downloads/
- During install, check "Add Python to PATH"
- After install, open terminal and run: `python --version`
- Verify you see 3.10 or higher

**Git** - https://git-scm.com
- This tracks all your work

**Excel** (or similar spreadsheet tool)
- You'll use this for your final dashboard

**VS Code (optional)** - https://code.visualstudio.com
- Good for editing Python files

### Step 2: Create Your Project

Open terminal and run:

```
mkdir PrintShopDataProject
cd PrintShopDataProject
git init
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

Create your folder structure:

```
mkdir data\raw data\cleaned data\processed notebooks scripts sql output\charts
```

### Step 3: Set Up Python

Create a virtual environment:

```
python -m venv venv
venv\Scripts\activate
```

You should see `(venv)` in your terminal. Then install libraries:

```
pip install pandas jupyter matplotlib seaborn
```

### Step 4: Create .gitignore

In your PrintShopDataProject folder, create a file called `.gitignore` with this:

```
*.csv
*.xlsx
*.db
venv/
__pycache__/
.ipynb_checkpoints/
```

This keeps large files out of Git.

### Step 5: Get Your Data

Download this file from this repository:
- `shops_raw_data_10k.csv`

Put it in your `data/raw/` folder.

### Step 6: First Commit

```
git add .
git commit -m "Initial project setup"
```

### Step 7: Test Jupyter

```
jupyter notebook
```

A browser window should open. If it does, close it with Ctrl+C. Good—Jupyter works.

### You're Ready

Setup is done. See you tomorrow for Day 1.

---

## DAY 1 - Load and Inspect the Data

**What you're doing:** Loading the data into Python and understanding what you have.

**Why it matters:** You need to see what problems exist before you can fix them.

### Your Tasks

1. **Open Jupyter and create a new notebook**

   ```
   jupyter notebook
   ```

   Create `notebooks/01_data_profiling.ipynb`

2. **Load the 10k dataset**

   In your notebook, run:

   ```python
   import pandas as pd
   
   df_10k = pd.read_csv('../data/raw/shops_raw_data_10k.csv')
   print(df_10k.head(10))
   print(df_10k.shape)
   ```

   You should see the first 10 rows and the dataset shape (rows, columns).

3. **Get basic info**

   ```python
   print(df_10k.info())
   print(df_10k.describe())
   ```

   Look at data types. Look at numeric summaries. What do you notice?

4. **Check for null values**

   ```python
   print(df_10k.isnull().sum())
   ```

   This shows you how many missing values each column has.

5. **Save your notebook**

   Name it clearly: `01_data_profiling.ipynb`

### Your Deliverable

A Jupyter notebook showing:
- Dataset loaded
- First 10 rows
- Data types for each column
- Null value counts for each column

### Commit Your Work

```
git add notebooks/01_data_profiling.ipynb
git commit -m "Day 1: Initial data profiling"
```

### What You Should See

You'll notice:
- Some columns have missing values (NaN)
- Some columns are strings, some are numbers, some are dates
- Some values might look odd or inconsistent

That's what we're going to fix over the next week.

## DAY 2 - Data Cleaning Part 1 (Handling Nulls & Data Types)

**What you're doing:** Finding and fixing missing values and incorrect data types.

**Why it matters:** Bad data causes bad analysis. You need clean data before any real work.

### Your Tasks

1. **Create a new notebook: `02_data_cleaning_part1.ipynb`**

   Open Jupyter:
   ```
   jupyter notebook
   ```

2. **Load the dataset**

   ```python
   import pandas as pd
   import numpy as np
   
   df_10k = pd.read_csv('../data/raw/shops_raw_data_10k.csv')
   
   print("Dataset shape:", df_10k.shape)
   ```

3. **Identify null values by column**

   ```python
   print("=" * 50)
   print("DATASET - NULL VALUE ANALYSIS")
   print("=" * 50)
   null_counts = df_10k.isnull().sum()
   null_percent = (df_10k.isnull().sum() / len(df_10k)) * 100
   
   for col in df_10k.columns:
       if null_counts[col] > 0:
           print(f"{col}: {null_counts[col]} nulls ({null_percent[col]:.1f}%)")
   ```

4. **Fix numeric columns: Replace nulls with median**

   ```python
   numeric_cols = df_10k.select_dtypes(include=[np.number]).columns
   
   for col in numeric_cols:
       if df_10k[col].isnull().sum() > 0:
           median_val = df_10k[col].median()
           df_10k[col].fillna(median_val, inplace=True)
           print(f"Filled {col} nulls with median: {median_val}")
   ```

5. **Fix categorical columns: Use "Unknown" for nulls**

   ```python
   categorical_cols = df_10k.select_dtypes(include=['object']).columns
   
   for col in categorical_cols:
       if df_10k[col].isnull().sum() > 0:
           df_10k[col].fillna('Unknown', inplace=True)
           print(f"Filled {col} nulls with 'Unknown'")
   ```

6. **Verify no nulls remain**

   ```python
   print("\nDataset remaining nulls:", df_10k.isnull().sum().sum())
   ```

7. **Save cleaned dataset**

   ```python
   df_10k.to_csv('../data/cleaned/shops_cleaned_10k.csv', index=False)
   print("✓ Cleaned dataset saved to data/cleaned/")
   ```

### Your Deliverable

A Jupyter notebook showing:
- Null value counts for the dataset
- Before/after comparison
- Cleaned dataset saved to `data/cleaned/`

### Commit Your Work

```
git add notebooks/02_data_cleaning_part1.ipynb
git add data/cleaned/
git commit -m "Day 2: Null value handling and initial data cleaning"
```

### What You Learned

- How to identify missing data
- Different strategies for filling nulls (median for numbers, 'Unknown' for text)
- How to verify data quality improved

### Tomorrow: Day 3

Tomorrow we'll work on duplicate detection and fixing inconsistent formats.

---

## DAY 3 - Data Cleaning Part 2 (Duplicates & Format Consistency)

**What you're doing:** Finding duplicate rows and fixing inconsistent data formats.

**Why it matters:** Duplicates skew your analysis. Inconsistent formats hide real problems. Clean data tells the true story.

### Your Tasks

1. **Create a new notebook: `03_data_cleaning_part2.ipynb`**

   Open Jupyter:
   ```
   jupyter notebook
   ```

2. **Load the cleaned dataset from Day 2**

   ```python
   import pandas as pd
   import numpy as np
   
   df_10k = pd.read_csv('../data/cleaned/shops_cleaned_10k.csv')
   
   print("Dataset shape:", df_10k.shape)
   ```

3. **Find duplicate rows**

   ```python
   print("=" * 50)
   print("DUPLICATE ANALYSIS")
   print("=" * 50)
   
   duplicates = df_10k.duplicated().sum()
   print(f"Total duplicate rows: {duplicates}")
   
   if duplicates > 0:
       print("\nSample duplicates:")
       print(df_10k[df_10k.duplicated(keep=False)].head(10))
   ```

4. **Remove duplicates**

   ```python
   # Keep the first occurrence, remove subsequent duplicates
   df_deduped = df_10k.drop_duplicates(keep='first')
   
   print(f"Dataset: {len(df_10k)} → {len(df_deduped)} rows ({duplicates} removed)")
   ```

5. **Identify inconsistent string formats**

   Look for columns with text data that might be inconsistent:

   ```python
   # For each text column, show unique values and their frequencies
   for col in df_deduped.select_dtypes(include=['object']).columns:
       print(f"\n{col} - Value counts:")
       print(df_deduped[col].value_counts().head(10))
   ```

6. **Standardize text formatting**

   ```python
   # Convert all text to lowercase and strip whitespace
   for col in df_deduped.select_dtypes(include=['object']).columns:
       df_deduped[col] = df_deduped[col].str.lower().str.strip()
   
   print("✓ Text formatting standardized (lowercase + whitespace removed)")
   ```

7. **Check for data type consistency**

   ```python
   print("\nDataset Data Types:")
   print(df_deduped.dtypes)
   ```

8. **Identify and fix outliers in numeric columns**

   ```python
   numeric_cols = df_deduped.select_dtypes(include=[np.number]).columns
   
   for col in numeric_cols:
       Q1 = df_deduped[col].quantile(0.25)
       Q3 = df_deduped[col].quantile(0.75)
       IQR = Q3 - Q1
       lower_bound = Q1 - 1.5 * IQR
       upper_bound = Q3 + 1.5 * IQR
       
       outliers = df_deduped[(df_deduped[col] < lower_bound) | (df_deduped[col] > upper_bound)]
       
       if len(outliers) > 0:
           print(f"\n{col}: {len(outliers)} outliers detected")
           print(f"  Range: {lower_bound:.2f} to {upper_bound:.2f}")
           print(f"  Outlier values: {outliers[col].unique()[:5]}")
   ```

9. **Save deduplicated and standardized dataset**

   ```python
   df_deduped.to_csv('../data/processed/shops_processed_10k.csv', index=False)
   print("✓ Processed dataset saved to data/processed/")
   ```

### Your Deliverable

A Jupyter notebook showing:
- Duplicate row counts
- Before/after row counts
- Text standardization applied
- Outliers identified by column
- Processed dataset saved to `data/processed/`

### Commit Your Work

```
git add notebooks/03_data_cleaning_part2.ipynb
git add data/processed/
git commit -m "Day 3: Duplicate removal and format standardization"
```

### What You Learned

- How to identify and remove duplicates
- How to standardize text formatting
- How to detect outliers using the Interquartile Range (IQR) method
- Data quality is an iterative process—each pass reveals more problems

### Tomorrow: Day 4

Tomorrow we'll validate the data against business rules and create our first analysis dashboard.

---

## DAY 4 - Data Validation & Business Rules

**What you're doing:** Applying business logic and validation rules to ensure data integrity.

**Why it matters:** Clean data isn't just about formatting—it needs to make sense for your business. Invalid combinations or impossible values can break reports and lead to wrong decisions.

### Your Tasks

1. **Create a new notebook: `04_data_validation.ipynb`**

   Open Jupyter:
   ```
   jupyter notebook
   ```

2. **Load the processed dataset from Day 3**

   ```python
   import pandas as pd
   import numpy as np
   from datetime import datetime
   
   df = pd.read_csv('../data/processed/shops_processed_10k.csv')
   
   print("Dataset shape:", df.shape)
   print("\nFirst few rows:")
   print(df.head())
   ```

3. **Define validation rules**

   Create a list to track all validation issues:

   ```python
   validation_issues = []
   
   def log_issue(rule_name, count, description):
       validation_issues.append({
           'Rule': rule_name,
           'Failed_Records': count,
           'Description': description
       })
       print(f"❌ {rule_name}: {count} records failed - {description}")
   ```

4. **Rule 1: Check for negative numeric values**

   ```python
   print("\n" + "="*50)
   print("RULE 1: NEGATIVE VALUE CHECK")
   print("="*50)
   
   numeric_cols = df.select_dtypes(include=[np.number]).columns
   
   for col in numeric_cols:
       negative_count = (df[col] < 0).sum()
       if negative_count > 0:
           log_issue(f"Negative_{col}", negative_count, f"{col} should not be negative")
           print(f"  Sample negative values: {df[df[col] < 0][col].head().tolist()}")
   ```

5. **Rule 2: Date consistency checks**

   ```python
   print("\n" + "="*50)
   print("RULE 2: DATE CONSISTENCY")
   print("="*50)
   
   # Example: created_at should be before updated_at
   date_cols = [col for col in df.columns if 'date' in col.lower() or 'at' in col.lower()]
   print(f"Date columns found: {date_cols}")
   
   # Add your specific date validation logic based on your columns
   ```

6. **Rule 3: Required field validation**

   ```python
   print("\n" + "="*50)
   print("RULE 3: REQUIRED FIELDS")
   print("="*50)
   
   # Define which columns should never be empty/null
   required_fields = ['business_name', 'city', 'state']  # Adjust based on your data
   
   for col in required_fields:
       if col in df.columns:
           missing = df[col].isnull().sum()
           empty = (df[col] == '').sum() if df[col].dtype == 'object' else 0
           total_invalid = missing + empty
           
           if total_invalid > 0:
               log_issue(f"Required_{col}", total_invalid, f"{col} is required but has missing/empty values")
   ```

7. **Rule 4: Value range validation**

   ```python
   print("\n" + "="*50)
   print("RULE 4: VALUE RANGES")
   print("="*50)
   
   # Example: Phone numbers should be 10 digits (if you have a phone column)
   if 'contact_phone' in df.columns:
       df['phone_length'] = df['contact_phone'].astype(str).str.len()
       invalid_phones = ((df['phone_length'] != 10) & (df['contact_phone'].notna())).sum()
       if invalid_phones > 0:
           log_issue("Invalid_Phone_Length", invalid_phones, "Phone numbers should be exactly 10 digits")
   
   # Example: Postal codes should be 6 digits (Indian PIN codes)
   if 'postal_code' in df.columns:
       df['pin_length'] = df['postal_code'].astype(str).str.len()
       invalid_pins = ((df['pin_length'] != 6) & (df['postal_code'].notna())).sum()
       if invalid_pins > 0:
           log_issue("Invalid_Postal_Code", invalid_pins, "Postal codes should be exactly 6 digits")
   ```

8. **Rule 5: Categorical value validation**

   ```python
   print("\n" + "="*50)
   print("RULE 5: VALID CATEGORIES")
   print("="*50)
   
   # Example: Status column should only have specific values
   if 'status' in df.columns:
       valid_statuses = ['active', 'inactive', 'pending', 'suspended']
       invalid_status = ~df['status'].isin(valid_statuses)
       invalid_count = invalid_status.sum()
       
       if invalid_count > 0:
           log_issue("Invalid_Status", invalid_count, f"Status must be one of {valid_statuses}")
           print(f"  Found invalid values: {df[invalid_status]['status'].unique().tolist()}")
   ```

9. **Rule 6: Cross-field validation**

   ```python
   print("\n" + "="*50)
   print("RULE 6: CROSS-FIELD LOGIC")
   print("="*50)
   
   # Example: If a shop has GST registration, it should have a GST number
   if 'gst_registered' in df.columns and 'gst_number' in df.columns:
       missing_gst = ((df['gst_registered'] == 'yes') & (df['gst_number'].isnull())).sum()
       if missing_gst > 0:
           log_issue("GST_Registration_Mismatch", missing_gst, "Registered shops must have GST number")
   ```

10. **Create validation summary report**

    ```python
    print("\n" + "="*50)
    print("VALIDATION SUMMARY REPORT")
    print("="*50)
    
    if len(validation_issues) == 0:
        print("✅ All validation rules passed! Dataset is valid.")
    else:
        validation_df = pd.DataFrame(validation_issues)
        print(f"\n❌ Found {len(validation_issues)} validation failures:\n")
        print(validation_df.to_string(index=False))
        
        # Save validation report
        validation_df.to_csv('../output/validation_report.csv', index=False)
        print("\n✓ Validation report saved to output/validation_report.csv")
    
    # Calculate data quality score
    total_records = len(df)
    total_failed = sum([issue['Failed_Records'] for issue in validation_issues])
    quality_score = ((total_records - total_failed) / total_records) * 100
    
    print(f"\n📊 Data Quality Score: {quality_score:.2f}%")
    print(f"   Total records: {total_records}")
    print(f"   Failed validations: {total_failed}")
    print(f"   Clean records: {total_records - total_failed}")
    ```

11. **Clean the data based on validation results**

    ```python
    # Decide what to do with failed records
    # Option 1: Remove all invalid rows (aggressive)
    # Option 2: Fix specific issues (conservative)
    # Option 3: Flag for manual review (safe)
    
    # Example: Remove rows with critical issues only
    df_validated = df.copy()
    
    # Your cleaning logic here based on validation results
    print(f"\n✓ Dataset after validation: {len(df_validated)} rows")
    
    # Save validated dataset
    df_validated.to_csv('../data/processed/shops_validated_10k.csv', index=False)
    print("✓ Validated dataset saved to data/processed/shops_validated_10k.csv")
    ```

### Your Deliverable

A Jupyter notebook showing:
- All validation rules executed
- Validation summary report
- Data quality score
- Validated dataset saved to `data/processed/`
- Validation report saved to `output/`

### Commit Your Work

```
git add notebooks/04_data_validation.ipynb
git add output/validation_report.csv
git add data/processed/shops_validated_10k.csv
git commit -m "Day 4: Data validation and business rules applied"
```

### What You Learned

- How to define and implement business rules
- How to validate data across multiple dimensions
- How to create data quality reports
- How to calculate data quality metrics
- The difference between clean data and valid data

### Tomorrow: Day 5

Tomorrow we'll start analyzing the data with SQL queries and basic statistics.

---

## DAYS 5-7 (Coming Soon)

Check back tomorrow for Day 5 tasks.
