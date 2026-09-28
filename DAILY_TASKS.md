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

## DAYS 4-7 (Coming Soon)

Check back tomorrow for Day 4 tasks.
