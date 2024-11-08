import threading
import os
import subprocess
import wav
import align
from flask import Flask, render_template_string, url_for
import socket
from PIL import Image

app = Flask(__name__)
web_output = {'audio': "I was so young when I was born", 'lip': "", 'align': "", 'confidence': "0%"}
lock = threading.Lock()

def run_inference(video_file):
    """Run inference on the recorded video."""
    inference_script = 'inference.py'
    
    #make sure in right place
    if not os.path.exists(inference_script):
        print(f"Error: {inference_script} not found.")
        return None  

    # Run the inference script using subprocess
    command = ['python', inference_script, '--input_video', video_file]
    
    try:
        #capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        
        if result.returncode == 0:
            return result.stdout  
        else:
            print(f"Inference failed: {result.stderr}")
            return None
    except Exception as e:
        print(f"Error during inference: {e}")
        return None

def create_gif(image_folder, gif_path, duration=71):
    """Create a GIF from JPG images in a specified folder."""
    images = sorted([img for img in os.listdir(image_folder) if img.endswith(".jpg")])
    frames = [Image.open(os.path.join(image_folder, img)) for img in images]
    
    #gif
    frames[0].save(gif_path, format="GIF", append_images=frames[1:], save_all=True, duration=duration, loop=0)
    print(f"GIF saved at {gif_path}")

####### Flask Routes ########

@app.route('/')
def display_text():
    with lock:
        text = web_output
    gif_url = url_for("static", filename="output.gif")
    
    html = """
    <html>
    <head>
        <meta http-equiv="refresh" content="5">
        <style>
            .audio { background-color: #ffdddd; padding: 10px; }
            .lip { background-color: #ddddff; padding: 10px; }
            .align { background-color: #ddffdd; padding: 10px; }
            .confidence { background-color: #fdfd96; padding: 10px; }
        </style>
    </head>
    <body>
        <h1>Transcription Output</h1>
        <div class="audio"><strong>Audio Transcription:</strong> {{ audio }}</div>
        <div class="lip"><strong>Lip Reading Transcription:</strong> {{ lip }}</div>
        <div class="align"><strong>Aligned Transcription:</strong> {{ align }}</div>
        <div class="confidence"><strong>Confidence:</strong> {{ confidence }}</div>
        
        <!-- Display the GIF below the transcriptions -->
        <img src="{{ gif_url }}" alt="Generated GIF">
    </body>
    </html>
    """
    return render_template_string(html, audio=text.get('audio', ''), lip=text.get('lip', ''), align=text.get('align', ''), confidence=text.get('confidence', '0%'),  gif_url=gif_url)

#############################
# Parameters for outputs
#############################
threshold = 0.5
samples_folder = "samples"  #folder of images
gif_path = "static/output.gif"  #gif save location

def send_cmp():
    server_ip = "100.99.216.109"
    server_port = 8080
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket. connect((server_ip, server_port))
    
    print("Sending Completion notice")
    client_socket.send("CMP".encode())
    client_socket.close()


def process_acknowledgment():
    global web_output
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8080))
    server_socket.listen(1)
    print("Server listening for acknowledgment on port 8080...")

    try:
        while True:
            client_socket, addr = server_socket.accept()
            print(f"Connection from {addr}")

            message = client_socket.recv(1024).decode()
            if message == "ACK":
                print("Acknowledgment received! Running inference...")
                l_output_file = r"Z:\home\p7127929\video.mp4"
                a_output_file = r"Z:\home\p7127929\audio.wav"

                try:
                    #inference
                    lip_transcription = run_inference(l_output_file)
                    audio_transcription = wav.main(a_output_file).upper()
                    score = 0
                    
                    aligned_transcription = None
                    if lip_transcription and audio_transcription:
                        alignment_result = align.nw(audio_transcription, lip_transcription)
                        aligned_transcription = align.align(alignment_result[0], alignment_result[1])
                        score = align.match_per(aligned_transcription)

                    

                    #update web param
                    with lock:
                        web_output = {
                            'audio': audio_transcription or "No audio transcription available",
                            'lip': lip_transcription or "No lip reading transcription available",
                            'align': aligned_transcription or "No aligned transcription available",
                            'confidence': f"{score*100}" + "%" or "0%"
                        }

                    #create the gif
                    create_gif(samples_folder, gif_path)
                    
                    send_cmp()
                    
                except Exception as e:
                    with lock:
                        web_output = {
                            'audio': "Error during processing",
                            'lip': "Error during processing",
                            'align': f"Error details: {e}"
                        }
                    print(f"Error during processing: {e}")

            client_socket.close()
    except KeyboardInterrupt:
        print("Server shutting down.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    #start main loop
    ack_thread = threading.Thread(target=process_acknowledgment)
    ack_thread.daemon = True
    ack_thread.start()

    #activate website
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)