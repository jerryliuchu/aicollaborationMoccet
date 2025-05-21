from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    review = data.get("review", "")

    # Simulated classification
    emotion_labels = ['Joy', 'Anger', 'Sadness', 'Fear']
    emotion_scores = [round(random.uniform(0, 1), 2) for _ in emotion_labels]

    intent_labels = ['Complaint', 'Praise', 'Request', 'Feedback']
    intent_scores = [round(random.uniform(0, 1), 2) for _ in intent_labels]

    return jsonify({
        "emotion_labels": emotion_labels,
        "emotion_scores": emotion_scores,
        "intent_labels": intent_labels,
        "intent_scores": intent_scores
    })

if __name__ == "__main__":
    app.run(debug=True)
