# Your Daily Tasks

I update this file each morning with your tasks for the day. Check back here every morning to see what you need to work on.

You're working with real production data from our system. Two CSV files with quality problems you need to identify and fix. By the end of this week, you'll have completed a full data engineering project.

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

**LibreOffice Calc** - https://www.libreoffice.org
- Or use Excel if you have it

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

Download these files from this repository:
- `shops_raw_data_10k.csv`
- `shops_raw_data_25k.csv`

Put them in your `data/raw/` folder.

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

5. **Do the same for the 25k dataset**

   ```python
   df_25k = pd.read_csv('../data/raw/shops_raw_data_25k.csv')
   print(df_25k.head(10))
   print(df_25k.info())
   print(df_25k.isnull().sum())
   ```

6. **Save your notebook**

   Name it clearly: `01_data_profiling.ipynb`

### Your Deliverable

A Jupyter notebook showing:
- Both datasets loaded
- First 10 rows of each
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
- The datasets have different numbers of rows but similar columns
- Some values might look odd or inconsistent

That's what we're going to fix over the next week.

---

## DAY 2 - Dive Deeper Into Data Quality

**What you're doing:** Finding the specific problems in your data.

**Why it matters:** You can't fix what you don't understand. Today you learn what's broken.

### Your Tasks

1. **Create a new notebook: `02_data_quality_check.ipynb`**

2. **Load both datasets again**

   ```python
   import pandas as pd
   
   df_10k = pd.read_csv('../data/raw/shops_raw_data_10k.csv')
   df_25k = pd.read_csv('../data/raw/shops_raw_data_25k.csv')
   ```

3. **Look for duplicates**

   ```python
   # Check for exact duplicates
   print("10k duplicates:", df_10k.duplicated().sum())
   print("25k duplicates:", df_25k.duplicated().sum())
   
   # Check for duplicates on specific columns (like email or phone)
   print("10k duplicate emails:", df_10k.duplicated(subset=['email']).sum())
   print("25k duplicate emails:", df_25k.duplicated(subset=['email']).sum())
   ```

4. **Analyze null values in detail**

   ```python
   # Show which rows have the most nulls
   null_counts = df_10k.isnull().sum()
   print(null_counts[null_counts > 0])
   
   # Show percentage of missing data per column
   missing_percent = (df_10k.isnull().sum() / len(df_10k)) * 100
   print(missing_percent[missing_percent > 0])
   ```

5. **Check for inconsistent formats**

   Pick a few columns and look at unique values:

   ```python
   # Phone numbers
   print("Sample phone numbers:")
   print(df_10k['phone'].head(20))
   print("Unique phone formats:", df_10k['phone'].nunique())
   
   # Cities
   print("Sample cities:")
   print(df_10k['city'].value_counts().head(20))
   
   # States
   print("Sample states:")
   print(df_10k['state'].value_counts())
   ```

6. **Create a summary report**

   ```python
   print("\n=== DATA QUALITY SUMMARY ===")
   print(f"10k rows: {df_10k.shape[0]}, columns: {df_10k.shape[1]}")
   print(f"25k rows: {df_25k.shape[0]}, columns: {df_25k.shape[1]}")
   print(f"\n10k null values:\n{df_10k.isnull().sum()}")
   print(f"\n25k null values:\n{df_25k.isnull().sum()}")
   print(f"\n10k duplicates: {df_10k.duplicated().sum()}")
   print(f"25k duplicates: {df_25k.duplicated().sum()}")
   ```

### Your Deliverable

A Jupyter notebook with:
- Duplicate analysis for both datasets
- Null value analysis (counts and percentages)
- Sample values from text columns to identify format issues
- A summary report

### Commit Your Work

```
git add notebooks/02_data_quality_check.ipynb
git commit -m "Day 2: Data quality assessment"
```

### What You Should Document

Write comments in your notebook explaining what you found:
- How many duplicates?
- Which columns have the most missing values?
- What format inconsistencies do you see?
- What will you need to fix?

This becomes your action plan for the cleaning days ahead.

---

## DAYS 3-7 (Coming Tomorrow)

I'll add more tasks here each morning:

**Days 3-4:** Clean the data. Handle missing values, remove duplicates, standardize formats.

**Days 5-6:** Validate and prepare. Write rules to catch errors. Create SQL-ready datasets.

**Days 7-8:** Analyze and report. Write SQL queries, create visualizations, tell the story in your data.

**Day 12:** Build your Excel dashboard and present your findings.

Check back tomorrow morning for Day 3 tasks.
