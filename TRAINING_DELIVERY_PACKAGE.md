# PrintApex Data Analytics Training Program
## Complete Delivery Package for Interns

**Program Version:** 1.0  
**Created:** September 23, 2026  
**Duration:** 7 days intensive  
**Cost:** $0 (free tools only)  
**Expected Outcome:** Interview-ready junior data analyst

---

## 📦 WHAT YOU'RE RECEIVING

This training package contains everything interns need to complete a real production data engineering project in one week. All materials are self-contained and designed for independent learning.

### Files Included

```
c:\Users\ABDUL\Documents\Printing Automation\
│
├── 📄 INTERN_TRAINING_README.md          [START HERE]
│   └─ Comprehensive guide to the entire 7-day program
│   └─ Tools breakdown by phase
│   └─ Interview talking points
│
├── 📄 INTERN_QUICK_START.md               [DAILY CHECKLIST]
│   └─ Day-by-day task breakdown
│   └─ Checkboxes for each phase
│   └─ Code templates and examples
│
├── 📄 TRAINING_DELIVERY_PACKAGE.md        [YOU ARE HERE]
│   └─ Index of all materials
│   └─ How to deploy to interns
│   └─ FAQs & troubleshooting
│
├── 📁 PrintShopDataProject/               [PROJECT TEMPLATE]
│   ├─ Phase1_Profile_Template.py          [Copy to Jupyter for Days 1-2]
│   ├─ FOLDER_STRUCTURE.md                 [How to organize files]
│   └─ (Interns will create subdirectories here)
│
├── 📊 shops_raw_data_10k.csv             [DATASET 1]
│   └─ 10,001 rows (incl. header)
│   └─ 32 columns (exact DB schema)
│   └─ 3.91 MB
│   └─ Real production data with intentional quality issues
│
├── 📊 shops_raw_data_25k.csv             [DATASET 2]
│   └─ 25,001 rows (incl. header)
│   └─ 32 columns (same schema)
│   └─ 9.88 MB
│   └─ Different quality issues than 10k
│
└── (Other training docs reference these)
```

---

## 🎯 HOW TO DELIVER THIS TO INTERNS

### Step 1: Share the Starting Materials (15 min)

**Give each intern:**

