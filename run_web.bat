@echo off
:: بررسی نصب Python
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed or not added to PATH. Please install Python and try again.
    pause
    exit /b 1
)

:: نصب پیش‌نیازها (در صورت نیاز)
echo Installing required Python packages...
pip install -r requirements.txt

:: اجرای وب اپلیکیشن
echo Starting Whisper Web Application...
python web/app.py
if errorlevel 1 (
    echo There was an error running the web application. Please check the script and try again.
    pause
    exit /b 1
)

pause