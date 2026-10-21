param(
    [int]$Port = 8765,
    [switch]$NoBrowser
)

$ErrorActionPreference = "Stop"
$Launcher = Join-Path $PSScriptRoot "run_dashboard.ps1"
& $Launcher -Port $Port -NoBrowser:$NoBrowser
if ($LASTEXITCODE -ne 0) {
    throw "Dashboard command exited with code $LASTEXITCODE."
}
