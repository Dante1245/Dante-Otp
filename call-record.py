from twilio.rest import Client
from twilio.request_validator import RequestValidator
from flask import Flask, request, Response
import os

# Twilio credentials
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
twilio_phone_number = 'your_twilio_phone_number'

app = Flask(__name__)

@app.route('/record', methods=['POST'])
def record_call():
    validator = RequestValidator(auth_token)

    # Validate incoming request from Twilio
    if not validator.validate(request.url, request.form, request.headers):
        return Response(status=403)

    # Check if the call is in progress and recording
    if 'CallSid' in request.form and 'RecordingUrl' in request.form:
        call_sid = request.form['CallSid']
        recording_url = request.form['RecordingUrl']
        download_recording(call_sid, recording_url)

    return Response(status=200)

def download_recording(call_sid, recording_url):
    client = Client(account_sid, auth_token)

    try:
        recording = client.recordings(recording_url).fetch()
        file_name = f"{call_sid}.mp3"
        with open(file_name, 'wb') as f:
            f.write(recording.audio_content)
        print(f"Recording downloaded: {file_name}")
    except Exception as e:
        print(f"Error downloading recording: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
