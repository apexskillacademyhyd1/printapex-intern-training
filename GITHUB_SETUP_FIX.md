# GitHub Setup Fix - Permission Denied Error

## Problem
When you tried to push to GitHub, you got this error:
```
Permission denied to azczefahanabdul
The requested URL returned error: 403
```

This means GitHub is rejecting the authentication. Here's how to fix it.

---

## Solution: Use GitHub Personal Access Token

GitHub no longer accepts passwords directly. You need a Personal Access Token (PAT).

### Step 1: Create a Personal Access Token on GitHub

1. Go to: https://github.com/settings/tokens
2. Click "Generate new token" → "Generate new token (classic)"
3. Set these permissions:
   - ✅ repo (full control of private/public repositories)
   - ✅ gist
4. Click "Generate token"
5. **COPY the token immediately** (you won't see it again)
6. Save it somewhere safe (you'll need it in 5 minutes)

### Step 2: Update Git to Use the Token

Open PowerShell and run:

```powershell
cd "C:\Users\ABDUL\Documents\Printing Automation\INTERN_TRAINING_PROGRAM"

# Change the remote URL to include your token
git remote remove origin

git remote add origin https://YOUR_GITHUB_USERNAME:YOUR_TOKEN@github.com/apexskillacademyhyd1/printapex-intern-training.git

# Replace:
# YOUR_GITHUB_USERNAME = your GitHub username (e.g., apexskillacademyhyd1)
# YOUR_TOKEN = the token you just generated (paste it here)
```

### Step 3: Try Push Again

```powershell
git push -u origin main
```

**Expected output:**
```
Counting objects: 5, done.
...
To https://github.com/apexskillacademyhyd1/printapex-intern-training.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

---

## Alternative: Use Git Credential Manager

If the above doesn't work, try this simpler approach:

### Step 1: Install Git Credential Manager for Windows

Download from: https://github.com/git-ecosystem/git-credential-manager/releases

Or if you have Chocolatey:
```powershell
choco install git-credential-manager
```

### Step 2: Configure Git

```powershell
git config --global credential.helper manager
```

### Step 3: Push to GitHub

```powershell
cd "C:\Users\ABDUL\Documents\Printing Automation\INTERN_TRAINING_PROGRAM"
git push -u origin main
```

A browser window will open asking you to authenticate with GitHub. Click "Authorize" and you're done.

---

## Quick Checklist

- [ ] Verify files are added: `git status`
- [ ] Commit is made: `git log --oneline` shows your commit
- [ ] Remote is set: `git remote -v` shows origin URL
- [ ] Create GitHub Personal Access Token
- [ ] Update remote URL with token OR use Git Credential Manager
- [ ] Try push: `git push -u origin main`
- [ ] Verify on GitHub: Go to https://github.com/apexskillacademyhyd1/printapex-intern-training and refresh

---

## If Still Having Issues

Try this simpler approach:

### Option A: Start Fresh (Recommended)

```powershell
# Delete the local git repo
cd "C:\Users\ABDUL\Documents\Printing Automation"
Remove-Item INTERN_TRAINING_PROGRAM\.git -Recurse -Force

# Go to GitHub and delete the repository if needed

# Create a new repo with a README first (from GitHub UI):
# 1. Go to GitHub.com
# 2. Click + icon → New repository
# 3. Name: printapex-intern-training
# 4. Create README during creation
# 5. Copy the generated .git folder commands

# Then in PowerShell:
cd "C:\Users\ABDUL\Documents\Printing Automation\INTERN_TRAINING_PROGRAM"
git init
git config user.name "Your Name"
git config user.email "your@email.com"
git add .
git commit -m "Initial: Day 0 tasks + datasets ready"
git branch -M main
git remote add origin https://YOUR_TOKEN@github.com/apexskillacademyhyd1/printapex-intern-training.git
git push -u origin main
```

### Option B: Use GitHub Desktop (Easiest for First-Time Users)

1. Download GitHub Desktop from: https://desktop.github.com
2. Sign in with your GitHub account
3. Click "Add" → "Clone repository"
4. Search for: printapex-intern-training
5. Clone to: `C:\Users\ABDUL\Documents\Printing Automation`
6. Copy your files into the cloned folder
7. In GitHub Desktop: See changes, add message, commit
8. Click "Push origin" button

---

## What Happens After You Push Successfully

Once push succeeds, you'll see:

**On GitHub:**
- https://github.com/apexskillacademyhyd1/printapex-intern-training
- Files visible: DAILY_TASKS.md, START_HERE.md, README.md
- Folder visible: data/raw/ with CSV files
- "Initial: Day 0 tasks..." commit visible in history

**Now you can:**
1. Share link with interns
2. They clone the repo
3. They see DAILY_TASKS.md with Day 0 tasks
4. Tomorrow: You update the file with Day 1-2 tasks

---

## Next Steps

1. Choose one solution above (Personal Access Token or GitHub Desktop)
2. Complete the push
3. Verify on GitHub
4. Share link with interns: https://github.com/apexskillacademyhyd1/printapex-intern-training
5. Tell interns to:
   - Clone or download the repo
   - Read START_HERE.md
   - Start Day 0 tasks from DAILY_TASKS.md

---

**You've got this! Once push succeeds, everything else is smooth sailing.** 🚀

