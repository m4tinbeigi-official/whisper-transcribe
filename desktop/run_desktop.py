# desktop/run_desktop.py

import os
from core.whisper_model import WhisperModel
from core.audio_utils import convert_audio_to_wav

def main():
    model = WhisperModel()

    audio_file = input("Enter the path to your audio file (e.g., input_audio.mp3): ")

    if not os.path.exists(audio_file):
        print("The audio file does not exist. Please check the path.")
        return

    output_path = "converted_audio.wav"
    convert_audio_to_wav(audio_file, output_path)

    print("Transcribing audio file...")
    try:
        text = model.transcribe_audio(output_path)
        print(f"Transcribed Text:\n{text}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        os.remove(output_path)

if __name__ == "__main__":
    main()