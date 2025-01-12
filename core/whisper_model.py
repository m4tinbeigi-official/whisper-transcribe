# core/whisper_model.py

import whisper
from config.config import WHISPER_MODEL_PATH

class WhisperModel:
    def __init__(self):
        print("Loading Whisper model...")
        self.model = whisper.load_model(WHISPER_MODEL_PATH)
        print("Model loaded successfully.")

    def transcribe_audio(self, audio_path, language="fa"):
        result = self.model.transcribe(audio_path, language=language)
        return result["text"]