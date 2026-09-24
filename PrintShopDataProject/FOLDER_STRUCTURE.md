# PrintShop Data Project - Folder Structure

Create this structure in your `PrintShopDataProject` folder:

```
PrintShopDataProject/
│
├── data/
│   ├── raw/                          # Original CSV files (do not modify)
│   │   ├── shops_raw_data_10k.csv
│   │   └── shops_raw_data_25k.csv
│   ├── cleaned/                      # After Phase 2-3 cleaning
│   │   ├── shops_10k_after_missing_handling.csv
│   │   ├── shops_25k_after_missing_handling.csv
│   │   ├── shops_10k_standardized.csv
│   │   └── shops_25k_standardized.csv
│   └── processed/                    # Final production-ready data
│       ├── shops_10k_final.csv
│       └── shops_25k_final.csv
│
├── notebooks/                        # Jupyter notebooks (one per phase)
│   ├── Phase1_Profile.ipynb         # Days 1-2: Profiling & issues
│   ├── Phase2_Missing_Duplicates.ipynb  # Days 3-4: Handle nulls/dups
│   ├── Phase3_Standardize.ipynb     # Days 5-6: Format fixes
│   ├── Phase4_Validation.ipynb      # Days 7-8: Rules & outliers
│   └── Phase5_Analysis.ipynb        # Days 9-11: SQL & insights
│
├── scripts/                          # Reusable Python modules
│   ├── __init__.py                  # (empty file to make it a package)
│   ├── cleaning.py                  # Reproducible cleaning pipeline
│   ├── validation.py                # Validation functions
│   └── analysis.py                  # Analysis & chart functions
│
├── sql/                              # SQL query files
│   ├── schema.sql                   # Create tables
│   └── queries.sql                  # 5 business analysis queries
│
├── output/                           # Final deliverables
│   ├── issue_log.txt                # Phase 1: Data quality issues
│   ├── decisions_made.csv           # Phase 2: Handling decisions
│   ├── transformation_log.txt       # Phase 2-3: All changes made
│   ├── validation_rules.txt         # Phase 4: Validation logic
│   ├── validation_results.csv       # Phase 4: Failed validation rows
│   ├── charts/                      # Generated charts
│   │   ├── chart_states.png
│   │   ├── chart_subscription_plans.png
│   │   ├── chart_printer_makes.png
│   │   └── chart_upi_configuration.png
│   └── dashboard.xlsx               # Phase 6: Final Excel dashboard
│
├── .gitignore                        # Prevents large files from Git
├── README.md                         # Your project summary
└── venv/                            # Virtual environment (do NOT commit)
```

---

## What Goes Where

### `data/raw/`
- Your original CSV files from the trainer
- **NEVER modify these files**
- Use these as the source of truth

### `data/cleaned/`
- Intermediate checkpoints as you work through phases
- Save after each major transformation
- Allows you to backtrack if needed

### `data/processed/`
- Final, production-ready datasets
- After Phase 4 validation completes
- These are what you'll load for analysis in Phase 5

### `notebooks/`
- One Jupyter notebook per phase
- Each contains exploration code + documentation
- Save after each session

### `scripts/`
- Python functions that do the same work as notebooks
- But in reproducible, reusable form
- Example: `cleaning.py` = all Phase 2-3 logic in one script

### `sql/`
- SQL queries for analysis
- Load your cleaned data into SQLite, then run these queries
- Test each query and document results

### `output/`
- Text logs documenting your decisions
- CSV reports of validation results
- PNG charts from Python
- Excel dashboard with all findings

---

## .gitignore

Create a `.gitignore` file to exclude large files from Git:

```
# Data files (too large)
*.csv
*.xlsx
*.db
*.db-journal

# Python
venv/
__pycache__/
*.pyc
*.egg-info/

# Jupyter
.ipynb_checkpoints/

# OS
.DS_Store
Thumbs.db

# Logs
*.log
```

---

## Create Structure (Bash/PowerShell)

### On Windows (PowerShell):

```powershell
mkdir data\raw, data\cleaned, data\processed, notebooks, scripts, sql, output\charts
New-Item -Path ".gitignore" -ItemType File
```

### On Mac/Linux (Bash):

```bash
mkdir -p data/raw data/cleaned data/processed notebooks scripts sql output/charts
touch .gitignore
```

---

## First Git Commit

After creating the structure:

```bash
cd PrintShopDataProject
git init
git config user.name "Your Name"
git config user.email "your.email@example.com"
git add .gitignore README.md
git commit -m "Initial project structure"
```

---

Now you're ready for Phase 1. Copy your CSV files into `data/raw/` and start profiling.
