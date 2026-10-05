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
