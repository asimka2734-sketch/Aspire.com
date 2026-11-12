@echo off
title Push Aspire College Website to GitHub
cd /d "%~dp0"

echo =========================================================
echo    Pushing Aspire College Website to GitHub
echo    Repository: https://github.com/asimka2734-sketch/Aspire.com.git
echo =========================================================
echo.

git status
echo.
echo Pushing branch 'main' to GitHub...
git push -u origin main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo =========================================================
    echo [SUCCESS] Website successfully uploaded to GitHub!
    echo View repository at: https://github.com/asimka2734-sketch/Aspire.com
    echo =========================================================
) else (
    echo.
    echo [ERROR] Push failed. If you need to log in to GitHub, please authorize in the prompt above.
)

echo.
pause
