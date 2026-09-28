# ============================================================================
# QUICK DAILY TASK PUSH - Edit day number and description, then run
# ============================================================================

# EDIT THESE TWO LINES FOR EACH DAY
$DAY = 3
$DESCRIPTION = "Data cleaning and analysis"

# ============================================================================
# Script starts here - no need to edit below
# ============================================================================

Set-Location "C:\Users\ABDUL\Documents\Printing Automation\INTERN_TRAINING_PROGRAM"

Write-Host ""
Write-Host "Pushing Day $DAY tasks: $DESCRIPTION" -ForegroundColor Cyan
Write-Host ""

git add .
git commit -m "Day ${DAY}: $DESCRIPTION"
git push origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "Day $DAY tasks pushed successfully!" -ForegroundColor Green
    Write-Host ""
} else {
    Write-Host ""
    Write-Host "Push failed. Check errors above." -ForegroundColor Red
    Write-Host ""
}
