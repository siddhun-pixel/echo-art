import os
from flask import Blueprint, request, jsonify, current_app
from datetime import datetime

# Create the blueprint with name "api"
api_bp = Blueprint('api', __name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def process_echo_art(audio_file_path, abstract_text):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{current_time}] Processing Request ...")
    print(f"Abstract: '{abstract_text[:50]}...'")
    print(f"Audio Path: {audio_file_path}")

    if "blue light" in abstract_text.lower() or "cave" in abstract_text.lower():
        image_url = "https://example.com/generated/echo_deep_blue_resonance.png"
    else:
        image_url = "https://example.com/generated/default_rainbow_art.png"

    return {
        "status": "completed",
        "message": "Art generation simulated successfully. Check 'image_url' for the result.",
        "image_url": image_url,
        "input_abstract": abstract_text,
        "input_audio_filename": os.path.basename(audio_file_path) if audio_file_path != "No audio provided" else None
    }

@api_bp.route('/process', methods=['POST'])
def handle_process_request():
    abstract = request.form.get('abstract', "").strip()
    audio_file = request.files.get('audio')

    if not audio_file and not abstract:
        return jsonify({"error": "No input provided. Please provide an audio file or a text abstract."}), 400

    audio_path = "No audio provided"
    if audio_file:
        filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{audio_file.filename}"
        audio_path = os.path.join(UPLOAD_FOLDER, filename)
        try:
            audio_file.save(audio_path)
        except Exception as e:
            current_app.logger.error(f"Error saving file: {e}")
            return jsonify({"error": "Failed to save audio file on the server."}), 500

    try:
        result_data = process_echo_art(audio_path, abstract)
        return jsonify(result_data), 200
    except Exception as e:
        current_app.logger.error(f"Processing error: {e}")
        return jsonify({"error": "Internal server processing error occurred."}), 500
