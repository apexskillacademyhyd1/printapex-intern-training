# Day 0 — Complete Setup Guide

Welcome. This guide is for you if you've never used Python, Git, or Jupyter before.

Don't worry. We'll go through everything step by step.

Your job today is to install the tools and verify they work. That's it.

By the end of Day 0, you'll be ready to start the actual data analytics work on Day 1.

---

## Before You Start

**Read this first.**

### Follow steps in order

Go from Step 1 → Step 2 → Step 3. Don't skip.

### When you see this:

```
TYPE THIS
```

Type the command exactly as shown. Don't change anything.

### When you see this:

```
EXPECTED RESULT
```

Check whether your computer shows something similar. If not, tell your mentor.

### If something breaks

Take a screenshot of the error. Send it to your mentor. Do not randomly try commands from the internet.

---

## What You're Installing Today

| Tool | What it does | Why you need it |
|------|-------------|-----------------|
| **Python** | A programming language | This is what you'll use to analyze data |
| **Git** | Tracks changes to your work | Keeps a history of everything you do. Required for the internship. |
| **Jupyter Notebook** | An interactive workspace | You write Python code here. It shows results instantly. |
| **pandas** | A data library | Reads CSV files and lets you work with data like a spreadsheet |
| **matplotlib** | A charting library | Creates line charts, bar charts, scatter plots, etc. |
| **seaborn** | An advanced charting library | Makes prettier, more professional charts |
| **Excel** | Spreadsheet software | You'll use this later for the final dashboard |

All of these are free. Everything except Excel comes pre-installed or installs through Python.

---

## Step 0 — Check Your System

These instructions are for **Windows 10 or Windows 11**.

If you use macOS or Linux, ask your mentor for different instructions.

---

## Step 1 — Install Python

### 1.1 Open the Python website

Go to:

https://www.python.org/downloads/

### 1.2 Download Python

Look for the big yellow download button. Click it.

For most Windows computers, download:

**Python 3.12** (or the latest 3.x version)

The file will be something like `python-3.12.x-amd64.exe`

### 1.3 Install Python

Open the file you downloaded.

**IMPORTANT:** When you see this checkbox:

```
Add Python to PATH
```

**CHECK THE BOX.** This is critical.

If you don't check it, Python won't work from the terminal.

Then click **Install Now** and wait for it to finish.

---

## Step 1.4 — Verify Python Works

Open PowerShell:

1. Press the **Windows key** on your keyboard
2. Type: `PowerShell`
3. Click **Windows PowerShell**

You should see a black window that says something like:

```
PS C:\Users\YourName>
```

Now type this:

```
python --version
```

Press **Enter**.

### Expected Result

You should see:

```
Python 3.12.x
```

(The exact version number may be different.)

If you see this, Python installed correctly.

If you see:

```
'python' is not recognized
```

Close PowerShell. Open a **new** PowerShell window and try again. If it still doesn't work, tell your mentor.

---

## Step 2 — Install Git

### 2.1 Open the Git website

Go to:

https://git-scm.com/download/win

### 2.2 Download Git

Click the download button for **64-bit Git for Windows Setup**.

The file will be something like `Git-2.x.x-64-bit.exe`

### 2.3 Install Git

Open the file.

For most screens, you can just click **Next**.

When you reach **Install**, click it and wait.

Then click **Finish**.

---

## Step 2.4 — Verify Git Works

Close PowerShell if it's open. Open a **new** PowerShell window.

Type:

```
git --version
```

Press **Enter**.

### Expected Result

You should see:

```
git version 2.x.x
```

(The exact version may be different.)

If you see a version number, Git is installed correctly.

---

## Step 3 — Create Your Project Folder

### 3.1 Open PowerShell

Press **Windows key**, type `PowerShell`, and open it.

### 3.2 Navigate to Desktop

Type:

```
cd $HOME\Desktop
```

Press **Enter**.

This moves you to your Desktop folder.

### 3.3 Check your location

Type:

```
pwd
```

Press **Enter**.

You should see something like:

```
C:\Users\YourName\Desktop
```

---

## Step 4 — Create Your Project

### 4.1 Create the project folder

Type:

```
mkdir PrintShopDataProject
```

Press **Enter**.

This creates a folder called `PrintShopDataProject`.

### 4.2 Enter the folder

