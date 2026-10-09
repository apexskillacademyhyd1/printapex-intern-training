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

## DAY 4 - Data Validation & Business Rules (CORRECTED)

**What you're doing:** Applying business logic and validation rules to ensure data integrity.

**Why it matters:** Clean data isn't just about formatting—it needs to make sense for your business. Invalid combinations or impossible values can break reports and lead to wrong decisions.

### ⚠️ IMPORTANT: Corrected Version

The original Day 4 code had **10 critical errors**. This corrected version fixes all of them. Use this code, not the earlier version.

**Fixes Applied:**
- ✓ Type conversion (string → numeric/datetime) before comparisons
- ✓ Proper phone/PIN validation (counts digits only, ignores formatting)
- ✓ Complete date consistency implementation (was incomplete)
- ✓ Whitespace handling in required fields
- ✓ Case-insensitive categorical validation
- ✓ Correct column names (gst_status, not gst_registered)
- ✓ Accurate quality score (counts unique failed records, not duplicates)
- ✓ Temp column cleanup (removes phone_length, pin_length)
- ✓ Actual data cleaning (removes invalid records)

### Your Tasks

1. **Create a new notebook: `04_data_validation.ipynb`**

   Open Jupyter:
   ```
   jupyter notebook
   ```

2. **Load and convert data types (CRITICAL)**

   ```python
   import pandas as pd
   import numpy as np
   from datetime import datetime
   import re
   
   df = pd.read_csv('../data/processed/shops_processed_10k.csv')
   
   print(f"Dataset shape: {df.shape}")
   print(f"First few rows:")
   print(df.head())
   
   # FIX #8: Convert numeric columns (prevents TypeError in rules)
   numeric_columns = ['annual_revenue', 'monthly_print_volume', 'employee_count']
   for col in numeric_columns:
       if col in df.columns:
           df[col] = pd.to_numeric(df[col], errors='coerce')
           print(f"✓ Converted {col} to numeric")
   
   # FIX #2: Convert date columns (enables date comparisons)
   date_columns = ['created_at', 'updated_at', 'last_order_date']
   for col in date_columns:
       if col in df.columns:
           df[col] = pd.to_datetime(df[col], errors='coerce')
           print(f"✓ Converted {col} to datetime")
   ```

3. **Define validation tracking (NEW)**

   ```python
   validation_issues = []
   failed_records_mask = pd.Series([False] * len(df))  # FIX #7: Track unique failures
   
   def log_issue(rule_name, count, description, affected_indices=None):
       global failed_records_mask
       
       validation_issues.append({
           'Rule': rule_name,
           'Failed_Records': count,
           'Description': description
       })
       
       # Mark these records as failed
       if affected_indices is not None:
           failed_records_mask.iloc[affected_indices] = True
       
       print(f"❌ {rule_name}: {count} records failed - {description}")
   ```

4. **Rule 1: Negative numeric values (FIXED)**

   ```python
   print("\n" + "-"*60)
   print("RULE 1: NEGATIVE VALUE CHECK")
   print("-"*60)
   
   # Only check actual numeric columns
   numeric_cols = df.select_dtypes(include=[np.number]).columns
   
   for col in numeric_cols:
       negative_mask = (df[col] < 0) & (df[col].notna())
       negative_count = negative_mask.sum()
       
       if negative_count > 0:
           log_issue(
               f"Negative_{col}",
               negative_count,
               f"{col} should not be negative",
               negative_mask[negative_mask].index
           )
           print(f"  Sample: {df[negative_mask][col].head().tolist()}")
       else:
           print(f"  ✓ {col}: No negative values")
   ```

5. **Rule 2: Date consistency (COMPLETE IMPLEMENTATION)**

   ```python
   print("\n" + "-"*60)
   print("RULE 2: DATE CONSISTENCY")
   print("-"*60)
   
   # FIX #2: Actual implementation (was just a stub)
   if 'created_at' in df.columns and 'updated_at' in df.columns:
       # created_at should be <= updated_at
       created_gt_updated = (df['created_at'] > df['updated_at']) & \
                            (df['created_at'].notna()) & (df['updated_at'].notna())
       invalid_count = created_gt_updated.sum()
       
       if invalid_count > 0:
           log_issue(
               "Date_Logic_Error",
               invalid_count,
               "created_at should be <= updated_at",
               created_gt_updated[created_gt_updated].index
           )
       else:
           print("  ✓ All created_at <= updated_at")
   
   # Check for future dates
   if 'created_at' in df.columns:
       future_created = (df['created_at'] > pd.Timestamp.now()) & (df['created_at'].notna())
       future_count = future_created.sum()
       
       if future_count > 0:
           log_issue(
               "Future_Created_Date",
               future_count,
               "created_at should not be in the future",
               future_created[future_created].index
           )
       else:
           print("  ✓ No future dates found")
   ```

6. **Rule 3: Required fields (WHITESPACE HANDLING)**

   ```python
   print("\n" + "-"*60)
   print("RULE 3: REQUIRED FIELDS")
   print("-"*60)
   
   required_fields = {
       'business_name': 'Business name is required',
       'city': 'City is required',
       'state': 'State is required',
   }
   
   for col, description in required_fields.items():
       if col in df.columns:
           # FIX #3: Handle null AND empty AND whitespace-only strings
           is_null = df[col].isnull()
           is_empty_string = (df[col].astype(str).str.strip() == '')
           invalid_mask = is_null | is_empty_string
           invalid_count = invalid_mask.sum()
           
           if invalid_count > 0:
               log_issue(
                   f"Required_{col}",
                   invalid_count,
                   description,
                   invalid_mask[invalid_mask].index
               )
           else:
               print(f"  ✓ {col}: All records have values")
   ```

7. **Rule 4: Value ranges - PHONE & PIN (DIGIT-ONLY COUNTING)**

   ```python
   print("\n" + "-"*60)
   print("RULE 4: VALUE RANGES")
   print("-"*60)
   
   # FIX #4: Phone - count DIGITS only, not all characters
   if 'contact_phone' in df.columns:
       # Extract only digits
       df['_phone_digits'] = df['contact_phone'].astype(str).str.replace(r'\D', '', regex=True)
       
       # Should be exactly 10 digits
       invalid_phones = ((df['_phone_digits'].str.len() != 10) & (df['contact_phone'].notna()))
       invalid_phone_count = invalid_phones.sum()
       
       if invalid_phone_count > 0:
           log_issue(
               "Invalid_Phone_Length",
               invalid_phone_count,
               "Phone numbers should have exactly 10 digits",
               invalid_phones[invalid_phones].index
           )
           print(f"  Sample: {df[invalid_phones]['contact_phone'].head().tolist()}")
       else:
           print(f"  ✓ contact_phone: All valid (10 digits)")
       
       # FIX #10: Clean up temp column
       df.drop('_phone_digits', axis=1, inplace=True)
   
   # FIX #4: Postal code - count DIGITS only, not all characters
   if 'postal_code' in df.columns:
       # Extract only digits
       df['_pin_digits'] = df['postal_code'].astype(str).str.replace(r'\D', '', regex=True)
       
       # Should be exactly 6 digits
       invalid_pins = ((df['_pin_digits'].str.len() != 6) & (df['postal_code'].notna()))
       invalid_pin_count = invalid_pins.sum()
       
       if invalid_pin_count > 0:
           log_issue(
               "Invalid_Postal_Code",
               invalid_pin_count,
               "Postal codes should have exactly 6 digits",
               invalid_pins[invalid_pins].index
           )
           print(f"  Sample: {df[invalid_pins]['postal_code'].head().tolist()}")
       else:
           print(f"  ✓ postal_code: All valid (6 digits)")
       
       # FIX #10: Clean up temp column
       df.drop('_pin_digits', axis=1, inplace=True)
   ```

