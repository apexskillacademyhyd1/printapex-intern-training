# 📤 FILES TO UPLOAD TO GITHUB

## What to Upload

You'll upload the following files to GitHub for your interns:

### 📋 Core Documents (Upload All)

1. **DAILY_TASKS.md** ⭐ (MOST IMPORTANT)
   - This is the main file interns check every day
   - Contains Day 0 full tasks
   - Contains Day 1-2 Phase 1 full tasks
   - Contains previews for future phases (you update daily)
   - **Action:** Upload to GitHub root
   - **Interns will:** Check this file daily for their tasks

2. **START_HERE.md**
   - Quick navigation guide
   - Upload to GitHub root
   - Interns read this first (before DAILY_TASKS.md)

3. **README.md**
   - Program overview
   - Boundary marker (independent folder)
   - Upload to GitHub root

4. **TRAINER_DAILY_UPDATE_TEMPLATE.md**
   - Your personal guide (don't give to interns)
   - Helps you know what to update each day
   - Can upload but mark as "Trainer Only"
   - Or keep locally

---

### 📊 Data Files (Upload Both)

1. **shops_raw_data_10k.csv**
   - Size: 3.91 MB
   - Rows: 10,001
   - Columns: 32
   - Upload to GitHub in `data/raw/` folder

2. **shops_raw_data_25k.csv**
   - Size: 9.88 MB
   - Rows: 25,001
   - Columns: 32
   - Upload to GitHub in `data/raw/` folder

---

### ❌ Files NOT to Upload

- `INTERN_QUICK_START.md` - Too much detail upfront
- `TRAINING_DELIVERY_PACKAGE.md` - Trainer reference only
- `TRAINER_HANDOFF.md` - Trainer reference only
- `Phase1_Profile_Template.py` - Included in DAILY_TASKS.md
- `FOLDER_STRUCTURE.md` - Reference only
- `⚠️_DO_NOT_MODIFY.txt` - Keep local only

---

## 📁 GitHub Repository Structure

```
your-repo-name/
│
├── README.md                      ← Program overview
├── START_HERE.md                  ← For interns to read first
├── DAILY_TASKS.md                 ← ⭐ MAIN FILE - Interns check daily
│
├── data/
│   └── raw/
│       ├── shops_raw_data_10k.csv
│       └── shops_raw_data_25k.csv
│
└── (interns create the rest: notebooks/, scripts/, sql/, output/)
```

---

## 🚀 Upload Instructions

### Step 1: Create GitHub Repository
1. Go to GitHub.com
2. Click "New repository"
3. Name: `printapex-intern-training` (or similar)
4. Description: "PrintApex Data Analytics Training Program - 7 Days"
5. Public (so interns can access)
6. Create repository

### Step 2: Prepare Files Locally
```bash
cd your-local-folder
mkdir -p data/raw

# Copy files
cp DAILY_TASKS.md .
cp START_HERE.md .
cp README.md .
cp shops_raw_data_10k.csv data/raw/
cp shops_raw_data_25k.csv data/raw/

# Optional: Copy trainer guide
cp TRAINER_DAILY_UPDATE_TEMPLATE.md . (with note "Trainer Only")
```

### Step 3: Initialize Git & Push
```bash
git init
git add .
git commit -m "Initial upload: Intern training program with Day 0 setup tasks"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/printapex-intern-training.git
git push -u origin main
```

### Step 4: Share with Interns
Give them the GitHub URL:
```
https://github.com/YOUR_USERNAME/printapex-intern-training
```

Tell them:
1. Clone the repository
2. Read `START_HERE.md` first
3. Check `DAILY_TASKS.md` each morning for that day's tasks
4. Work through tasks
5. Commit their work daily

---

## 📅 Daily Update Process

### Each Day (Before Interns Wake Up)

1. Open DAILY_TASKS.md locally
2. Find the section marked `## [COMING TOMORROW - Day X]`
3. Replace with that day's full tasks (copy from your detailed notes)
4. Keep all previous days unchanged
5. Update the "Status" line at bottom
6. Commit and push:

```bash
git add DAILY_TASKS.md
git commit -m "Day 3: Tasks updated - Phase 2 now live"
git push origin main
```

### Interns Will See

When they refresh GitHub or pull:
```bash
git pull origin main
```

They'll see the new tasks for the day. Simple!

---

## 📝 Example: Your First Update (Tomorrow - Day 1)

**Tomorrow morning:**

1. Open `DAILY_TASKS.md`
2. Find this section:
   ```
   ## ⏭️ DAY 0: SETUP & PREPARATION
   [... full tasks visible ...]

   ## [COMING TOMORROW - Day 3]
   ### Phase 2: Handle Missing Values & Duplicates (Days 3-4)
   ```

3. That stays the same (Day 0 and Phase 2 preview)

4. Find:
   ```
   ## [COMING TOMORROW - Day 3]

   ### Phase 2: Handle Missing Values & Duplicates (Days 3-4)

   Tasks for Days 3-4 will be posted tomorrow. Come back to this document to see your new tasks.
   ```

5. You already wrote:
   ```
   ## 🔶 PHASE 2: DATA PROFILING & ISSUE IDENTIFICATION

   ## 📅 DAYS 3-4: Handle Missing Values & Duplicates

   **Status:** Days 3-4 (Wed-Thu)  
   **Time Required:** 8-10 hours  
   **Objective:** Remove corrupted data, handle nulls, eliminate duplicates

   ### Task 2.1: Create Phase 2 Notebook
   [Full detailed task with code examples]

   ### Task 2.2: Analyze Missing Values
   [Full detailed task with code examples]

   [... etc ...]
   ```

6. Copy that section and replace the placeholder

7. Update status line:
   ```
   **Status:** ACTIVE PROGRAM - DAYS 1-2 TASKS LIVE (Day 0 Complete) ✅
   ```

8. Push to GitHub:
   ```bash
   git add DAILY_TASKS.md
   git commit -m "Day 1: Phase 1 profiling tasks now live"
   git push origin main
   ```

9. Interns will refresh and see:
   - ✅ Day 0 setup (complete)
   - ✅ Days 1-2 Phase 1 (new tasks for today)
   - ⏳ Days 3-4 Phase 2 (coming in 2 days - preview)

---

## 🎯 The Magic

**Why this works:**

1. **Interns don't get overwhelmed** — They only see current + next day's tasks
2. **You have time to prepare** — You write detailed tasks in advance, copy them each day
3. **Progress is visible** — Each day new tasks appear, showing forward movement
4. **Reference is available** — All previous days stay visible if they need to debug or review
5. **Git history shows growth** — Daily commits prove daily progress

---

## ✅ Pre-Upload Checklist

Before pushing to GitHub:

- [ ] DAILY_TASKS.md has complete Day 0 tasks
- [ ] DAILY_TASKS.md has complete Days 1-2 Phase 1 tasks
- [ ] DAILY_TASKS.md has Days 3-4 Phase 2 preview
- [ ] START_HERE.md is clear and welcoming
- [ ] README.md explains the program
- [ ] shops_raw_data_10k.csv is in `data/raw/`
- [ ] shops_raw_data_25k.csv is in `data/raw/`
- [ ] .gitignore prevents large files (already included in DAILY_TASKS.md notes)
- [ ] All files are UTF-8 encoded
- [ ] No sensitive data in files

---

## 🔄 What Happens After Upload

### Day 0 (Today)
- Upload repository with Day 0 + Day 1-2 preview
- Interns clone repo and read START_HERE.md

### Day 1 (Tomorrow)
- Interns see DAILY_TASKS.md with Day 1 instructions
- They work through tasks
- Evening: You update DAILY_TASKS.md for Day 2 + preview Day 3-4

### Day 2
- Interns see Day 2 tasks (you updated yesterday)
- They complete Phase 1
- Evening: You update DAILY_TASKS.md for Days 3-4 Phase 2

### Days 3-12
- Same pattern: Update file each evening with next day's tasks
- Interns pull latest updates in morning
- Work through new tasks
- By Day 12: Full 7-day project in one GitHub file

---

## 💡 Tips

### For Large CSV Files
GitHub has a 100MB file limit per file. Your CSVs are:
- 10k: 3.91 MB ✅ Safe
- 25k: 9.88 MB ✅ Safe

Both are well under the limit.

### Keep .gitignore Updated
Interns will create large files. Add to `.gitignore`:
```
*.xlsx
*.db
*.db-journal
*.png
*.jpg
```

### Make Commits Clear
Your commit messages should be:
```bash
# Good:
"Day 1: Phase 1 profiling tasks now live"
"Day 3: Phase 2 tasks added"
"Day 12: Program complete - all phases published"

# Bad:
"update"
"changes"
"fixed"
```

---

## 🎓 The Final Result

**What interns will see on Day 12:**

One long GitHub file showing:
- ✅ Day 0: Setup (complete)
- ✅ Days 1-2: Phase 1 Profiling (complete)
- ✅ Days 3-4: Phase 2 Missing Values (complete)
- ✅ Days 5-6: Phase 3 Standardization (complete)
- ✅ Days 7-8: Phase 4 Validation (complete)
- ✅ Days 9-11: Phase 5 SQL Analysis (complete)
- ✅ Day 12: Phase 6 Dashboard (complete)

**Plus:** Their cloned repository with all their work, Git commits, and final deliverables.

**They can show this to employers and say:** "Here's my 7-day data engineering project with complete documentation."

---

## 📞 Questions?

Refer to `TRAINER_DAILY_UPDATE_TEMPLATE.md` for detailed guidance on updating the file each day.

---

**Ready to upload? Let's go! 🚀**

**Next steps:**
1. Create GitHub repository
2. Upload files using instructions above
3. Share link with interns
4. Tell them to start with START_HERE.md
5. Tomorrow: Update DAILY_TASKS.md with Day 1-2 full tasks
6. Repeat daily for 7 days