Type:

```
cd PrintShopDataProject
```

Press **Enter**.

### 4.3 Verify your location

Type:

```
pwd
```

You should now see:

```
C:\Users\YourName\Desktop\PrintShopDataProject
```

Good. You're inside your project.

---

## Step 5 — Initialize Git

### 5.1 Set up Git for this project

Type:

```
git init
```

Press **Enter**.

### Expected Result

You should see:

```
Initialized empty Git repository in ...
```

This means Git is now tracking this folder.

### 5.2 Tell Git who you are

Git needs your name and email. Type:

```
git config user.name "Your Name"
```

Replace `Your Name` with your actual name. For example:

```
git config user.name "Rahul Kumar"
```

Press **Enter**.

Then type:

```
git config user.email "your.email@example.com"
```

Replace with your actual email. For example:

```
git config user.email "rahul.kumar@example.com"
```

Press **Enter**.

### 5.3 Verify your Git settings

Type:

```
git config user.name
```

You should see your name.

Type:

```
git config user.email
```

You should see your email.

Good. Git knows who you are now.

---

## Step 6 — Create Your Project Folders

We need to organize your project like this:

```
PrintShopDataProject
│
├── data
│   ├── raw
│   ├── cleaned
│   └── processed
│
├── notebooks
├── scripts
├── sql
└── output
    └── charts
```

We'll create these using PowerShell.

### 6.1 Create the main folders

Type:

```
mkdir data, notebooks, scripts, sql, output
```

Press **Enter**.

### 6.2 Create the subfolders

Type:

```
mkdir data\raw, data\cleaned, data\processed, output\charts
```

Press **Enter**.

### 6.3 Verify the structure

Type:

```
tree /f
```

Press **Enter**.

You should see all your folders listed. If yes, you're good.

---

## Step 7 — Create a Python Virtual Environment

A **virtual environment** is a private Python workspace for this project.

Think of it like this:

> Your computer is a building.
>
> Your project gets its own room.
>
> Python packages installed in that room belong to this project only.
>
> This prevents different projects from interfering with each other.

### 7.1 Create the environment

Make sure you're still in `PrintShopDataProject`.

Type:

```
python -m venv venv
```

Press **Enter**.

Wait a few seconds. This creates a folder called `venv`.

### 7.2 Activate the environment

Type:

```
.\venv\Scripts\Activate.ps1
```

Press **Enter**.

### Expected Result

Your PowerShell prompt should now start with `(venv)`:

```
(venv) PS C:\Users\YourName\Desktop\PrintShopDataProject>
```

This means the virtual environment is active.

### If PowerShell shows an error about execution policy

You may see:

```
running scripts is disabled on this system
```

If so, type:

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Press **Enter**.

PowerShell will ask:

```
Do you want to change the execution policy?
```

Type `Y` and press **Enter**.

Then activate the environment again:

```
.\venv\Scripts\Activate.ps1
```

You should now see `(venv)` in your prompt.

---

## Step 8 — Install Python Libraries

We need to install four Python libraries:

- **pandas** - Reads and works with data files
- **jupyter** - The interactive notebook where you'll write code
- **matplotlib** - Creates charts
- **seaborn** - Creates prettier charts

### 8.1 Upgrade pip first

`pip` is Python's package installer. We'll use it to install everything.

Make sure you see `(venv)` in your prompt.

Type:

```
python -m pip install --upgrade pip
```

Press **Enter**.

Wait for it to finish.

### 8.2 Install the libraries

Type:

```
pip install pandas jupyter matplotlib seaborn
```

Press **Enter**.

This will take a few minutes. You'll see a lot of text. That's normal. Don't close PowerShell.

### 8.3 Verify pandas installed

Type:

```
python -c "import pandas; print(pandas.__version__)"
```

Press **Enter**.

You should see a version number like `2.1.x`

### 8.4 Verify jupyter installed

Type:

```
jupyter --version
```

Press **Enter**.

You should see version numbers for Jupyter components.

### 8.5 Verify matplotlib installed

Type:

```
python -c "import matplotlib; print(matplotlib.__version__)"
```

Press **Enter**.

You should see a version number.

### 8.6 Verify seaborn installed

Type:

```
python -c "import seaborn; print(seaborn.__version__)"
```

Press **Enter**.

