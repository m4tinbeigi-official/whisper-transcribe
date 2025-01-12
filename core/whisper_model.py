# core/whisper_model.py

import whisper
from config.config import WHISPER_MODEL_PATH

class WhisperModel:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(WhisperModel, cls).__new__(cls)
            print("Loading Whisper model...")
            cls._instance.model = whisper.load_model(WHISPER_MODEL_PATH)
            print("Model loaded successfully.")
        return cls._instance

    def transcribe_audio(self, audio_path, language="fa"):
        result = self.model.transcribe(audio_path, language=language)
        return result["text"]