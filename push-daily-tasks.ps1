# ============================================================================
# DAILY INTERN TRAINING TASK PUSH SCRIPT
# ============================================================================
# This script commits and pushes daily tasks to the intern training repository.
# Modify the variables below for each day's push.
# ============================================================================

# ──────────────────────────────────────────────────────────────────────────
# CONFIGURATION - UPDATE THESE FOR EACH DAY
# ──────────────────────────────────────────────────────────────────────────

# Day number (e.g., 3, 4, 5...)
$DAY_NUMBER = 3  # ← CHANGE THIS FOR EACH DAY

# Short description of what tasks were added (keep it concise)
$TASK_DESCRIPTION = "data validation and error handling tasks"  # ← CHANGE THIS

# Detailed description for commit message (optional, can be multi-line)
$DETAILED_DESCRIPTION = @"
Added tasks covering:
- Input validation techniques
- Error handling patterns
- Data sanitization methods
- Edge case testing
"@  # ← CHANGE THIS

# ──────────────────────────────────────────────────────────────────────────
# SCRIPT EXECUTION - NO NEED TO MODIFY BELOW THIS LINE
# ──────────────────────────────────────────────────────────────────────────

# Colors for output
$GREEN = "Green"
$RED = "Red"
$YELLOW = "Yellow"
$CYAN = "Cyan"

# Get script directory (INTERN_TRAINING_PROGRAM folder)
$SCRIPT_DIR = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $SCRIPT_DIR

Write-Host "`n╔════════════════════════════════════════════════════════════════╗" -ForegroundColor $CYAN
Write-Host "║  INTERN TRAINING - DAY $DAY_NUMBER TASK PUSH                             ║" -ForegroundColor $CYAN
Write-Host "╚════════════════════════════════════════════════════════════════╝`n" -ForegroundColor $CYAN

# Check if we're in a git repository
if (-not (Test-Path ".git")) {
    Write-Host "✗ ERROR: Not a git repository!" -ForegroundColor $RED
    Write-Host "  Current directory: $SCRIPT_DIR" -ForegroundColor $YELLOW
    exit 1
}

# Show current status
Write-Host "📁 Repository: INTERN_TRAINING_PROGRAM" -ForegroundColor $CYAN
Write-Host "📅 Day: $DAY_NUMBER" -ForegroundColor $CYAN
Write-Host "📝 Description: $TASK_DESCRIPTION`n" -ForegroundColor $CYAN

# Check git status
Write-Host "──────────────────────────────────────────────────────────────" -ForegroundColor $YELLOW
Write-Host "Checking git status..." -ForegroundColor $YELLOW
Write-Host "──────────────────────────────────────────────────────────────`n" -ForegroundColor $YELLOW

git status --short

if ($LASTEXITCODE -ne 0) {
    Write-Host "`n✗ ERROR: Git status check failed!" -ForegroundColor $RED
    exit 1
}

# Confirm before proceeding
Write-Host "`n──────────────────────────────────────────────────────────────" -ForegroundColor $YELLOW
$confirmation = Read-Host "Do you want to stage ALL changes and push Day $DAY_NUMBER tasks? (yes/no)"
Write-Host "──────────────────────────────────────────────────────────────`n" -ForegroundColor $YELLOW

if ($confirmation -ne "yes") {
    Write-Host "✗ Push cancelled by user." -ForegroundColor $YELLOW
    exit 0
}

# Stage all changes
Write-Host "📦 Staging all changes..." -ForegroundColor $CYAN
git add .

if ($LASTEXITCODE -ne 0) {
    Write-Host "✗ ERROR: Failed to stage changes!" -ForegroundColor $RED
    exit 1
}

Write-Host "✓ Changes staged successfully`n" -ForegroundColor $GREEN

# Create commit message
$COMMIT_MESSAGE = @"
feat: add Day $DAY_NUMBER intern training tasks - $TASK_DESCRIPTION

$DETAILED_DESCRIPTION

Tasks are now available for interns to begin Day $DAY_NUMBER work.
"@

# Commit changes
Write-Host "💾 Creating commit..." -ForegroundColor $CYAN
git commit -m $COMMIT_MESSAGE

if ($LASTEXITCODE -ne 0) {
    Write-Host "✗ ERROR: Failed to create commit!" -ForegroundColor $RED
    Write-Host "  (This might mean there are no changes to commit)" -ForegroundColor $YELLOW
    exit 1
}

Write-Host "✓ Commit created successfully`n" -ForegroundColor $GREEN

# Push to remote
Write-Host "🚀 Pushing to remote repository..." -ForegroundColor $CYAN
git push origin main

if ($LASTEXITCODE -ne 0) {
    Write-Host "`n✗ ERROR: Failed to push to remote!" -ForegroundColor $RED
    Write-Host "  You may need to pull first if there are remote changes." -ForegroundColor $YELLOW
    exit 1
}

Write-Host "`n✓ Successfully pushed Day $DAY_NUMBER tasks to remote repository!`n" -ForegroundColor $GREEN

# Show final status
Write-Host "══════════════════════════════════════════════════════════════" -ForegroundColor $GREEN
Write-Host "  Day $DAY_NUMBER tasks are now live!" -ForegroundColor $GREEN
Write-Host "  Interns can pull and begin working on: $TASK_DESCRIPTION" -ForegroundColor $GREEN
Write-Host "══════════════════════════════════════════════════════════════`n" -ForegroundColor $GREEN

# Optional: Show last commit
Write-Host "Last commit:" -ForegroundColor $CYAN
git log -1 --oneline

Write-Host "`n✓ Done!`n" -ForegroundColor $GREEN