1. Access to this folder: `c:\Users\ABDUL\Documents\Printing Automation\`
2. Read these files in order:
   - [ ] `INTERN_TRAINING_README.md` (understand the program)
   - [ ] `INTERN_QUICK_START.md` (day-by-day checklist)

### Step 2: Ensure They Have Tools (30 min)

Verify each intern has installed:
- [ ] Python 3.10+ (`python --version`)
- [ ] Git (`git --version`)
- [ ] Jupyter (`jupyter notebook`)
- [ ] LibreOffice Calc or Excel
- [ ] Virtual environment set up in their `PrintShopDataProject` folder

### Step 3: Verify Data Files (5 min)

- [ ] Both CSV files exist in `data/raw/`
- [ ] File sizes match (10k = 3.91 MB, 25k = 9.88 MB)
- [ ] Both have 32 columns

### Step 4: They Begin Phase 1 (Days 1-2)

- [ ] Each intern works through `INTERN_QUICK_START.md` independently
- [ ] No hand-holding; struggles are intentional
- [ ] They document their discoveries in `output/issue_log.txt`

### Step 5: Weekly Check-ins (Optional)

Each day morning or evening:
- Interns commit their work to Git: `git commit -m "Day X: [phase] complete"`
- You review commits to check progress
- Flag blockers (missing tools, unclear steps)

### Step 6: Final Review (Day 12)

- [ ] All 8 deliverables present
- [ ] Git history shows 6+ commits
- [ ] Cleaned data exists
- [ ] SQL queries work
- [ ] Excel dashboard displays correctly

---

## 📋 PHASE BREAKDOWN

| Phase | Days | Goal | Intern Creates |
|-------|------|------|-----------------|
| 1 | 1-2 | Profile raw data | `issue_log.txt` |
| 2 | 3-4 | Handle nulls/dups | `transformation_log.txt` |
| 3 | 5-6 | Standardize formats | Standardized CSVs |
| 4 | 7-8 | Validate business logic | `validation_rules.txt` |
| 5 | 9-11 | SQL + Python analysis | SQL queries + charts |
| 6 | 12 | Build Excel dashboard | `dashboard.xlsx` |

---

## 🛠 TOOLS REQUIRED (ALL FREE)

| Tool | Download Link | Why Needed |
|------|---------------|-----------|
| Python 3.10+ | https://www.python.org/downloads/ | Data processing engine |
| pip (included) | With Python | Package manager |
| pandas | `pip install pandas` | Data manipulation |
| Jupyter | `pip install jupyter` | Interactive notebooks |
| SQLite | Built into Python | Database queries |
| Git | https://git-scm.com | Version control |
| VS Code | https://code.visualstudio.com | Code editor (optional) |
| LibreOffice Calc | https://www.libreoffice.org | Excel alternative |

**Total install time:** ~30 minutes  
**Total cost:** $0

---

## 📊 DATASETS

Both CSV files use **exact schema from production database** (32 columns):

```
id, tenant_id, slug, status, business_name, owner_name, 
contact_phone, contact_email, address_line_1, address_line_2, 
city, state, postal_code, gst_status, gst_number, 
printer_make, printer_model, printer_notes, 
payout_upi_id, payout_upi_name, 
subscription_plan, subscription_status, 
current_period_end, subscription_reference, 
subscription_verified_at, timezone, config, 
created_at, updated_at, approved_at, 
suspended_at, expired_at
```

### Dataset 1: `shops_raw_data_10k.csv`
- **Rows:** 10,001 (1 header + 10,000 data)
- **Size:** 3.91 MB
- **Quality Issues:** 
  - 2% missing contact_phone
  - 15% inconsistent phone format
  - 5% business name spacing issues
  - 3% missing postal codes
  - 1% invalid date formats
  - 0.5% duplicate rows

### Dataset 2: `shops_raw_data_25k.csv`
- **Rows:** 25,001 (1 header + 25,000 data)
- **Size:** 9.88 MB
- **Quality Issues (different from 10k):**
  - 3% null values in different fields
  - Different duplicate patterns
  - Different formatting inconsistencies
  - Interns see realistic data variation

---

## ✅ SUCCESS CRITERIA

### For Each Intern

**By End of Day 2 (Phase 1):**
- [ ] `Phase1_Profile.ipynb` created with profiling code
- [ ] `output/issue_log.txt` documents real issues found
- [ ] Git commit: "Phase 1 complete"
- [ ] Understands the data problems

**By End of Day 4 (Phase 2):**
- [ ] `Phase2_Missing_Duplicates.ipynb` shows decisions made
- [ ] `output/transformation_log.txt` documents changes
- [ ] Cleaned checkpoint CSVs saved
- [ ] Git commit: "Phase 2 complete"

**By End of Day 6 (Phase 3):**
- [ ] `Phase3_Standardize.ipynb` shows standardization logic
- [ ] All data types correct
- [ ] Phones = 10 digits, Dates = ISO format
- [ ] Git commit: "Phase 3 complete"

**By End of Day 8 (Phase 4):**
- [ ] `Phase4_Validation.ipynb` with validation rules
- [ ] `output/validation_rules.txt` documents rules
- [ ] `data/processed/shops_[10k/25k]_final.csv` created
- [ ] Git commit: "Phase 4 complete"

**By End of Day 11 (Phase 5):**
- [ ] `sql/queries.sql` with 5 working queries
- [ ] `notebooks/Phase5_Analysis.ipynb` with insights
- [ ] Charts generated in `output/charts/`
- [ ] Git commit: "Phase 5 complete"

**By End of Day 12 (Phase 6):**
- [ ] `output/dashboard.xlsx` created
- [ ] All 8 deliverables present
- [ ] Git log shows 6+ commits
- [ ] Git commit: "Final: All deliverables complete"

---

## 🚀 PHASE 1 QUICK START (For Trainer to Review)

Here's what happens on Day 1-2:

### Day 1 Morning

```bash
# Intern opens terminal
cd PrintShopDataProject

# Activates virtual environment
venv\Scripts\activate

# Starts Jupyter
jupyter notebook