8. **Rule 5: Categorical validation (CASE-INSENSITIVE)**

   ```python
   print("\n" + "-"*60)
   print("RULE 5: VALID CATEGORIES")
   print("-"*60)
   
   # FIX #5: Case-insensitive to handle mixed-case data
   if 'status' in df.columns:
       valid_statuses = ['active', 'inactive', 'pending', 'suspended']
       
       status_lower = df['status'].astype(str).str.lower().str.strip()
       invalid_status_mask = ~status_lower.isin(valid_statuses) & (df['status'].notna())
       invalid_status_count = invalid_status_mask.sum()
       
       if invalid_status_count > 0:
           log_issue(
               "Invalid_Status",
               invalid_status_count,
               f"Status must be one of {valid_statuses}",
               invalid_status_mask[invalid_status_mask].index
           )
           print(f"  Found: {df[invalid_status_mask]['status'].unique().tolist()}")
       else:
           print(f"  ✓ status: All valid")
   ```

9. **Rule 6: Cross-field validation (CORRECT COLUMN NAMES)**

   ```python
   print("\n" + "-"*60)
   print("RULE 6: CROSS-FIELD LOGIC")
   print("-"*60)
   
   # FIX #6: Use 'gst_status' not 'gst_registered'
   # FIX #3: Handle both null AND empty strings
   if 'gst_status' in df.columns and 'gst_number' in df.columns:
       gst_status_lower = df['gst_status'].astype(str).str.lower().str.strip()
       gst_is_null = df['gst_number'].isnull()
       gst_is_empty = (df['gst_number'].astype(str).str.strip() == '')
       gst_is_missing = gst_is_null | gst_is_empty
       
       # If registered, must have GST number
       missing_gst_mask = (gst_status_lower == 'registered') & gst_is_missing
       missing_gst_count = missing_gst_mask.sum()
       
       if missing_gst_count > 0:
           log_issue(
               "GST_Registration_Mismatch",
               missing_gst_count,
               "Registered shops must have GST number",
               missing_gst_mask[missing_gst_mask].index
           )
       else:
           print(f"  ✓ GST: All registered shops have numbers")
   ```

10. **Validation summary (CORRECTED QUALITY SCORE)**

    ```python
    print("\n" + "="*60)
    print("VALIDATION SUMMARY REPORT")
    print("="*60)
    
    if len(validation_issues) == 0:
        print("\n✅ All validation rules passed! Dataset is valid.")
    else:
        validation_df = pd.DataFrame(validation_issues)
        print(f"\n❌ Found {len(validation_issues)} validation issues:\n")
        print(validation_df.to_string(index=False))
        
        validation_df.to_csv('../output/validation_report.csv', index=False)
        print("\n✓ Validation report saved to output/validation_report.csv")
    
    # FIX #7 & #9: Count UNIQUE failed records (not sum of all violations)
    total_records = len(df)
    unique_failed_records = failed_records_mask.sum()
    quality_score = ((total_records - unique_failed_records) / total_records) * 100
    
    print(f"\n📊 DATA QUALITY SCORE: {quality_score:.2f}%")
    print(f"   Total records: {total_records:,}")
    print(f"   Failed records: {unique_failed_records:,}")
    print(f"   Clean records: {total_records - unique_failed_records:,}")
    
    if quality_score >= 95:
        print("   Status: ✅ EXCELLENT - Ready for analysis")
    elif quality_score >= 80:
        print("   Status: ⚠️  GOOD - Minor issues")
    else:
        print("   Status: ❌ POOR - Major issues")
    ```

