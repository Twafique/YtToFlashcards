from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

@app.route('/transcribe', methods=['POST'])
def transcribe():
    data = request.get_json()
    video_url = data.get('video_url')

    # Dummy response for testing
    return jsonify({
        "message": "Received URL",
        "video_url": video_url,
        "flashcards": [
            {"q": "Sample question?", "a": "Sample answer."}
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
