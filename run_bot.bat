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

:: اجرای ربات تلگرام
echo Starting Telegram Whisper Bot...
python bot/telegram_bot.py
if errorlevel 1 (
    echo There was an error running the bot. Please check the script and try again.
    pause
    exit /b 1
)

pause