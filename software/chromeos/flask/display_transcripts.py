from flask import Flask
from flask import render_template
from flask import render_template_string

import asyncio
#import websockets
import binascii
from io import BytesIO
from PIL import Image
from flask import Flask, Response
from base64 import b64encode


app = Flask(__name__)

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