11. **Data cleaning & save (FIX #10 - ACTUAL CLEANING)**

    ```python
    # FIX #10: Actually clean the data (was just a copy before)
    print(f"\nBefore cleaning: {len(df):,} rows")
    
    # Remove rows with any validation failures
    df_validated = df[~failed_records_mask].copy()
    
    rows_removed = failed_records_mask.sum()
    print(f"After cleaning: {len(df_validated):,} rows")
    print(f"Removed: {rows_removed:,} invalid records ({rows_removed/total_records*100:.2f}%)")
    
    # Save validated dataset
    df_validated.to_csv('../data/processed/shops_validated_10k.csv', index=False)
    print(f"\n✓ Validated dataset saved to data/processed/shops_validated_10k.csv")
    print(f"  Rows: {len(df_validated):,}")
    print(f"  Columns: {len(df_validated.columns)}")
    
    # Save summary
    summary_df = pd.DataFrame({
        'Total Records': [total_records],
        'Failed Records': [unique_failed_records],
        'Cleaned Records': [len(df_validated)],
        'Data Quality %': [quality_score],
        'Validation Issues': [len(validation_issues)]
    })
    summary_df.to_csv('../output/validation_summary.csv', index=False)
    print(f"✓ Summary saved to output/validation_summary.csv")
    ```

### Your Deliverable

A Jupyter notebook showing:
- Data types properly converted before validation
- All 6 validation rules executed correctly
- Accurate quality score (no double-counting)
- Temp columns cleaned up
- Invalid records removed
- Validation reports saved
- Ready for Day 5 SQL analysis

### Commit Your Work

```
git add notebooks/04_data_validation.ipynb
git add output/validation_report.csv
git add output/validation_summary.csv
git add data/processed/shops_validated_10k.csv
git commit -m "Day 4: Data validation with all corrections applied"
```

### What You Learned

- How to convert data types before validation
- How to validate date logic properly
- How to handle whitespace in text data
- How to count digits vs characters (phone/PIN)
- How to calculate accurate quality scores
- How to clean and track failed records
- The difference between data quality checks

### Tomorrow: Day 5

Tomorrow we'll use the cleaned data for SQL analysis and business statistics.

---

## DAY 5 - SQL Analysis & Business Statistics

**What you're doing:** Using SQL to query the validated data and calculating key business metrics.

**Why it matters:** Analysis transforms clean data into insights. You'll identify patterns that drive business decisions—which shops are thriving, where problems exist, and what opportunities lie ahead.

### Your Tasks

1. **Create a new notebook: `05_sql_analysis_statistics.ipynb`**

   Open Jupyter:
   ```
   jupyter notebook
   ```

2. **Load the validated dataset and set up SQLite database**

   ```python
   import pandas as pd
   import sqlite3
   import numpy as np
   from datetime import datetime
   
   # Load validated data
   df = pd.read_csv('../data/processed/shops_validated_10k.csv')
   
   print("Dataset shape:", df.shape)
   print("Columns:", df.columns.tolist())
   
   # Create SQLite database from the validated data
   conn = sqlite3.connect('../data/shops_analysis.db')
   df.to_sql('shops', conn, if_exists='replace', index=False)
   
   print("✓ Database created: shops_analysis.db")
   ```

3. **Query 1: Basic aggregate statistics**

   ```python
   # Query: Count shops by state
   query1 = """
   SELECT 
       state,
       COUNT(*) as shop_count,
       ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM shops), 2) as percentage
   FROM shops
   GROUP BY state
   ORDER BY shop_count DESC
   LIMIT 10;
   """
   
   result1 = pd.read_sql_query(query1, conn)
   print("="*50)
   print("QUERY 1: Shops by State")
   print("="*50)
   print(result1.to_string(index=False))
   ```

4. **Query 2: Revenue analysis by region**

   ```python
   # Query: Total and average revenue by city (top 15)
   query2 = """
   SELECT 
       city,
       state,
       COUNT(*) as shop_count,
       ROUND(AVG(annual_revenue), 2) as avg_revenue,
       ROUND(SUM(annual_revenue), 2) as total_revenue,
       ROUND(MAX(annual_revenue), 2) as max_revenue,
       ROUND(MIN(annual_revenue), 2) as min_revenue
   FROM shops
   WHERE annual_revenue IS NOT NULL
   GROUP BY city, state
   ORDER BY total_revenue DESC
   LIMIT 15;
   """
   
   result2 = pd.read_sql_query(query2, conn)
   print("\n" + "="*50)
   print("QUERY 2: Revenue Analysis by City (Top 15)")
   print("="*50)
   print(result2.to_string(index=False))
   ```

5. **Query 3: Shop status distribution**

   ```python
   # Query: Breakdown of shop statuses
   query3 = """
   SELECT 
       status,
       COUNT(*) as shop_count,
       ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM shops), 2) as percentage
   FROM shops
   GROUP BY status
   ORDER BY shop_count DESC;
   """
   
   result3 = pd.read_sql_query(query3, conn)
   print("\n" + "="*50)
   print("QUERY 3: Shop Status Distribution")
   print("="*50)
   print(result3.to_string(index=False))
   ```

6. **Query 4: Print volume analysis**

   ```python
   # Query: Print volume statistics
   query4 = """
   SELECT 
       CASE 
           WHEN monthly_print_volume < 1000 THEN 'Low (0-999)'
           WHEN monthly_print_volume < 5000 THEN 'Medium (1k-5k)'
           WHEN monthly_print_volume < 10000 THEN 'High (5k-10k)'
           ELSE 'Very High (10k+)'
       END as volume_segment,
       COUNT(*) as shop_count,
       ROUND(AVG(monthly_print_volume), 0) as avg_volume,
       ROUND(AVG(annual_revenue), 2) as avg_revenue
   FROM shops
   WHERE monthly_print_volume IS NOT NULL
   GROUP BY volume_segment
   ORDER BY avg_volume;
   """
   
   result4 = pd.read_sql_query(query4, conn)
   print("\n" + "="*50)
   print("QUERY 4: Print Volume Segments")
   print("="*50)
   print(result4.to_string(index=False))
   ```

7. **Query 5: High-value customers**

   ```python
   # Query: Top 20 highest revenue shops
   query5 = """
   SELECT 
       business_name,
       city,
       state,
       annual_revenue,
       monthly_print_volume,
       status
   FROM shops
   WHERE annual_revenue IS NOT NULL
   ORDER BY annual_revenue DESC
   LIMIT 20;
   """
   
   result5 = pd.read_sql_query(query5, conn)
   print("\n" + "="*50)
   print("QUERY 5: Top 20 Highest Revenue Shops")
   print("="*50)
   print(result5.to_string(index=False))
   ```

8. **Calculate summary statistics**

   ```python
   print("\n" + "="*50)
   print("SUMMARY STATISTICS")
   print("="*50)
   
   # Overall metrics
   total_shops = len(df)
   active_shops = len(df[df['status'] == 'active'])
   total_revenue = df['annual_revenue'].sum()
   avg_revenue = df['annual_revenue'].mean()
   median_revenue = df['annual_revenue'].median()
   
   print(f"\nTotal Shops: {total_shops:,}")
   print(f"Active Shops: {active_shops:,} ({active_shops/total_shops*100:.1f}%)")
   print(f"Total Annual Revenue: ${total_revenue:,.2f}")
   print(f"Average Revenue per Shop: ${avg_revenue:,.2f}")
   print(f"Median Revenue: ${median_revenue:,.2f}")
   
   # Print volume metrics
   avg_volume = df['monthly_print_volume'].mean()
   total_volume = df['monthly_print_volume'].sum()
   max_volume_shop = df.loc[df['monthly_print_volume'].idxmax()]
   
   print(f"\nTotal Monthly Print Volume: {total_volume:,.0f} prints")
   print(f"Average Monthly Volume per Shop: {avg_volume:,.0f} prints")
   print(f"Highest Volume Shop: {max_volume_shop['business_name']} ({max_volume_shop['monthly_print_volume']:,.0f} prints/month)")
   ```

9. **Create insights summary**

   ```python
   print("\n" + "="*50)
   print("KEY INSIGHTS")
   print("="*50)
   
   # Insight 1: Geographic concentration
   state_diversity = df['state'].nunique()
   top_state = df['state'].value_counts().index[0]
   top_state_pct = df['state'].value_counts().iloc[0] / len(df) * 100
   
   print(f"\n1. GEOGRAPHIC CONCENTRATION:")
   print(f"   - Shops across {state_diversity} states")
   print(f"   - Top state ({top_state}): {top_state_pct:.1f}% of shops")
   
   # Insight 2: Revenue distribution
   high_revenue_threshold = df['annual_revenue'].quantile(0.75)
   high_revenue_shops = len(df[df['annual_revenue'] > high_revenue_threshold])
   
   print(f"\n2. REVENUE DISTRIBUTION:")
   print(f"   - Top 25% of shops: ${high_revenue_threshold:,.0f}+ revenue")
   print(f"   - These {high_revenue_shops} shops generate {df[df['annual_revenue'] > high_revenue_threshold]['annual_revenue'].sum() / total_revenue * 100:.1f}% of total revenue")
   
   # Insight 3: Volume correlation
   corr = df['monthly_print_volume'].corr(df['annual_revenue'])
   print(f"\n3. VOLUME-REVENUE CORRELATION:")
   print(f"   - Correlation coefficient: {corr:.3f}")
   if corr > 0.5:
       print(f"   - Strong positive relationship: Higher volume = Higher revenue")
   elif corr > 0.3:
       print(f"   - Moderate relationship between volume and revenue")
   else:
       print(f"   - Weak relationship between volume and revenue")
   
   # Insight 4: Status breakdown
   print(f"\n4. SHOP STATUS:")
   for status in df['status'].unique():
       count = len(df[df['status'] == status])
       pct = count / len(df) * 100
       print(f"   - {status.title()}: {count:,} shops ({pct:.1f}%)")
   ```

10. **Export query results for visualization**

    ```python
    # Save query results for use in Day 6 visualization
    
    result1.to_csv('../output/analysis_shops_by_state.csv', index=False)
    result2.to_csv('../output/analysis_revenue_by_city.csv', index=False)
    result3.to_csv('../output/analysis_status_distribution.csv', index=False)
    result4.to_csv('../output/analysis_volume_segments.csv', index=False)
    result5.to_csv('../output/analysis_top_revenue_shops.csv', index=False)
    
    print("\n✓ All query results exported to output/")
    ```

11. **Close database connection**

    ```python
    conn.close()
    print("✓ Database connection closed")
    ```

### Your Deliverable

A Jupyter notebook showing:
- SQLite database created from validated data
- 5 SQL queries with results
- Summary statistics calculated
- Key business insights identified
- Query results exported to CSV files
- Analysis complete and ready for visualization

### Commit Your Work

```
git add notebooks/05_sql_analysis_statistics.ipynb
git add output/analysis_*.csv
git add data/shops_analysis.db
git commit -m "Day 5: SQL analysis and business statistics"
```

### What You Learned

- How to write SQL queries for data analysis
- How to calculate aggregate statistics
- How to identify business insights from data
- How to segment customers by behavior
- How to correlate multiple metrics
- How to export analysis results for visualization

### Tomorrow: Day 6

Tomorrow we'll create visual charts and dashboards from these query results using matplotlib and seaborn.


---

## DAY 6 - Data Visualization & Charts

**What you're doing:** Creating visual charts and dashboards from your analysis data using matplotlib and seaborn.

**Why it matters:** Visualizations tell stories that raw numbers can't. A good chart reveals patterns instantly, communicates findings to non-technical stakeholders, and helps you spot trends you'd miss in spreadsheets.

### Your Tasks

1. **Create a new notebook: `06_data_visualization.ipynb`**

   Open Jupyter:
   ```
   jupyter notebook
   ```

2. **Load query results from Day 5**

   ```python
   import pandas as pd
   import matplotlib.pyplot as plt
   import seaborn as sns
   import numpy as np
   
   # Set style for all charts
   sns.set_style("whitegrid")
   plt.rcParams['figure.figsize'] = (14, 8)
   
   # Load analysis results from Day 5
   shops_by_state = pd.read_csv('../output/analysis_shops_by_state.csv')
   revenue_by_city = pd.read_csv('../output/analysis_revenue_by_city.csv')
   status_dist = pd.read_csv('../output/analysis_status_distribution.csv')
   volume_segments = pd.read_csv('../output/analysis_volume_segments.csv')
   top_revenue = pd.read_csv('../output/analysis_top_revenue_shops.csv')
   
   print("✓ All analysis files loaded successfully")
   ```

3. **Chart 1: Shops by State (Bar Chart)**

   ```python
   # Create a bar chart showing shop distribution by state
   fig, ax = plt.subplots(figsize=(14, 6))
   
   shops_by_state_sorted = shops_by_state.sort_values('shop_count', ascending=False)
   
   bars = ax.bar(shops_by_state_sorted['state'], 
                 shops_by_state_sorted['shop_count'],
                 color='steelblue',
                 edgecolor='navy',
                 alpha=0.8)
   
   # Add value labels on top of bars
   for bar in bars:
       height = bar.get_height()
       ax.text(bar.get_x() + bar.get_width()/2., height,
               f'{int(height):,}',
               ha='center', va='bottom', fontsize=9)
   
   ax.set_xlabel('State', fontsize=12, fontweight='bold')
   ax.set_ylabel('Number of Shops', fontsize=12, fontweight='bold')
   ax.set_title('Shop Distribution by State (Top 15)', fontsize=14, fontweight='bold')
   ax.grid(axis='y', alpha=0.3)
   
   plt.xticks(rotation=45, ha='right')
   plt.tight_layout()
   plt.savefig('../output/chart_01_shops_by_state.png', dpi=300, bbox_inches='tight')
   print("✓ Chart saved: chart_01_shops_by_state.png")
   plt.show()
   ```

4. **Chart 2: Revenue Distribution by City (Top 10)**

   ```python
   # Create a horizontal bar chart for top cities by revenue
   fig, ax = plt.subplots(figsize=(12, 8))
   
   top_cities = revenue_by_city.head(10).sort_values('total_revenue', ascending=True)
   
   bars = ax.barh(top_cities['city'] + ', ' + top_cities['state'],
                  top_cities['total_revenue'],
                  color='coral',
                  edgecolor='darkred',
                  alpha=0.8)
   
   # Add value labels
   for i, bar in enumerate(bars):
       width = bar.get_width()
       ax.text(width, bar.get_y() + bar.get_height()/2.,
               f'${width:,.0f}',
               ha='left', va='center', fontsize=9, fontweight='bold')
   
   ax.set_xlabel('Total Revenue ($)', fontsize=12, fontweight='bold')
   ax.set_ylabel('City, State', fontsize=12, fontweight='bold')
   ax.set_title('Top 10 Cities by Total Annual Revenue', fontsize=14, fontweight='bold')
   ax.grid(axis='x', alpha=0.3)
   
   plt.tight_layout()
   plt.savefig('../output/chart_02_revenue_by_city.png', dpi=300, bbox_inches='tight')
   print("✓ Chart saved: chart_02_revenue_by_city.png")
   plt.show()
   ```

5. **Chart 3: Shop Status Distribution (Pie Chart)**

   ```python
   # Create a pie chart showing status distribution
   fig, ax = plt.subplots(figsize=(10, 8))
   
   colors = ['#2ecc71', '#e74c3c', '#f39c12', '#9b59b6']
   explode = (0.05, 0, 0, 0)  # Explode the largest slice slightly
   
   wedges, texts, autotexts = ax.pie(status_dist['shop_count'],
                                      labels=status_dist['status'].str.title(),
                                      autopct='%1.1f%%',
                                      startangle=90,
                                      colors=colors,
                                      explode=explode,
                                      textprops={'fontsize': 11, 'fontweight': 'bold'})
   
   # Enhance text
   for autotext in autotexts:
       autotext.set_color('white')
       autotext.set_fontsize(10)
       autotext.set_fontweight('bold')
   
   ax.set_title('Shop Status Distribution', fontsize=14, fontweight='bold', pad=20)
   
   # Add legend with counts
   legend_labels = [f"{status.title()}: {count:,}" 
                    for status, count in zip(status_dist['status'], status_dist['shop_count'])]
   ax.legend(legend_labels, loc='upper left', bbox_to_anchor=(1, 1))
   
   plt.tight_layout()
   plt.savefig('../output/chart_03_status_distribution.png', dpi=300, bbox_inches='tight')
   print("✓ Chart saved: chart_03_status_distribution.png")
   plt.show()
   ```

6. **Chart 4: Print Volume Segments (Grouped Bar Chart)**

   ```python
   # Create a grouped bar chart for volume segments
   fig, ax = plt.subplots(figsize=(12, 6))
   
   x = np.arange(len(volume_segments))
   width = 0.35
   
   bars1 = ax.bar(x - width/2, volume_segments['shop_count'],
                  width, label='Shop Count', color='skyblue', edgecolor='navy', alpha=0.8)
   
   # Create second y-axis for revenue
   ax2 = ax.twinx()
   bars2 = ax2.plot(x, volume_segments['avg_revenue'],
                    marker='o', color='red', linewidth=2, markersize=8, label='Avg Revenue')
   
   ax.set_xlabel('Volume Segment', fontsize=12, fontweight='bold')
   ax.set_ylabel('Number of Shops', fontsize=12, fontweight='bold', color='navy')
   ax2.set_ylabel('Average Revenue ($)', fontsize=12, fontweight='bold', color='red')
   
   ax.set_title('Print Volume Segments: Shop Count vs Average Revenue', fontsize=14, fontweight='bold')
   ax.set_xticks(x)
   ax.set_xticklabels(volume_segments['volume_segment'], rotation=15, ha='right')
   
   ax.tick_params(axis='y', labelcolor='navy')
   ax2.tick_params(axis='y', labelcolor='red')
   ax.grid(axis='y', alpha=0.3)
   
   # Add combined legend
   lines1, labels1 = ax.get_legend_handles_labels()
   lines2, labels2 = ax2.get_legend_handles_labels()
   ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
   
   plt.tight_layout()
   plt.savefig('../output/chart_04_volume_segments.png', dpi=300, bbox_inches='tight')
   print("✓ Chart saved: chart_04_volume_segments.png")
   plt.show()
   ```

7. **Chart 5: Top 15 Revenue Shops (Horizontal Bar with Color Gradient)**

   ```python
   # Create a horizontal bar chart for top 15 revenue shops
   fig, ax = plt.subplots(figsize=(12, 10))
   
   top_15 = top_revenue.head(15).sort_values('annual_revenue', ascending=True)
   
   # Create color gradient from low to high
   colors_gradient = plt.cm.Greens(np.linspace(0.4, 0.9, len(top_15)))
   
   bars = ax.barh(top_15['business_name'],
                  top_15['annual_revenue'],
                  color=colors_gradient,
                  edgecolor='darkgreen',
                  alpha=0.85)
   
   # Add value labels
   for i, bar in enumerate(bars):
       width = bar.get_width()
       ax.text(width, bar.get_y() + bar.get_height()/2.,
               f'${width:,.0f}',
               ha='left', va='center', fontsize=9, fontweight='bold')
   
   ax.set_xlabel('Annual Revenue ($)', fontsize=12, fontweight='bold')
   ax.set_title('Top 15 Highest Revenue Shops', fontsize=14, fontweight='bold')
   ax.grid(axis='x', alpha=0.3)
   
   plt.tight_layout()
   plt.savefig('../output/chart_05_top_revenue_shops.png', dpi=300, bbox_inches='tight')
   print("✓ Chart saved: chart_05_top_revenue_shops.png")
   plt.show()
   ```

8. **Chart 6: Revenue Distribution (Histogram with KDE)**

   ```python
   # Load full dataset for distribution analysis
   df_full = pd.read_csv('../data/processed/shops_validated_10k.csv')
   
   fig, ax = plt.subplots(figsize=(12, 6))
   
   # Create histogram with KDE
   df_full['annual_revenue'].hist(bins=50, ax=ax, color='lightblue',
                                   edgecolor='black', alpha=0.7)
   
   # Add KDE curve
   df_full['annual_revenue'].plot(kind='density', ax=ax, secondary_y=False,
                                  color='red', linewidth=2, label='Distribution Curve')
   
   ax.set_xlabel('Annual Revenue ($)', fontsize=12, fontweight='bold')
   ax.set_ylabel('Number of Shops', fontsize=12, fontweight='bold')
   ax.set_title('Revenue Distribution Across All Shops', fontsize=14, fontweight='bold')
   ax.grid(axis='y', alpha=0.3)
   ax.legend()
   
   plt.tight_layout()
   plt.savefig('../output/chart_06_revenue_distribution.png', dpi=300, bbox_inches='tight')
   print("✓ Chart saved: chart_06_revenue_distribution.png")
   plt.show()
   ```

9. **Chart 7: Print Volume vs Revenue Scatter Plot**

   ```python
   # Create scatter plot showing correlation
   fig, ax = plt.subplots(figsize=(12, 8))
   
   # Create scatter plot with color coding by status
   for status in df_full['status'].unique():
       subset = df_full[df_full['status'] == status]
       ax.scatter(subset['monthly_print_volume'],
                 subset['annual_revenue'],
                 label=status.title(),
                 alpha=0.6,
                 s=50,
                 edgecolors='black',
                 linewidth=0.5)
   
   # Add trend line
   z = np.polyfit(df_full['monthly_print_volume'].dropna(), 
                  df_full['annual_revenue'].dropna(), 1)
   p = np.poly1d(z)
   x_trend = np.linspace(df_full['monthly_print_volume'].min(),
                        df_full['monthly_print_volume'].max(), 100)
   ax.plot(x_trend, p(x_trend), "r--", linewidth=2, label='Trend Line')
   
   ax.set_xlabel('Monthly Print Volume', fontsize=12, fontweight='bold')
   ax.set_ylabel('Annual Revenue ($)', fontsize=12, fontweight='bold')
   ax.set_title('Print Volume vs Annual Revenue (with Trend Line)', fontsize=14, fontweight='bold')
   ax.legend(loc='upper left')
   ax.grid(True, alpha=0.3)
   
   plt.tight_layout()
   plt.savefig('../output/chart_07_volume_vs_revenue.png', dpi=300, bbox_inches='tight')
   print("✓ Chart saved: chart_07_volume_vs_revenue.png")
   plt.show()
   ```

10. **Create a summary visualization dashboard**

    ```python
    # Create a multi-panel dashboard
    fig = plt.figure(figsize=(16, 12))
    gs = fig.add_gridspec(3, 2, hspace=0.3, wspace=0.3)
    
    # Panel 1: Status pie
    ax1 = fig.add_subplot(gs[0, 0])
    colors = ['#2ecc71', '#e74c3c', '#f39c12', '#9b59b6']
    ax1.pie(status_dist['shop_count'], labels=status_dist['status'].str.title(),
            autopct='%1.1f%%', colors=colors, startangle=90)
    ax1.set_title('Shop Status Distribution', fontweight='bold')
    
    # Panel 2: Top states
    ax2 = fig.add_subplot(gs[0, 1])
    top_5_states = shops_by_state.head(5).sort_values('shop_count', ascending=True)
    ax2.barh(top_5_states['state'], top_5_states['shop_count'],
             color='steelblue', edgecolor='navy', alpha=0.8)
    ax2.set_xlabel('Shop Count', fontweight='bold')
    ax2.set_title('Top 5 States by Shop Count', fontweight='bold')
    ax2.grid(axis='x', alpha=0.3)
    
    # Panel 3: Revenue distribution histogram
    ax3 = fig.add_subplot(gs[1, :])
    ax3.hist(df_full['annual_revenue'], bins=40, color='lightblue',
             edgecolor='black', alpha=0.7)
    ax3.set_xlabel('Annual Revenue ($)', fontweight='bold')
    ax3.set_ylabel('Number of Shops', fontweight='bold')
    ax3.set_title('Revenue Distribution', fontweight='bold')
    ax3.grid(axis='y', alpha=0.3)
    
    # Panel 4: Volume segments
    ax4 = fig.add_subplot(gs[2, 0])
    ax4.bar(range(len(volume_segments)), volume_segments['shop_count'],
            color='coral', edgecolor='darkred', alpha=0.8)
    ax4.set_xticks(range(len(volume_segments)))
    ax4.set_xticklabels(volume_segments['volume_segment'], rotation=15, ha='right')
    ax4.set_ylabel('Shop Count', fontweight='bold')
    ax4.set_title('Volume Segments', fontweight='bold')
    ax4.grid(axis='y', alpha=0.3)
    
    # Panel 5: Volume vs Revenue scatter
    ax5 = fig.add_subplot(gs[2, 1])
    for status in df_full['status'].unique():
        subset = df_full[df_full['status'] == status]
        ax5.scatter(subset['monthly_print_volume'],
                   subset['annual_revenue'],
                   label=status.title(), alpha=0.6, s=30)
    ax5.set_xlabel('Monthly Print Volume', fontweight='bold')
    ax5.set_ylabel('Annual Revenue ($)', fontweight='bold')
    ax5.set_title('Volume vs Revenue', fontweight='bold')
    ax5.legend(fontsize=8)
    ax5.grid(True, alpha=0.3)
    
    fig.suptitle('Print Shop Analytics Dashboard', fontsize=16, fontweight='bold', y=0.995)
    
    plt.savefig('../output/dashboard_full_analytics.png', dpi=300, bbox_inches='tight')
    print("✓ Dashboard saved: dashboard_full_analytics.png")
    plt.show()
    ```

11. **Create a summary report**

    ```python
    print("\n" + "="*60)
    print("VISUALIZATION SUMMARY")
    print("="*60)
    
    chart_files = [
        'chart_01_shops_by_state.png',
        'chart_02_revenue_by_city.png',
        'chart_03_status_distribution.png',
        'chart_04_volume_segments.png',
        'chart_05_top_revenue_shops.png',
        'chart_06_revenue_distribution.png',
        'chart_07_volume_vs_revenue.png',
        'dashboard_full_analytics.png'
    ]
    
    print("\n✓ Charts created:")
    for i, chart in enumerate(chart_files, 1):
        print(f"  {i}. {chart}")
    
    print("\n✓ All charts saved to: output/")
    print("\nThese visualizations show:")
    print("  • Geographic distribution of shops")
    print("  • Revenue patterns by location and volume")
    print("  • Shop status breakdown")
    print("  • Strong correlation between volume and revenue")
    print("  • Top performing shops and cities")
    print("\nNext: Use these charts in your Excel dashboard presentation!")
    ```

### Your Deliverable

A Jupyter notebook showing:
- 7 individual charts (PNG format, high resolution)
- 1 comprehensive analytics dashboard
- All charts properly labeled with titles and axes
- Color-coded visualizations for easy interpretation
- All charts saved to `output/` folder

### Commit Your Work

```
git add notebooks/06_data_visualization.ipynb
git add output/chart_*.png
git add output/dashboard_*.png
git commit -m "Day 6: Data visualization and dashboard charts"
```

### What You Learned

- How to create publication-quality charts with matplotlib
- How to use seaborn for styling and enhanced visuals
- How to create multi-panel dashboards
- How to add trend lines and distribution curves
- How to color-code data by category
- How to export high-resolution charts (DPI 300)
- How to tell stories with data visualization

### Tomorrow: Day 7

Tomorrow we'll create an interactive Excel dashboard that brings all these insights together in a professional presentation format.


---

## DAY 7 - Excel Dashboard & Final Presentation

**What you're doing:** Creating a professional Excel dashboard that combines all your analysis, charts, and insights into an executive-ready presentation.

**Why it matters:** Technical analysis is meaningless if stakeholders can't understand it. An Excel dashboard turns your Python work into a business tool that anyone can use and understand. This is your portfolio piece.

### Your Tasks

1. **Create a new notebook: `07_excel_dashboard.ipynb`**

   Open Jupyter:
   ```
   jupyter notebook
   ```

2. **Load all analysis results**

   ```python
   import pandas as pd
   import openpyxl
   from openpyxl import Workbook
   from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
   from openpyxl.chart import BarChart, PieChart, LineChart, Reference
   from openpyxl.utils.dataframe import dataframe_to_rows
   from openpyxl.drawing.image import Image
   import os
   
   print("="*60)
   print("EXCEL DASHBOARD CREATION")
   print("="*60)
   
   # Load validated data
   df = pd.read_csv('../data/processed/shops_validated_10k.csv')
   
   # Load analysis results
   shops_by_state = pd.read_csv('../output/analysis_shops_by_state.csv')
   revenue_by_city = pd.read_csv('../output/analysis_revenue_by_city.csv')
   status_dist = pd.read_csv('../output/analysis_status_distribution.csv')
   volume_segments = pd.read_csv('../output/analysis_volume_segments.csv')
   
   print(f"✓ Loaded {len(df):,} validated shop records")
   print(f"✓ Loaded {len(shops_by_state)} state summaries")
   print(f"✓ Loaded {len(revenue_by_city)} city summaries")
   ```

3. **Create Excel workbook with multiple sheets**

   ```python
   # Create new workbook
   wb = Workbook()
   
   # Remove default sheet
   wb.remove(wb.active)
   
   # Create sheets
   ws_summary = wb.create_sheet("Executive Summary", 0)
   ws_data = wb.create_sheet("Raw Data", 1)
   ws_state = wb.create_sheet("By State", 2)
   ws_city = wb.create_sheet("By City", 3)
   ws_status = wb.create_sheet("Status Analysis", 4)
   ws_volume = wb.create_sheet("Volume Segments", 5)
   ws_charts = wb.create_sheet("Visualizations", 6)
   
   print("✓ Created 7 worksheets")
   ```

4. **Executive Summary Sheet (Professional Header)**

   ```python
   # Title and header styling
   ws_summary['A1'] = 'PRINT SHOP DATA ANALYSIS'
   ws_summary['A1'].font = Font(name='Arial', size=24, bold=True, color='FFFFFF')
   ws_summary['A1'].fill = PatternFill(start_color='1F4E78', end_color='1F4E78', fill_type='solid')
   ws_summary['A1'].alignment = Alignment(horizontal='center', vertical='center')
   ws_summary.merge_cells('A1:F1')
   ws_summary.row_dimensions[1].height = 40
   
   # Subtitle
   ws_summary['A2'] = f'Data Quality Project - {len(df):,} Shop Records Analyzed'
   ws_summary['A2'].font = Font(name='Arial', size=12, italic=True)
   ws_summary['A2'].alignment = Alignment(horizontal='center')
   ws_summary.merge_cells('A2:F2')
   ws_summary.row_dimensions[2].height = 25
   
   # Key metrics header
   ws_summary['A4'] = 'KEY METRICS'
   ws_summary['A4'].font = Font(name='Arial', size=14, bold=True, color='1F4E78')
   ws_summary['A4'].alignment = Alignment(horizontal='left')
   ws_summary.row_dimensions[4].height = 25
   
   # Calculate key metrics
   total_shops = len(df)
   total_revenue = df['annual_revenue'].sum()
   avg_revenue = df['annual_revenue'].mean()
   total_volume = df['monthly_print_volume'].sum()
   active_shops = len(df[df['status'] == 'active'])
   states_covered = df['state'].nunique()
   
   # Metrics data
   metrics = [
       ['Total Shops', f'{total_shops:,}'],
       ['Active Shops', f'{active_shops:,} ({active_shops/total_shops*100:.1f}%)'],
       ['Total Annual Revenue', f'${total_revenue:,.2f}'],
       ['Average Revenue/Shop', f'${avg_revenue:,.2f}'],
       ['Total Monthly Print Volume', f'{total_volume:,.0f} prints'],
       ['States Covered', f'{states_covered}']
   ]
   
   # Write metrics with styling
   row = 5
   for metric, value in metrics:
       ws_summary[f'A{row}'] = metric
       ws_summary[f'A{row}'].font = Font(name='Arial', size=11, bold=True)
       ws_summary[f'A{row}'].fill = PatternFill(start_color='D9E1F2', end_color='D9E1F2', fill_type='solid')
       
       ws_summary[f'C{row}'] = value
       ws_summary[f'C{row}'].font = Font(name='Arial', size=11, color='1F4E78', bold=True)
       ws_summary[f'C{row}'].alignment = Alignment(horizontal='right')
       
       row += 1
   
   # Column widths
   ws_summary.column_dimensions['A'].width = 25
   ws_summary.column_dimensions['C'].width = 30
   
   print("✓ Executive Summary created")
   ```

5. **Add Top Insights Section**

   ```python
   # Insights header
   ws_summary['A12'] = 'TOP INSIGHTS'
   ws_summary['A12'].font = Font(name='Arial', size=14, bold=True, color='1F4E78')
   ws_summary.row_dimensions[12].height = 25
   
   # Calculate insights
   top_state = shops_by_state.iloc[0]
   top_city = revenue_by_city.iloc[0]
   high_volume_shops = len(df[df['monthly_print_volume'] > 10000])
   
   insights = [
       f"1. Geographic Concentration: {top_state['state']} leads with {top_state['shop_count']} shops ({top_state['percentage']}%)",
       f"2. Revenue Leader: {top_city['city']}, {top_city['state']} generates ${top_city['total_revenue']:,.0f} annually",
       f"3. High-Volume Operators: {high_volume_shops} shops print over 10,000 pages/month",
       f"4. Market Penetration: Active presence across {states_covered} states",
       f"5. Average Shop Size: {avg_revenue/1000:.0f}K annual revenue with {df['monthly_print_volume'].mean():,.0f} prints/month"
   ]
   
   row = 13
   for insight in insights:
       ws_summary[f'A{row}'] = insight
       ws_summary[f'A{row}'].font = Font(name='Arial', size=10)
       ws_summary[f'A{row}'].alignment = Alignment(wrap_text=True, vertical='top')
       ws_summary.row_dimensions[row].height = 30
       row += 1
   
   ws_summary.merge_cells(f'A13:F17')
   
   print("✓ Insights section added")
   ```

6. **Raw Data Sheet with Formatting**

   ```python
   # Add header
   ws_data['A1'] = 'VALIDATED SHOP DATA'
   ws_data['A1'].font = Font(name='Arial', size=14, bold=True, color='FFFFFF')
   ws_data['A1'].fill = PatternFill(start_color='1F4E78', end_color='1F4E78', fill_type='solid')
   ws_data.row_dimensions[1].height = 25
   
   # Write dataframe
   for r_idx, row in enumerate(dataframe_to_rows(df.head(1000), index=False, header=True), 3):
       for c_idx, value in enumerate(row, 1):
           cell = ws_data.cell(row=r_idx, column=c_idx, value=value)
           
           # Header row styling
           if r_idx == 3:
               cell.font = Font(name='Arial', size=10, bold=True, color='FFFFFF')
               cell.fill = PatternFill(start_color='4472C4', end_color='4472C4', fill_type='solid')
               cell.alignment = Alignment(horizontal='center', vertical='center')
           else:
               cell.font = Font(name='Arial', size=9)
               cell.alignment = Alignment(horizontal='left', vertical='top')
   
   # Auto-fit columns
   for column in ws_data.columns:
       max_length = 0
       column_letter = column[0].column_letter
       for cell in column:
           if cell.value:
               max_length = max(max_length, len(str(cell.value)))
       ws_data.column_dimensions[column_letter].width = min(max_length + 2, 50)
   
   print(f"✓ Raw data sheet created (first 1000 records)")
   ```

7. **State Analysis Sheet with Bar Chart**

   ```python
   # Write state data
   ws_state['A1'] = 'SHOPS BY STATE'
   ws_state['A1'].font = Font(name='Arial', size=14, bold=True, color='FFFFFF')
   ws_state['A1'].fill = PatternFill(start_color='1F4E78', end_color='1F4E78', fill_type='solid')
   ws_state.merge_cells('A1:D1')
   ws_state.row_dimensions[1].height = 25
   
   # Write data with headers
   for r_idx, row in enumerate(dataframe_to_rows(shops_by_state, index=False, header=True), 3):
       for c_idx, value in enumerate(row, 1):
           cell = ws_state.cell(row=r_idx, column=c_idx, value=value)
           if r_idx == 3:
               cell.font = Font(bold=True, color='FFFFFF')
               cell.fill = PatternFill(start_color='4472C4', end_color='4472C4', fill_type='solid')
   
   # Create bar chart
   chart = BarChart()
   chart.title = "Shop Distribution by State"
   chart.x_axis.title = "State"
   chart.y_axis.title = "Number of Shops"
   
   data = Reference(ws_state, min_col=2, min_row=3, max_row=3+len(shops_by_state))
   cats = Reference(ws_state, min_col=1, min_row=4, max_row=3+len(shops_by_state))
   
   chart.add_data(data, titles_from_data=True)
   chart.set_categories(cats)
   chart.height = 12
   chart.width = 20
   
   ws_state.add_chart(chart, "F3")
   
   print("✓ State analysis sheet with chart created")
   ```

8. **City Revenue Sheet with Top 10**

   ```python
   # Write city data
   ws_city['A1'] = 'TOP CITIES BY REVENUE'
   ws_city['A1'].font = Font(name='Arial', size=14, bold=True, color='FFFFFF')
   ws_city['A1'].fill = PatternFill(start_color='1F4E78', end_color='1F4E78', fill_type='solid')
   ws_city.merge_cells('A1:E1')
   ws_city.row_dimensions[1].height = 25
   
   # Write top 10 cities
   top_10_cities = revenue_by_city.head(10)
   for r_idx, row in enumerate(dataframe_to_rows(top_10_cities, index=False, header=True), 3):
       for c_idx, value in enumerate(row, 1):
           cell = ws_city.cell(row=r_idx, column=c_idx, value=value)
           if r_idx == 3:
               cell.font = Font(bold=True, color='FFFFFF')
               cell.fill = PatternFill(start_color='4472C4', end_color='4472C4', fill_type='solid')
           
           # Format revenue columns
           if c_idx in [4, 5, 6, 7] and r_idx > 3:
               cell.number_format = '$#,##0.00'
   
   # Create horizontal bar chart
   chart = BarChart()
   chart.type = "bar"
   chart.title = "Top 10 Cities by Total Revenue"
   chart.y_axis.title = "City"
   chart.x_axis.title = "Total Revenue ($)"
   
   data = Reference(ws_city, min_col=5, min_row=3, max_row=13)
   cats = Reference(ws_city, min_col=1, min_row=4, max_row=13)
   
   chart.add_data(data, titles_from_data=True)
   chart.set_categories(cats)
   chart.height = 12
   chart.width = 20
   
   ws_city.add_chart(chart, "G3")
   
   print("✓ City revenue sheet with chart created")
   ```

9. **Status Distribution with Pie Chart**

   ```python
   # Write status data
   ws_status['A1'] = 'SHOP STATUS BREAKDOWN'
   ws_status['A1'].font = Font(name='Arial', size=14, bold=True, color='FFFFFF')
   ws_status['A1'].fill = PatternFill(start_color='1F4E78', end_color='1F4E78', fill_type='solid')
   ws_status.merge_cells('A1:C1')
   ws_status.row_dimensions[1].height = 25
   
   for r_idx, row in enumerate(dataframe_to_rows(status_dist, index=False, header=True), 3):
       for c_idx, value in enumerate(row, 1):
           cell = ws_status.cell(row=r_idx, column=c_idx, value=value)
           if r_idx == 3:
               cell.font = Font(bold=True, color='FFFFFF')
               cell.fill = PatternFill(start_color='4472C4', end_color='4472C4', fill_type='solid')
   
   # Create pie chart
   chart = PieChart()
   chart.title = "Shop Status Distribution"
   
   data = Reference(ws_status, min_col=2, min_row=3, max_row=3+len(status_dist))
   labels = Reference(ws_status, min_col=1, min_row=4, max_row=3+len(status_dist))
   
   chart.add_data(data, titles_from_data=True)
   chart.set_categories(labels)
   chart.height = 12
   chart.width = 16
   
   ws_status.add_chart(chart, "E3")
   
   print("✓ Status distribution sheet with pie chart created")
   ```

10. **Volume Segments Analysis**

    ```python
    # Write volume segment data
    ws_volume['A1'] = 'PRINT VOLUME SEGMENTS'
    ws_volume['A1'].font = Font(name='Arial', size=14, bold=True, color='FFFFFF')
    ws_volume['A1'].fill = PatternFill(start_color='1F4E78', end_color='1F4E78', fill_type='solid')
    ws_volume.merge_cells('A1:D1')
    ws_volume.row_dimensions[1].height = 25
    
    for r_idx, row in enumerate(dataframe_to_rows(volume_segments, index=False, header=True), 3):
        for c_idx, value in enumerate(row, 1):
            cell = ws_volume.cell(row=r_idx, column=c_idx, value=value)
            if r_idx == 3:
                cell.font = Font(bold=True, color='FFFFFF')
                cell.fill = PatternFill(start_color='4472C4', end_color='4472C4', fill_type='solid')
            
            # Format numeric columns
            if c_idx in [2, 3, 4] and r_idx > 3:
                if c_idx == 4:
                    cell.number_format = '$#,##0.00'
                else:
                    cell.number_format = '#,##0'
    
    # Create combo chart
    chart = BarChart()
    chart.title = "Shop Count by Volume Segment"
    chart.x_axis.title = "Volume Segment"
    chart.y_axis.title = "Shop Count"
    
    data = Reference(ws_volume, min_col=2, min_row=3, max_row=3+len(volume_segments))
    cats = Reference(ws_volume, min_col=1, min_row=4, max_row=3+len(volume_segments))
    
    chart.add_data(data, titles_from_data=True)
    chart.set_categories(cats)
    chart.height = 12
    chart.width = 20
    
    ws_volume.add_chart(chart, "F3")
    
    print("✓ Volume segments sheet with chart created")
    ```

11. **Insert PNG Charts from Day 6**

    ```python
    # Insert saved charts as images
    chart_files = [
        ('chart_01_shops_by_state.png', 'A3'),
        ('chart_03_status_distribution.png', 'A25'),
        ('chart_07_volume_vs_revenue.png', 'K3')
    ]
    
    for filename, position in chart_files:
        filepath = f'../output/{filename}'
        if os.path.exists(filepath):
            img = Image(filepath)
            img.width = 480
            img.height = 320
            ws_charts.add_image(img, position)
            print(f"  ✓ Inserted {filename}")
    
    ws_charts['A1'] = 'DATA VISUALIZATIONS'
    ws_charts['A1'].font = Font(name='Arial', size=14, bold=True, color='FFFFFF')
    ws_charts['A1'].fill = PatternFill(start_color='1F4E78', end_color='1F4E78', fill_type='solid')
    ws_charts.merge_cells('A1:T1')
    
    print("✓ Visualizations sheet created with embedded charts")
    ```

12. **Save Excel Dashboard**

    ```python
    # Save workbook
    output_file = '../output/PrintShop_Analysis_Dashboard.xlsx'
    wb.save(output_file)
    
    file_size = os.path.getsize(output_file) / 1024  # KB
    
    print("\n" + "="*60)
    print("DASHBOARD CREATION COMPLETE")
    print("="*60)
    print(f"✓ File: {output_file}")
    print(f"✓ Size: {file_size:.1f} KB")
    print(f"✓ Sheets: 7 (Summary, Raw Data, State, City, Status, Volume, Charts)")
    print(f"✓ Records: {len(df):,} shops")
    print(f"✓ Charts: 5 Excel native + 3 embedded PNG visualizations")
    print("\nYour dashboard is ready for presentation!")
    ```

### Your Deliverable

A professional Excel dashboard (`PrintShop_Analysis_Dashboard.xlsx`) containing:
- Executive Summary with key metrics and insights
- Raw validated data (first 1000 records)
- State-by-state analysis with bar chart
- Top 10 cities by revenue with horizontal bar chart
- Shop status distribution with pie chart
- Volume segments analysis with chart
- Embedded high-resolution visualizations from Day 6

### Commit Your Work

```
git add notebooks/07_excel_dashboard.ipynb
git add output/PrintShop_Analysis_Dashboard.xlsx
git commit -m "Day 7: Excel dashboard creation - final deliverable"
```

### What You Learned

- How to create professional Excel workbooks with Python
- How to style cells, fonts, colors, and borders
- How to add Excel native charts (bar, pie, line)
- How to embed external images into Excel
- How to format numbers as currency and percentages
- How to merge cells and create headers
- How to auto-fit columns for readability
- How to create multi-sheet workbooks
- How to build executive-ready dashboards

### Congratulations! 🎉

**You've completed the 7-day Data Analytics Training Program!**

You now have:
- ✅ A clean, validated dataset
- ✅ Comprehensive data quality analysis
- ✅ SQL queries and statistical insights
- ✅ Professional visualizations (charts, graphs, dashboards)
- ✅ An executive Excel dashboard
- ✅ A complete portfolio project

**What's Next:**
1. Review your entire Git history: `git log --oneline`
2. Push to GitHub: `git push origin main`
3. Share your dashboard with stakeholders
4. Add this project to your resume/portfolio
5. Apply these skills to your next data project!

**Skills Acquired:**
- Python data manipulation (pandas, numpy)
- Data profiling and quality assessment
- Data cleaning (nulls, duplicates, formatting)
- Business rule validation
- SQL querying and aggregation
- Statistical analysis
- Data visualization (matplotlib, seaborn)
- Excel automation (openpyxl)
- Git version control
- Project documentation

**Your portfolio now demonstrates:**
- End-to-end data pipeline construction
- Real-world data quality problem-solving
- Business intelligence and analytics
- Professional presentation skills
- Technical communication
- Attention to detail and data integrity

Well done! 🚀
