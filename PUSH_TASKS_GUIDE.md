# Daily Task Push Guide

## Quick Start

1. **Edit the script**: Open `push-daily-tasks.ps1`
2. **Update variables** (lines 11-23):
   - `$DAY_NUMBER` - The day number
   - `$TASK_DESCRIPTION` - Short description
   - `$DETAILED_DESCRIPTION` - Detailed description
3. **Run the script**: `.\push-daily-tasks.ps1`

---

## Day 3 Example (Current)

```powershell
$DAY_NUMBER = 3
$TASK_DESCRIPTION = "data validation and error handling tasks"
$DETAILED_DESCRIPTION = @"
Added tasks covering:
- Input validation techniques
- Error handling patterns
- Data sanitization methods
- Edge case testing
"@
```

---

## Day 4 Example Template

```powershell
$DAY_NUMBER = 4
$TASK_DESCRIPTION = "API integration and testing"
$DETAILED_DESCRIPTION = @"
Added tasks covering:
- RESTful API design
- API endpoint testing
- Authentication and authorization
- Error response handling
"@
```

---

## Day 5 Example Template

```powershell
$DAY_NUMBER = 5
$TASK_DESCRIPTION = "database operations and queries"
$DETAILED_DESCRIPTION = @"
Added tasks covering:
- SQL query optimization
- Database schema design
- Transaction management
- Index creation and usage
"@
```

---

## Day 6 Example Template

```powershell
$DAY_NUMBER = 6
$TASK_DESCRIPTION = "frontend components and styling"
$DETAILED_DESCRIPTION = @"
Added tasks covering:
- Component architecture
- CSS/styling best practices
- Responsive design
- Accessibility considerations
"@
```

---

## Usage Instructions

### Method 1: Edit and Run (Recommended)
1. Open `push-daily-tasks.ps1` in any text editor
2. Change the three variables at the top
3. Save the file
4. Run: `.\push-daily-tasks.ps1`

### Method 2: One-Line Command
If you prefer not to edit the file, run directly:

```powershell
# Example for Day 4
powershell -Command "
    $DAY_NUMBER = 4;
    $TASK_DESCRIPTION = 'API integration tasks';
    $DETAILED_DESCRIPTION = 'Added API-related tasks';
    cd 'C:\Users\ABDUL\Documents\Printing Automation\INTERN_TRAINING_PROGRAM';
    git add .;
    git commit -m 'feat: add Day 4 intern training tasks';
    git push origin main
"
```

---

## What the Script Does

1. ✓ Checks you're in the correct git repository
2. ✓ Shows current git status
3. ✓ Asks for confirmation before pushing
4. ✓ Stages all changes (`git add .`)
5. ✓ Creates a properly formatted commit message
6. ✓ Commits the changes
7. ✓ Pushes to remote repository
8. ✓ Shows success confirmation

---

## Example Workflow for Tomorrow (Day 4)

1. Create/update Day 4 tasks in `DAILY_TASKS.md`
2. Open `push-daily-tasks.ps1`
3. Update:
   ```powershell
   $DAY_NUMBER = 4
   $TASK_DESCRIPTION = "YOUR_DESCRIPTION_HERE"
   $DETAILED_DESCRIPTION = @"
   YOUR_DETAILED_DESCRIPTION_HERE
   "@
   ```
4. Save and run: `.\push-daily-tasks.ps1`
5. Type `yes` when prompted
6. Done! ✓

---

## Troubleshooting

### "Not a git repository" error
- Make sure you're running the script from the INTERN_TRAINING_PROGRAM folder
- Check that .git folder exists

### "Nothing to commit" error
- You haven't made any changes to commit
- Check `git status` to see if files were modified

### Push failed error
- Pull remote changes first: `git pull origin main`
- Then run the script again

### Permission denied
- Run PowerShell as Administrator, or
- Enable script execution: `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`

---

## Commit Message Format

The script generates this format:

```
feat: add Day X intern training tasks - [SHORT_DESCRIPTION]

[DETAILED_DESCRIPTION]

Tasks are now available for interns to begin Day X work.
```

---

## Tips

- **Be descriptive**: Make task descriptions clear for interns
- **Keep it consistent**: Use similar formatting for each day
- **Review before pushing**: Always check `git status` output
- **Test first**: Run on a test branch if unsure

---

## Need Help?

If the script isn't working:
1. Check you're in the right directory
2. Verify git is installed: `git --version`
3. Check git remote: `git remote -v`
4. Manually run commands to debug:
   ```powershell
   git status
   git add .
   git commit -m "test"
   git push origin main
   ```
