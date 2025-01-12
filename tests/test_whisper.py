# tests/test_whisper.py

import unittest
from core.whisper_model import WhisperModel

class TestWhisperModel(unittest.TestCase):
    def test_transcribe_audio(self):
        model = WhisperModel()
        text = model.transcribe_audio("test_audio.wav")
        self.assertIsInstance(text, str)

if __name__ == "__main__":
    unittest.main()