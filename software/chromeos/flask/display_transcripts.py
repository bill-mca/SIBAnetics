from flask import Flask, render_template, render_template_string, Response
import os
import time
from io import BytesIO
from PIL import Image

TEXT_FILE = 'audio_transcript.txt'
last_modified_time = 0

app = Flask(__name__)

def read_audio_transcript():
    with open('audio_transcript.txt', 'r') as file:
        return file.read()

def read_lip_reading_transcript():
    with open('lip_reading_transcript.txt', 'r') as file:
        return file.read()

def generate_lip_reading_stream():
    global last_modified_time
    while True:
        current_modified_time = os.path.getmtime(TEXT_FILE)
        if current_modified_time != last_modified_time:
            last_modified_time = current_modified_time
            yield f"data: {read_lip_reading_transcript()}\n\n"
        time.sleep(1.1)  # Check every second

@app.route('/lip_reading_stream')
def lip_reading_stream():
    return Response(generate_lip_reading_stream(), content_type='text/event-stream')

@app.route('/audio_stream')
def audio_stream():
    return Response(generate_audio_stream(), content_type='text/event-stream')

def generate_audio_stream():
    global last_modified_time
    while True:
        current_modified_time = os.path.getmtime(TEXT_FILE)
        if current_modified_time != last_modified_time:
            last_modified_time = current_modified_time
            yield f"data: {read_audio_transcript()}\n\n"
        time.sleep(1.2)  # Check every second

def get_image():
    while True:
        try:
            with open("src/image.jpg", "rb") as f:
                image_bytes = f.read()
            image = Image.open(BytesIO(image_bytes))
            img_io = BytesIO()
            image.save(img_io, 'JPEG')
            img_io.seek(0)
            img_bytes = img_io.read()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + img_bytes + b'\r\n')

        except Exception as e:
            print("encountered an exception: ")
            print(e)

            with open("image.jpg", "rb") as f:
                image_bytes = f.read()
            image = Image.open(BytesIO(image_bytes))
            img_io = BytesIO()
            image.save(img_io, 'JPEG')
            img_io.seek(0)
            img_bytes = img_io.read()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + img_bytes + b'\r\n')
            continue


@app.route('/image')
def image():
    return Response(get_image(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def display_transcripts():
    # Read the content of the file
    with open('audio_transcript.txt', 'r') as file:
        audio_transcript = file.read()
    with open('lip_reading_transcript.txt', 'r') as file:
        lip_reading_transcript = file.read()
    return render_template('display_transcripts.html',
                            audio_transcript=audio_transcript,
                            lip_reading_transcript=lip_reading_transcript)
