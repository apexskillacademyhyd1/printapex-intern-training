# Daily GitHub Push Script for Intern Training Program
# Usage: .\daily_push.ps1

# Navigate to project
$projectPath = "C:\Users\ABDUL\Documents\Printing Automation\INTERN_TRAINING_PROGRAM"
cd $projectPath

# Check if we're in a git repo
if (-not (Test-Path ".git")) {
    Write-Host "ERROR: Not a git repository!" -ForegroundColor Red
    exit
}

# Show current status
Write-Host "`n=== GIT STATUS ===" -ForegroundColor Green
git status

# Ask user if they want to proceed
$confirm = Read-Host "`nReady to push changes to GitHub? (yes/no)"

if ($confirm -eq "yes" -or $confirm -eq "y") {
    # Stage all changes
    Write-Host "Staging changes..." -ForegroundColor Yellow
    git add .
    
    # Get commit message from user
    Write-Host "`nEnter your commit message (e.g., 'Day 3: Add validation tasks')" -ForegroundColor Cyan
    $message = Read-Host "Message"
    
    if ($message -eq "") {
        $message = "Daily update: $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
    }
    
    # Commit
    Write-Host "Creating commit..." -ForegroundColor Yellow
    git commit -m $message
    
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Commit failed or nothing to commit." -ForegroundColor Red
        exit
    }
    
    # Push
    Write-Host "Pushing to GitHub..." -ForegroundColor Yellow
    git push origin main
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "`n✓ Successfully pushed to GitHub!" -ForegroundColor Green
        Write-Host "Interns can now see the new tasks." -ForegroundColor Green
    } else {
        Write-Host "`n✗ Push failed. Check your internet connection." -ForegroundColor Red
    }
} else {
    Write-Host "`nPush cancelled." -ForegroundColor Red
}

# Keep window open so user can see the output
Read-Host "`nPress Enter to close"
