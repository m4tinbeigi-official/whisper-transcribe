# bot/telegram_bot.py

import os
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
from core.whisper_model import WhisperModel
from core.audio_utils import convert_audio_to_wav
from config.config import TELEGRAM_BOT_TOKEN

class TelegramWhisperBot:
    def __init__(self):
        self.model = WhisperModel()

    def handle_voice(self, update: Update, context: CallbackContext):
        user = update.message.from_user
        print(f"Received voice message from {user.first_name} ({user.id})")

        # دانلود فایل صوتی
        file = context.bot.get_file(update.message.voice.file_id)
        input_path = f"voice_{user.id}.ogg"
        output_path = f"voice_{user.id}.wav"
        file.download(input_path)

        # تبدیل به WAV
        convert_audio_to_wav(input_path, output_path)

        # تبدیل صدا به متن
        update.message.reply_text("در حال پردازش فایل صوتی شما، لطفاً صبر کنید...")
        try:
            text = self.model.transcribe_audio(output_path)
            update.message.reply_text(f"متن استخراج شده:\n{text}")
        except Exception as e:
            update.message.reply_text("متأسفانه در پردازش فایل صوتی شما مشکلی پیش آمد.")
            print(f"Error: {e}")

        # حذف فایل‌های موقت
        os.remove(input_path)
        os.remove(output_path)

    def run(self):
        updater = Updater(TELEGRAM_BOT_TOKEN)
        dispatcher = updater.dispatcher

        # تنظیم هندلرها
        dispatcher.add_handler(MessageHandler(Filters.voice, self.handle_voice))

        # شروع ربات
        print("Bot is running...")
        updater.start_polling()
        updater.idle()

if __name__ == "__main__":
    bot = TelegramWhisperBot()
    bot.run()