# Voltora EV Mobility Platform PowerShell Launcher
Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "   Voltora EV Mobility Platform Launcher" -ForegroundColor Green
Write-Host "========================================================" -ForegroundColor Cyan

# 1. Clear ports 8000 & 3000
Write-Host "[1/3] Checking and clearing ports 8000 and 3000..." -ForegroundColor Yellow
$ports = @(8000, 3000)
foreach ($p in $ports) {
    $conn = Get-NetTCPConnection -LocalPort $p -ErrorAction SilentlyContinue
    if ($conn) {
        $pids = $conn | Select-Object -ExpandProperty OwningProcess -Unique
        foreach ($procId in $pids) {
            Stop-Process -Id $procId -Force -ErrorAction SilentlyContinue
        }
    }
}

$root = $PSScriptRoot

# 2. Start Django backend
Write-Host "[2/3] Starting Django backend..." -ForegroundColor Yellow
Start-Process cmd.exe -ArgumentList "/k cd /d `"$root\backend`" && ..\backend_venv\Scripts\python.exe manage.py runserver 0.0.0.0:8000"

# 3. Start Next.js frontend
Write-Host "[3/3] Starting Next.js frontend..." -ForegroundColor Yellow
Start-Process cmd.exe -ArgumentList "/k cd /d `"$root\frontend`" && npm.cmd run dev"

Write-Host ""
Write-Host "Voltora Platform is now starting in separate windows!" -ForegroundColor Green
Write-Host "  Frontend: http://localhost:3000" -ForegroundColor White
Write-Host "  Backend:  http://localhost:8000/api/docs/" -ForegroundColor White
Write-Host "  Admin:    http://localhost:8000/admin/" -ForegroundColor White
Write-Host ""

