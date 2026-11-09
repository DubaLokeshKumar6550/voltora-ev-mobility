@echo off
title Voltora EV Mobility Platform Launcher
echo ========================================================
echo   Voltora EV Platform - Starting Services
echo ========================================================
echo.

:: 1. Clean up any lingering processes on ports 8000 and 3000
echo [1/3] Ensuring ports 8000 and 3000 are ready...
for /f "tokens=5" %%a in ('netstat -aon ^| findstr ":8000 "') do (
    if not "%%a"=="" taskkill /f /pid %%a >nul 2>&1
)
for /f "tokens=5" %%a in ('netstat -aon ^| findstr ":3000 "') do (
    if not "%%a"=="" taskkill /f /pid %%a >nul 2>&1
)

:: 2. Launch Django Backend
echo [2/3] Starting Django REST Backend on http://localhost:8000 ...
start "Voltora Backend API (Port 8000)" cmd /k "cd /d "%~dp0backend" && ..\backend_venv\Scripts\python.exe manage.py runserver 0.0.0.0:8000"

:: 3. Launch Next.js Frontend
echo [3/3] Starting Next.js Frontend on http://localhost:3000 ...
start "Voltora Frontend (Port 3000)" cmd /k "cd /d "%~dp0frontend" && npm.cmd run dev"

echo.
echo ========================================================
echo   Voltora Platform is now running in 2 terminal windows!
echo ========================================================
echo   - Frontend Web:  http://localhost:3000
echo   - Backend API:   http://localhost:8000/api/docs/
echo   - Admin Portal:  http://localhost:8000/admin/
echo ========================================================
echo.
echo Press any key to exit this launcher window (servers stay open)...
pause >nul
