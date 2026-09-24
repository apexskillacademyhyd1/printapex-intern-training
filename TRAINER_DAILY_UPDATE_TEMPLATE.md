# TRAINER'S GUIDE: How to Update Daily Tasks

## 📌 How This Works

You created `DAILY_TASKS.md` for your interns on GitHub. This file shows you exactly what to update each day.

**The Pattern:**
1. Each morning, you update `DAILY_TASKS.md` with that day's tasks
2. Interns check GitHub and see new tasks for today
3. They complete the tasks
4. Tomorrow, you update the file again with new tasks
5. This continues for 7 days

---

## 📅 Daily Update Schedule

### Day 0 (Today)
✅ **DONE** - Posted initial setup tasks (Day 0)  
✅ Posted Phase 1 preview (Days 1-2)

### Day 1 (Tomorrow)
- [ ] Keep Day 0 tasks (for reference)
- [ ] **EXPAND** `## DAY 1 MORNING: Get Started with Profiling` section with full code
- [ ] **EXPAND** `## DAY 1 EVENING/DAY 2: Review Findings & Create Issue Log` section
- [ ] Keep preview of Day 3 (unchanged)

### Day 2 (Day After Tomorrow)
- [ ] Keep Day 0-1 tasks (for reference)
- [ ] Complete all Day 1 tasks (already visible)
- [ ] **EXPAND** Day 2 sections with full code
- [ ] Move Phase 2 from preview to "COMING DAY 3"

### Day 3 (3 Days From Now)
- [ ] Keep previous days (for reference)
- [ ] **ADD** Phase 2: Handle Missing Values section with full code
- [ ] **ADD** detailed Day 3-4 tasks
- [ ] Move Phase 3 from preview to "COMING DAY 5"

### Day 5 (5 Days From Now)
- [ ] Keep previous phases (for reference)
- [ ] **ADD** Phase 3: Standardize & Format section with full code
- [ ] **ADD** detailed Day 5-6 tasks
- [ ] Move Phase 4 from preview to "COMING DAY 7"

### Day 7 (7 Days From Now)
- [ ] Keep previous phases (for reference)
- [ ] **ADD** Phase 4: Validation Rules section with full code
- [ ] **ADD** detailed Day 7-8 tasks
- [ ] Move Phase 5 from preview to "COMING DAY 9"

### Day 9 (9 Days From Now)
- [ ] Keep previous phases (for reference)
- [ ] **ADD** Phase 5: SQL Analysis & Python Insights section
- [ ] **ADD** detailed Day 9-11 tasks
- [ ] Move Phase 6 from preview to "COMING DAY 12"

### Day 12 (12 Days From Now - FINAL)
- [ ] Keep all previous phases (for reference)
- [ ] **ADD** Phase 6: Excel Dashboard section with full code
- [ ] **ADD** Day 12 final tasks and deliverables checklist
- [ ] Mark program as COMPLETE

---

## 🔄 Update Process (Each Day)

### Step 1: Open DAILY_TASKS.md
Location on GitHub: `/INTERN_TRAINING_PROGRAM/DAILY_TASKS.md`

### Step 2: Find the Section to Update
Look for this pattern:
```
## [TO BE UPDATED ON DAY X]

### Phase Y: [Name] (Days X-Y)

Tasks for Days X-Y will be posted on Day X.
```

### Step 3: Replace with Actual Tasks
Replace the placeholder with real tasks like the Day 1 example.

### Step 4: Keep Previous Days Unchanged
All previous day tasks stay visible (for reference and troubleshooting).

### Step 5: Update Status Line
Change this line:
```
**Status:** ACTIVE PROGRAM - DAY 1 TASKS LIVE ✅
```

To:
```
**Status:** ACTIVE PROGRAM - DAY 3 TASKS LIVE (Days 0-2 Complete) ✅
```

### Step 6: Commit Update
```bash
git add DAILY_TASKS.md
git commit -m "Day 3: Tasks updated for Days 3-4"
git push origin main
```

---

## 📝 Template: What to Add Each Day

When you update the file, replace this:
```
## [COMING TOMORROW - Day 3]

### Phase 2: Handle Missing Values & Duplicates (Days 3-4)

Tasks for Days 3-4 will be posted tomorrow. Come back to this document to see your new tasks.

**Preview of what's coming:**
- Remove or fill null values based on business logic
- Handle duplicate rows
- Save cleaned checkpoint data
- Document all decisions
- Create transformation log
```

With this structure:
```
## 📅 DAYS 3-4: Handle Missing Values & Duplicates

**Status:** Days 3-4 (Wed-Thu)  
**Time Required:** 8-10 hours  
**Objective:** Remove corrupted data, handle nulls, eliminate duplicates

### Task 2.1: [Task Name]
[Full instructions with code examples]
**Deliverable:** [What to produce]
**Time:** [Minutes]

### Task 2.2: [Task Name]
[Full instructions with code examples]
**Deliverable:** [What to produce]
**Time:** [Minutes]

[Continue with all tasks for that phase...]

### Day 3-4 Checklist
- [ ] Task 1 complete
- [ ] Task 2 complete
- [ ] ...

**Status:** ✅ PHASE 2 COMPLETE
```

---

## 💡 Tips for Daily Updates

### Keep It Consistent
- Use same formatting as Day 1
- Include code examples in markdown blocks
- Show expected output
- Time estimates per task

