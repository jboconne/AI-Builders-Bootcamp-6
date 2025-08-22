@echo off
echo ========================================
echo File Text Extractor - Windows Installer
echo ========================================
echo.

echo This script will install dependencies step by step.
echo Press any key to continue...
pause >nul

echo.
echo Installing dependencies...
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

echo Python found. Installing dependencies...
echo.

REM Run the Python installation script
python install_dependencies.py

echo.
echo Installation complete!
echo.
echo If you encountered any errors, try:
echo 1. Running: pip install -r requirements_extractor_alternative.txt
echo 2. Installing packages individually
echo 3. Checking the troubleshooting section in README_extractor.md
echo.
pause