# In Jupyter:
# 1. Creates new Python 3 notebook → "Phase1_Profile.ipynb"
# 2. Copies Phase1_Profile_Template.py code into cells
# 3. Runs all cells (Shift+Enter)
# 4. Saves notebook
```

### Day 1 Evening

Intern reviews outputs:
- Dataset shapes
- Null value counts
- Duplicate rows
- Date anomalies
- Phone format issues

### Day 2 Morning

Intern creates `output/issue_log.txt`:

```
contact_phone | MISSING | 2% (200 rows) | MEDIUM | Some shops use email only
contact_phone | FORMAT_INCONSISTENT | 15% (1500 rows) | MEDIUM | Mix of +91, 91-, plain digits
business_name | LEADING_TRAILING_SPACES | 5% (500 rows) | LOW | "  Copy Center  " needs trim
postal_code | INVALID_FORMAT | 1% (100 rows) | HIGH | Should be 6 digits; some are 5-7
postal_code | MISSING | 3% (300 rows) | HIGH | Can't validate without postal code
[...continue for all issues...]
```

### Day 2 Afternoon

Intern commits to Git:

```bash
git add output/issue_log.txt notebooks/Phase1_Profile.ipynb
git commit -m "Phase 1 complete: Data profiling and issue identification"
```

---

## ❓ FAQ & TROUBLESHOOTING

### Q: "Python not found" error
**A:** Python not installed or not added to PATH. Download from python.org, reinstall, check "Add Python to PATH"

### Q: "ModuleNotFoundError: No module named 'pandas'"
**A:** Run `pip install pandas` (with virtual environment activated)

### Q: "Jupyter won't start"
**A:** Run `pip install jupyter` then `jupyter notebook`

### Q: "CSV file too large, won't open"
**A:** Don't try to open 25k CSV in Excel. Use pandas instead: `df = pd.read_csv('shops_raw_data_25k.csv')`

### Q: "I don't understand what Phase X wants"
**A:** Re-read the phase outline in `INTERN_QUICK_START.md`. The goal is clear, but you must figure out how to accomplish it.

### Q: "Can I skip Phase Y?"
**A:** No. Each phase builds on the last. Phase 2 needs Phase 1 output. Phase 3 needs Phase 2 output.

### Q: "How do I know if my work is correct?"
**A:** Your Git log and deliverables are your proof. If your issue_log.txt shows real problems, you're on track. If your transformation_log.txt explains every change, you're doing it right.

### Q: "What if I find issues my peers didn't?"
**A:** Great! Data profiling is exploratory. Different people find different things. Document what you found and why it matters.

### Q: "Can I use AI/ChatGPT to help?"
**A:** Yes, use it for syntax help, debugging, and explanations. But don't copy-paste full solutions. The struggle of writing your own code is where learning happens.

---

## 📞 SUPPORT

### What Trainer Should Provide

- [ ] This entire folder and files
- [ ] Access to the two CSV data files
- [ ] Answers to "What tool should I use for X?" questions
- [ ] Clarification on any phase goals
- [ ] Code review and feedback on Git commits

### What Trainer Should NOT Provide

- [ ] Full solutions to Phase problems
- [ ] Answers to "What value should I use?" questions
- [ ] Debugging their code line-by-line
- [ ] Extensions beyond 7 days (timeboxing is critical)

---

## 🎓 LEARNING OUTCOMES

After completing this program, interns can:

**Technical Skills:**
- [ ] Load and profile large datasets with pandas
- [ ] Identify and document data quality issues
- [ ] Write data cleaning logic (handling nulls, standardization, validation)
- [ ] Write SQL queries to analyze data
- [ ] Create Python visualizations
- [ ] Build Excel dashboards
- [ ] Use Git for version control

**Professional Skills:**
- [ ] Think like a data engineer (data first, then analysis)
- [ ] Document decisions and transformations
- [ ] Reproduce work with scripts (not just notebooks)
- [ ] Communicate findings to non-technical audiences
- [ ] Time-box work (deliver in 1 week)

**Portfolio:**
- [ ] GitHub repo with 6+ commits
- [ ] Cleaned datasets
- [ ] SQL queries
- [ ] Python analysis notebooks
- [ ] Excel dashboard
- [ ] Documentation showing thought process

---

## 🏆 WHAT SUCCESS LOOKS LIKE

### Week 1 Check-in Email

> Subject: Week 1 Data Analytics Training Complete
>
> Hi [Intern],
>
> Congratulations on completing your first data engineering project! Here's what you accomplished:
>
> ✅ Profiled 35,000 production records  
> ✅ Identified and documented 15 data quality issues  
> ✅ Cleaned and standardized 34,385 records  
> ✅ Wrote 5 SQL business analysis queries  
> ✅ Created Python visualizations  
> ✅ Built an Excel dashboard with KPIs  
> ✅ Maintained version control with Git  
> ✅ Documented every decision  
>
> Your GitHub repo shows:
> - 7 commits across 6 phases
> - Clean code with meaningful messages
> - Professional data transformations
>
> **Interview Talking Points:**
> - "I profiled 35k shop records and found real data issues"
> - "I standardized phone numbers, dates, and postal codes using regex"
> - "I wrote SQL queries to answer business questions"
> - "I built reproducible cleaning pipelines"
> - "I delivered analysis in Excel and Python"
>
> This is real work. You're ready for entry-level interviews.
>
> Next steps: Link this repo in your portfolio. Reference it in job applications.
>
> Well done,
> [Your Name]
> Apex AGI Solutions

---

## 📝 APPENDIX: PROJECT STRUCTURE

Interns should create this folder structure:

```
PrintShopDataProject/
│
├── data/
│   ├── raw/
│   │   ├── shops_raw_data_10k.csv          [GIVEN]
│   │   └── shops_raw_data_25k.csv          [GIVEN]
│   ├── cleaned/
│   │   ├── shops_10k_after_missing_handling.csv
│   │   ├── shops_25k_after_missing_handling.csv
│   │   ├── shops_10k_standardized.csv
│   │   └── shops_25k_standardized.csv
│   └── processed/
│       ├── shops_10k_final.csv             [DELIVERABLE 1]
│       ├── shops_25k_final.csv             [DELIVERABLE 2]
│       └── shops_analysis.db               (SQLite database)
│
├── notebooks/
│   ├── Phase1_Profile.ipynb                [DELIVERABLE 5]
│   ├── Phase2_Missing_Duplicates.ipynb
│   ├── Phase3_Standardize.ipynb
│   ├── Phase4_Validation.ipynb
│   └── Phase5_Analysis.ipynb               [DELIVERABLE 6]
│
├── scripts/
│   ├── __init__.py
│   ├── cleaning.py
│   ├── validation.py
│   └── analysis.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql                         [DELIVERABLE 7]
│
├── output/
│   ├── issue_log.txt                       [DELIVERABLE 3]
│   ├── transformation_log.txt              [DELIVERABLE 4]
│   ├── validation_rules.txt
│   ├── validation_summary.csv
│   ├── decisions_made.csv
│   ├── charts/
│   │   ├── chart_01_states.png
│   │   ├── chart_02_subscription_plans.png
│   │   ├── chart_03_printers.png
│   │   ├── chart_04_upi.png
│   │   └── chart_05_status.png
│   └── dashboard.xlsx                      [DELIVERABLE 8]
│
├── .gitignore                              [CREATED]
├── README.md                               [CREATED]
├── venv/                                   [PYTHON VENV - not committed]
│
└── .git/                                   [CREATED]
```

---

## 🎯 FINAL NOTES

### For the Trainer

This program is designed to be **self-contained and independent**. Each intern should be able to:
- Understand what they're building (from README)
- Know what to do each day (from QUICK_START)
- Have templates to follow (Phase1_Profile_Template.py)
- Debug themselves (using Git commits, checking work)

Your role is to:
- Answer "how do I use Git?" but not "why is my code wrong?"
- Verify they have tools installed
- Review their week-end deliverables
- Provide feedback on their code quality (not quantity)

### For the Interns

You are expected to:
- Work independently for 40-50 hours across 7 days
- Struggle. That's the point. Google errors, check documentation, ask peers.
- Document your decisions (issue_log, transformation_log)
- Commit your work every 1-2 days
- Deliver all 8 final files on Day 12

This is a sprint. You're not here to relax. You're building a real portfolio.

### For Hiring Managers

When an intern shows you this project, you'll see:
- **Real data engineering thinking** (profiling → cleaning → validation → analysis)
- **Production-ready mindset** (version control, documentation, reproducibility)
- **Interview-ready skills** (SQL, Python, Excel, storytelling)

They won't know everything, but they'll know how to think. That's what matters.

---

## 📄 Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-09-23 | Initial delivery package created |

---

## 🎉 YOU'RE READY

Everything you need is in this folder. Share it with your interns. Track their progress with Git commits. Review deliverables on Day 12.

They'll emerge as junior-level data engineers ready for their first interviews.

Good luck.

---

*PrintApex Data Analytics Training Program v1.0*  
*Created: September 23, 2026*  
*For: Apex AGI Solutions Interns*  
*Duration: 7 Days*  
*Cost: $0*  
*Success Rate: Designed for 95% completion*
