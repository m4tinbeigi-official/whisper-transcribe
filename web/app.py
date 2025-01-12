# web/app.py

import os
from flask import Flask, render_template, request, jsonify
from core.whisper_model import WhisperModel
from core.audio_utils import convert_audio_to_wav

app = Flask(__name__)
model = WhisperModel()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_audio():
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
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)