You should see a version number.

If all four commands returned version numbers, all your libraries are installed.

---

## Step 9 — Create .gitignore

We don't want certain files committed to Git:

- Excel files (large and personal)
- Database files
- The virtual environment folder
- Jupyter temporary files

We'll create a file called `.gitignore` to tell Git to ignore these.

### 9.1 Create the file

In PowerShell (you should still be in `PrintShopDataProject`), type:

```
notepad .gitignore
```

Press **Enter**.

A text editor will open. Paste this:

```
*.xlsx
*.db
venv/
__pycache__/
.ipynb_checkpoints/
```

This tells Git:

- Don't commit any `.xlsx` files (Excel files - large and personal)
- Don't commit any `.db` files (databases)
- Don't commit the `venv/` folder (virtual environment)
- Don't commit `__pycache__/` (Python cache)
- Don't commit `.ipynb_checkpoints/` (Jupyter temporary files)

**Important:** We DO NOT ignore `*.csv` files because this training data is synthetic and safe to commit to Git. Your data cleaning work will be part of your Git history.

### 9.2 Save the file

Press **Ctrl + S** to save.

Then close Notepad.

### 9.3 Verify the file exists

Type:

```
dir
```

Press **Enter**.

You should see `.gitignore` in the list.

---

## Step 10 — Download the Data

The dataset for this project is stored on GitHub.

### 10.1 Open the GitHub page

Go to:

https://raw.githubusercontent.com/apexskillacademyhyd1/printapex-intern-training/main/shops_raw_data_10k.csv

This opens the raw CSV file.

### 10.2 Save the file

Right-click on the page and select **Save as**.

Or press **Ctrl + S**.

### 10.3 Name and location

Save it as:

```
shops_raw_data_10k.csv
```

Save it in this location:

```
PrintShopDataProject\data\raw
```

Your final path should be:

```
Desktop
└── PrintShopDataProject
    └── data
        └── raw
            └── shops_raw_data_10k.csv
```

### 10.4 Verify the file

In PowerShell, type:

```
dir data\raw
```

Press **Enter**.

You should see:

```
shops_raw_data_10k.csv
```

---

## Step 11 — Test Python Can Read the CSV

This is the most important test. If Python can't read the CSV, everything else doesn't matter.

Make sure you're in `PrintShopDataProject` and you see `(venv)` in your prompt.

Type:

```
python -c "import pandas as pd; df=pd.read_csv('data/raw/shops_raw_data_10k.csv'); print('CSV loaded successfully'); print(df.shape)"
```

Press **Enter**.

### Expected Result

You should see:

```
CSV loaded successfully
(10000, XX)
```

The first number will be around `10000`. The second number represents the number of columns.

If you see this, Python can read your data. Excellent.

---

## Step 12 — Verify Git is Tracking

Type:

```
git status
```

Press **Enter**.

You should see a list of files Git detected. You should **NOT** see `shops_raw_data_10k.csv` because we put `*.csv` in `.gitignore`.

That's correct. Your data should stay on your computer.

---

## Step 13 — Make Your First Git Commit

This saves your project state in Git history.

Type:

```
git add .
```

Press **Enter**.

This stages all files for commit (except those in `.gitignore`).

Then type:

```
git commit -m "Day 0: Initial project setup"
```

Press **Enter**.

### Expected Result

You should see something like:

```
[main (root-commit) xxxxx] Day 0: Initial project setup
```

This means your first commit was successful.

---

## Step 14 — Test Jupyter

Now we'll test that Jupyter Notebook works.

Type:

```
jupyter notebook
```

Press **Enter**.

### Expected Result

Your web browser should automatically open.

You should see a Jupyter Notebook interface.

You should see your project folders listed:

```
data
notebooks
scripts
sql
output
venv
```

This is correct.

### 14.1 Create your first notebook

Click the **notebooks** folder.

Then click **New** → **Python 3**.

A new notebook will open.

### 14.2 Rename it

At the top, click **Untitled**.

Rename it:

```
01_data_profiling
```

Press **Enter**.

### 14.3 Test Python code

In the first cell, type:

```python
print("Hello Printapex")
```

Press **Shift + Enter** (not just Enter).

### Expected Result

Below the cell, you should see:

```
Hello Printapex
```

If you see this, Python and Jupyter are working.

---