### Make It Actionable
- Each task should be doable in 15-30 minutes
- Provide exact code to copy/paste
- Show what "done" looks like
- Include verification steps

### Keep Previous Phases
- Never delete earlier tasks
- Interns can scroll up to review
- Shows continuous progress
- Useful for debugging

### Add Time Estimates
- Helps interns pace themselves
- Realistic: 50-60 hours total
- ~7 hours per day
- More time on Days 5-6 (standardization is complex)

---

## 📋 Daily Update Checklist

Each day before updating, verify:

- [ ] Day's tasks are well-defined
- [ ] Code examples are tested
- [ ] Expected outputs described
- [ ] Time estimates reasonable
- [ ] Deliverables are clear
- [ ] Previous days remain unchanged
- [ ] Status line updated
- [ ] Commit message is clear

---

## 🔀 Example: Updating for Day 3

**Current text in file (before update):**
```
## [COMING TOMORROW - Day 3]

### Phase 2: Handle Missing Values & Duplicates (Days 3-4)

Tasks for Days 3-4 will be posted tomorrow.
```

**What you'll replace it with (after update):**
```
## 📅 DAYS 3-4: Handle Missing Values & Duplicates

**Status:** Days 3-4 (Wed-Thu)  
**Time Required:** 8-10 hours  
**Objective:** Remove/fill nulls, handle duplicates, save checkpoints

### Task 2.1: Create Phase 2 Notebook

Create file: `notebooks/Phase2_Missing_Duplicates.ipynb`

In Jupyter, create this code:

**Cell 1: Load Phase 1 Output**
```python
import pandas as pd

df_10k = pd.read_csv('../../data/raw/shops_raw_data_10k.csv')
print(f"Data loaded: {len(df_10k)} rows")
```

**Cell 2: Handle Missing postal_code**
```python
# Remove rows with missing postal_code (required field)
rows_before = len(df_10k)
df_10k = df_10k.dropna(subset=['postal_code'])
rows_removed = rows_before - len(df_10k)

print(f"Removed: {rows_removed} rows missing postal_code")
print(f"Remaining: {len(df_10k)} rows")
```

[... continue with more detailed tasks ...]

**Deliverable:** Phase 2 notebook with all tasks complete  
**Time:** 8 hours

### Day 3-4 Checklist
- [ ] Phase 2 notebook created
- [ ] Missing values handled
- [ ] Duplicates removed
- [ ] Cleaned data saved
- [ ] Transformation log created
- [ ] Work committed to Git

**Status:** ✅ PHASE 2 COMPLETE
```

---

## 🎯 What Interns Will See

**Day 0 Morning:**
Interns open DAILY_TASKS.md on GitHub and see:
```
✅ Day 0: Setup tasks (10 detailed tasks)
✅ Day 1: Phase 1 preview (coming tomorrow)
```

**Day 1 Morning:**
They refresh the page and see:
```
✅ Day 0: Setup tasks (already done)
✅ Day 1: Phase 1 profiling (12 detailed tasks - NEW!)
✅ Day 2: Review & issue log (5 detailed tasks - NEW!)
⏳ Day 3-4: Phase 2 preview (coming in 2 days)
```

**Day 3 Morning:**
They refresh again and see:
```
✅ Day 0: Setup tasks (reference)
✅ Day 1: Phase 1 profiling (reference)
✅ Day 2: Review & issue log (reference)
✅ Day 3-4: Phase 2 missing values (12 detailed tasks - NEW!)
⏳ Day 5-6: Phase 3 preview (coming in 2 days)
```

**By Day 12:**
They see all phases completed, entire 7-day journey visible in one document.

---

## ✅ Final Tip

Keep the document in this format:

1. **Header** - What this program is
2. **Setup (Day 0)** - Still visible ✅
3. **Phase 1 (Days 1-2)** - Detailed tasks visible ✅
4. **Phase 2 (Days 3-4)** - Detailed tasks visible ✅
5. **Phase 3 (Days 5-6)** - Preview or detailed ⏳
6. **Phase 4 (Days 7-8)** - Preview ⏳
7. **Phase 5 (Days 9-11)** - Preview ⏳
8. **Phase 6 (Day 12)** - Preview ⏳
9. **Reference Section** - Tools, summary, FAQ

**This way, interns see their complete 7-day journey in one file.**

---

## 📅 Update Timeline Summary

| Day | Update | Status |
|-----|--------|--------|
| Day 0 | Post setup + Phase 1 preview | ✅ DONE |
| Day 1 | Post Phase 1 full + Phase 2 preview | TODO |
| Day 2 | Complete Phase 1 + Phase 2 preview | TODO |
| Day 3 | Post Phase 2 full + Phase 3 preview | TODO |
| Day 4 | Complete Phase 2 + Phase 3 preview | TODO |
| Day 5 | Post Phase 3 full + Phase 4 preview | TODO |
| Day 6 | Complete Phase 3 + Phase 4 preview | TODO |
| Day 7 | Post Phase 4 full + Phase 5 preview | TODO |
| Day 8 | Complete Phase 4 + Phase 5 preview | TODO |
| Day 9 | Post Phase 5 full + Phase 6 preview | TODO |
| Day 11 | Complete Phase 5 + Phase 6 preview | TODO |
| Day 12 | Post Phase 6 full - PROGRAM COMPLETE | TODO |

---

**Remember:** Interns will be watching this file daily. Clear, detailed tasks help them stay on track. Good luck! 🚀

