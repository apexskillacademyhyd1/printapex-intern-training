# Start Here

Welcome. You're going to spend the next 7 days working on a real data project. It's not a tutorial. It's real work with real data that has real problems.

You'll load two CSV files with production data. They have missing values, inconsistent formats, duplicates—all the mess you see in actual jobs. Your job is to clean them, analyze them, and build a professional report. By the end, you'll have portfolio pieces you can show to future employers.

## What You Need (Everything Is Free)

Get these installed today:
- **Python 3.10 or higher** - https://www.python.org/downloads/
- **Git** - https://git-scm.com
- **Excel** (or similar spreadsheet tool)
- **VS Code** (optional, but I recommend it) - https://code.visualstudio.com

That's it. Nothing paid. Everything open-source.

## Your First Steps Today

1. Install Python. Make sure you check "Add Python to PATH" during setup.
2. Open a terminal and verify: `python --version` (should be 3.10+)
3. Install Git.
4. Create your project folder:
   ```
   mkdir PrintShopDataProject
   cd PrintShopDataProject
   ```
5. Initialize Git:
   ```
   git init
   git config user.name "Your Name"
   git config user.email "your.email@example.com"
   ```
6. Create your folder structure:
   ```
   mkdir data\raw data\cleaned data\processed notebooks scripts sql output\charts
   ```
7. Set up Python. Create a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
   You should see `(venv)` in your terminal.
8. Install the libraries you'll need:
   ```
   pip install pandas jupyter matplotlib seaborn
   ```
9. Download the two data files from this repository and put them in `data/raw/`:
   - `shops_raw_data_10k.csv`
   - `shops_raw_data_25k.csv`
10. Create a `.gitignore` file in your project folder with this content:
    ```
    *.csv
    *.xlsx
    *.db
    venv/
    __pycache__/
    .ipynb_checkpoints/
    ```
11. Make your first commit:
    ```
    git add .
    git commit -m "Initial project setup"
    ```
12. Test Jupyter:
    ```
    jupyter notebook
    ```
    A browser window should open. Close it with Ctrl+C. If that worked, you're ready.

## What Happens Next

Tomorrow, come back to `DAILY_TASKS.md`. I'll have your Day 1 tasks there. Each morning I update that file with what you need to do that day.

Your tasks will tell you exactly what to build, what to analyze, what to commit. Follow them in order.

## Your Timeline

**Days 1-2:** Load and profile the data. Understand what you're working with.

**Days 3-4:** Clean it. Remove bad records, fix missing values, get it organized.

**Days 5-6:** Standardize it. Make formats consistent.

**Days 7-8:** Validate it. Write rules to catch errors.

**Days 9-11:** Analyze it. Write SQL, create charts, draw insights.

**Day 12:** Build your final Excel dashboard.

## Get Started

Go to `DAILY_TASKS.md` and do the setup work. I'll see you on Day 1.
