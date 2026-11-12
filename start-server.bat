@echo off
title Aspire College Taunsa - Localhost Web Server
cd /d "%~dp0"

echo =========================================================
echo    Aspire College Taunsa - Starting Local Server
echo =========================================================
echo.

:: Try starting with Python first
python --version >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo Starting server with Python...
    start "" "http://localhost:8000"
    python server.py 8000 --no-browser
    goto end
)

:: Try Node.js if Python is not found
node --version >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo Starting server with Node.js...
    start "" "http://localhost:8000"
    node server.js
    goto end
)

echo [ERROR] Neither Python nor Node.js was found in your PATH.
echo Please install Python (https://www.python.org/) or Node.js (https://nodejs.org/) to run the local server.
pause

:end
