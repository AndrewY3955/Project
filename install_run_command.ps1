$ErrorActionPreference = "Stop"

$ProfilePath = $PROFILE.CurrentUserCurrentHost
$ProfileDirectory = Split-Path -Parent $ProfilePath
if (-not (Test-Path $ProfileDirectory)) {
    New-Item -ItemType Directory -Path $ProfileDirectory -Force | Out-Null
}

$BeginMarker = "# BEGIN PROJECT_DASHBOARD_RUN_MACRO"
$EndMarker = "# END PROJECT_DASHBOARD_RUN_MACRO"
$Block = @'
# BEGIN PROJECT_DASHBOARD_RUN_MACRO
function run {
    $directory = (Get-Location).Path
    while ($directory) {
        $launcher = Join-Path $directory "run_dashboard.ps1"
        if (Test-Path $launcher) {
            & $launcher @args
            return
        }
        $parent = Split-Path -Parent $directory
        if (-not $parent -or $parent -eq $directory) {
            break
        }
        $directory = $parent
    }
    throw "Could not find run_dashboard.ps1. Change to the cloned project directory and run 'run' again."
}
# END PROJECT_DASHBOARD_RUN_MACRO
'@

$ProfileContent = ""
if (Test-Path $ProfilePath) {
    $ProfileContent = Get-Content -LiteralPath $ProfilePath -Raw
}

$EscapedBegin = [regex]::Escape($BeginMarker)
$EscapedEnd = [regex]::Escape($EndMarker)
$ManagedBlock = "(?s)$EscapedBegin.*?$EscapedEnd\r?\n?"
if ($ProfileContent -match $ManagedBlock) {
    $ProfileContent = [regex]::Replace($ProfileContent, $ManagedBlock, "")
}
$LegacyBlock = "(?ms)^# PROJECT_DASHBOARD_RUN_MACRO\r?\nfunction run \{.*?^\}\r?\n?"
if ($ProfileContent -match $LegacyBlock) {
    $ProfileContent = [regex]::Replace($ProfileContent, $LegacyBlock, "")
}

$UpdatedProfile = ($ProfileContent.TrimEnd() + "`r`n`r`n" + $Block + "`r`n").TrimStart()
Set-Content -LiteralPath $ProfilePath -Value $UpdatedProfile -Encoding utf8
. $ProfilePath
Write-Host "Installed the portable 'run' command in $ProfilePath."
Write-Host "From any directory inside a cloned project, run: run"
