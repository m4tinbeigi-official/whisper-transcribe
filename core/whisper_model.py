# web/app.py

import os
import logging
from flask import Flask, render_template, request, jsonify
from core.whisper_model import WhisperModel
from core.audio_utils import convert_audio_to_wav

app = Flask(__name__)
model = WhisperModel()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_audio():
    logging.info("Received a file upload request.")
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    # اعتبارسنجی فرمت فایل
    allowed_extensions = {"ogg", "wav", "mp3"}
    if not file.filename.lower().endswith(tuple(allowed_extensions)):
        return jsonify({"error": "Invalid file format"}), 400

    input_path = "uploaded_audio.ogg"
    output_path = "uploaded_audio.wav"
    file.save(input_path)

    # تبدیل به WAV
    convert_audio_to_wav(input_path, output_path)

    # تبدیل صدا به متن
    try:
        text = model.transcribe_audio(output_path)
        os.remove(input_path)
        os.remove(output_path)
        return jsonify({"text": text})
    except Exception as e:
        logging.error(f"Error processing file: {e}")
        return jsonify({"error": "An error occurred while processing your request. Please try again later."}), 500

if __name__ == "__main__":
    app.run(debug=True)