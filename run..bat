@echo off
:: نصب پیش‌نیازهای Python و Whisper
echo Installing prerequisites...
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install git+https://github.com/openai/whisper.git

:: ایجاد پوشه کش برای مدل‌ها
set "MODEL_DIR=%USERPROFILE%\.cache\whisper"
if not exist "%MODEL_DIR%" (
    mkdir "%MODEL_DIR%"
)

:: دانلود مدل بزرگ (Large) اگر قبلاً دانلود نشده
set "MODEL_PATH=%MODEL_DIR%\large.pt"
if not exist "%MODEL_PATH%" (
    echo Downloading Whisper large model...
    curl -L -o "%MODEL_PATH%" https://huggingface.co/openai/whisper-large/resolve/main/pytorch_model.bin
    if errorlevel 1 (
        echo Failed to download the model. Please check your internet connection.
        exit /b 1
    )
) else (
    echo Whisper large model already exists.
)

:: دریافت مسیر فایل صوتی از کاربر
set /p "AUDIO_FILE=Enter the path to your audio file (e.g., input_audio.mp3): "

:: بررسی وجود فایل صوتی
if not exist "%AUDIO_FILE%" (
    echo The audio file "%AUDIO_FILE%" does not exist. Please check the path.
    exit /b 1
)

:: تبدیل فایل صوتی به متن
echo Transcribing audio file...
whisper "%AUDIO_FILE%" --language fa --model large
if errorlevel 1 (
    echo Failed to transcribe the audio file. Please check your setup.
    exit /b 1
)

echo Transcription completed successfully!
pause