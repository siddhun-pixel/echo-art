from flask import Blueprint, request, jsonify
from models import db, Submission

api = Blueprint('api', __name__)

@api.route('/process', methods=['POST'])
def process_audio():
    data = request.get_json()
    audio = data.get('audio')
    abstract = data.get('abstract')

    if not audio or not abstract:
        return jsonify({'error': 'Missing audio or abstract'}), 400

    submission = Submission(audio=audio, abstract=abstract)
    db.session.add(submission)
    db.session.commit()

    return jsonify({
        'message': 'Submission saved successfully',
        'id': submission.id
    })
