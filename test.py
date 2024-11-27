from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Backend Server URL
BACKEND_SERVER_URL = "https://5a25-218-235-241-54.ngrok-free.app"  # 백엔드 서버 URL

song_id = 10

# Function to get song URL from backend server
def get_song_url(song_id):
    try:
        # Send GET request to backend server with song_id
        response = requests.get(f"{BACKEND_SERVER_URL}/10")
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json().get("song_url")  # Extract the song_url from response
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to fetch song URL from backend: {str(e)}")

# Function to simulate playing a song on the speaker
def play_song_on_speaker(song_url):
    try:
        # Simulate song playback (Here you can integrate with your speaker API or system call)
        print(f"Playing song on speaker: {song_url}")
        return True
    except Exception as e:
        raise Exception(f"Failed to play song on speaker: {str(e)}")

# Flask endpoint to handle song playback request
@app.route('/answer.music.play', methods=['POST'])
def play_song(song_id):
    try:
        # Get the song URL from backend server
        song_url = get_song_url(song_id)
        if not song_url:
            return jsonify({"error": "No song URL found"}), 404

        # Play the song on the speaker
        play_song_on_speaker(song_url)

        # Return success response
        return jsonify({"status": "success", "song_url": song_url}), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