## Step 14.4 Test pandas

Create a new cell. Type:

```python
import pandas as pd
df = pd.read_csv('../data/raw/shops_raw_data_10k.csv')
print(df.shape)
```

Press **Shift + Enter**.

### Expected Result

You should see:

```
(10000, XX)
```

If you see this, you can load data. Perfect.

---

## Step 14.5 Close Jupyter

Go back to PowerShell.

Press **Ctrl + C** twice to stop Jupyter.

---

## Step 15 — Verify Your Project Structure

Your project should now look like this:

```
PrintShopDataProject
│
├── .git
├── .gitignore
│
├── data
│   ├── cleaned
│   ├── processed
│   └── raw
│       └── shops_raw_data_10k.csv
│
├── notebooks
│   └── 01_data_profiling.ipynb
│
├── scripts
├── sql
│
└── output
    └── charts

(and the venv folder, but it's hidden in many views)
```

---

## Step 16 — Final Verification

Run each of these commands in PowerShell. You should see version numbers for all of them.

### Python:

```
python --version
```

Expected: `Python 3.x.x`

### Git:

```
git --version
```

Expected: `git version 2.x.x`

### pandas:

```
python -c "import pandas; print('pandas: OK')"
```

Expected: `pandas: OK`

### Jupyter:

```
jupyter --version
```

Expected: Jupyter component versions

### CSV:

```
python -c "import pandas as pd; df=pd.read_csv('data/raw/shops_raw_data_10k.csv'); print('CSV: OK'); print(df.shape)"
```

Expected:

```
CSV: OK
(10000, XX)
```

### Git history:

```
git log --oneline
```

Expected:

```
xxxxx Day 0: Initial project setup
```

If all of these work, you're ready for Day 1.

---

## Step 17 — Save Your Work

Commit your notebook to Git:

Type:

```
git add notebooks/01_data_profiling.ipynb
```

Press **Enter**.

Then:

```
git commit -m "Day 0: First Jupyter notebook"
```

Press **Enter**.

---

## Important Notes

### About the 25k dataset

The current project provides only the `shops_raw_data_10k.csv` file. Your mentor will provide the 25k dataset later if needed.

Do not try to create your own 25k dataset.

### About the CSV file

Your `shops_raw_data_10k.csv` file is:

- On your computer
- Not committed to Git (because of `.gitignore`)
- Not uploaded anywhere
- Only visible to you locally

This is intentional. Production data should stay private.

### About the virtual environment

The `venv` folder is large. It's not committed to Git (because of `.gitignore`).

If you ever delete `venv` by accident, you can recreate it:

```
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install pandas jupyter matplotlib seaborn
```

### About Excel

If you don't have Excel installed, tell your mentor. We'll need it for the final dashboard.

---

## What You Just Accomplished

✅ Installed Python 3.12+

✅ Installed Git

✅ Created a project folder structure

✅ Initialized Git for your project

✅ Created a Python virtual environment

✅ Installed pandas (reads data)

✅ Installed Jupyter (interactive notebooks)

✅ Installed matplotlib (charts)

✅ Installed seaborn (prettier charts)

✅ Created `.gitignore` (protects sensitive files)

✅ Downloaded the project dataset

✅ Verified Python can read the CSV

✅ Created your first Jupyter notebook

✅ Made your first Git commits

You are now ready for Day 1.

---

## Day 1 — What's Next

Tomorrow you will open `DAILY_TASKS.md` on GitHub and see the Day 1 tasks.

Day 1 is about **inspecting** the data—not cleaning it yet. Just understanding what's inside.

Repository:

https://github.com/apexskillacademyhyd1/printapex-intern-training

Daily tasks:

https://github.com/apexskillacademyhyd1/printapex-intern-training/blob/main/DAILY_TASKS.md

---

## If Something Went Wrong

Do not panic. Tell your mentor immediately.

Include:

1. **Screenshot** of the error
2. **The command you typed**
3. **The exact error message**

Example:

```
COMMAND:
python --version

ERROR:
'python' is not recognized as an internal or external command
```

Your mentor has seen these errors before. They'll help you fix it.

---

## Most Important Rule

**If you don't understand a command, ask before you run it.**

You're learning a professional data workflow. Understanding each step is more important than just making it work.

Welcome to the internship.

Let's go.
