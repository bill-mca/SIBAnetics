from flask import Flask, Response, render_template
import time
import os

app = Flask(__name__)

# Path to your text file
TEXT_FILE = 'audio_transcript.txt'
last_modified_time = 0

def read_file():
    with open(TEXT_FILE, 'r') as file:
        return file.read()

@app.route('/')
def index():
    return render_template('text_feed.html')

def generate():
    global last_modified_time
    while True:
        current_modified_time = os.path.getmtime(TEXT_FILE)
        if current_modified_time != last_modified_time:
            last_modified_time = current_modified_time
            yield f"data: {read_file()}\n\n"
        time.sleep(1)  # Check every second

@app.route('/stream')
def stream():
    return Response(generate(), content_type='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)
