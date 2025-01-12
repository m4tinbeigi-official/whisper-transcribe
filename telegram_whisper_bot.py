import os
import whisper
from pydub import AudioSegment
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# مدل Whisper را لود کن
print(Loading Whisper model...)
model = whisper.load_model(large)
print(Model loaded successfully.)

# تبدیل فایل OGG به WAV (برای فایل‌های تلگرام)
def convert_audio_to_wav(input_path, output_path)
    audio = AudioSegment.from_file(input_path)
    audio.export(output_path, format=wav)

# پردازش صدا و تبدیل به متن
def transcribe_audio(audio_path)
    result = model.transcribe(audio_path, language=fa)
    return result[text]

# پاسخ به پیام صوتی
def handle_voice(update Update, context CallbackContext)
    user = update.message.from_user
    print(fReceived voice message from {user.first_name} ({user.id}))

    # دانلود فایل صوتی
    file = context.bot.get_file(update.message.voice.file_id)
    input_path = fvoice_{user.id}.ogg
    output_path = fvoice_{user.id}.wav
    file.download(input_path)
    
    # تبدیل به WAV
    convert_audio_to_wav(input_path, output_path)

    # تبدیل صدا به متن
    update.message.reply_text(در حال پردازش فایل صوتی شما، لطفاً صبر کنید...)
    try
        text = transcribe_audio(output_path)
        update.message.reply_text(fمتن استخراج شدهn{text})
    except Exception as e
        update.message.reply_text(متأسفانه در پردازش فایل صوتی شما مشکلی پیش آمد.)
        print(fError {e})

    # حذف فایل‌های موقت
    os.remove(input_path)
    os.remove(output_path)

# راه‌اندازی ربات تلگرام
def main()
    TOKEN = YOUR_TELEGRAM_BOT_TOKEN  # توکن ربات تلگرام خود را اینجا وارد کن
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # تنظیم هندلرها
    dispatcher.add_handler(MessageHandler(Filters.voice, handle_voice))

    # شروع ربات
    print(Bot is running...)
    updater.start_polling()
    updater.idle()

if __name__ == __main__
    main()
