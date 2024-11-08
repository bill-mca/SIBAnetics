import time
import os
import subprocess
from picamera2 import Picamera2
import threading
import RPi.GPIO as GPIO
import socket

# GPIO setups
BUTTON_PIN = 2
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(BUTTON_PIN, GPIO.IN)
GPIO.setup(18, GPIO.OUT)  # Rec LED
GPIO.setup(23, GPIO.OUT)  # Active LED
GPIO.setup(22, GPIO.OUT)  # Process LED

# Global flag to indicate waiting for CMP
waiting_for_cmp = False

def rec_led_on():
    GPIO.output(18, GPIO.HIGH)

def rec_led_off():
    GPIO.output(18, GPIO.LOW)

def active_led_on():
    GPIO.output(23, GPIO.HIGH)

def active_led_off():
    GPIO.output(23, GPIO.LOW)

def process_led_on():
    GPIO.output(22, GPIO.HIGH)

def process_led_off():
    GPIO.output(22, GPIO.LOW)

# Parameters for recording
duration = 3
audio_filename = "audio.wav"
video_filename = "video.mp4"

def record_audio(filename, duration):
    time.sleep(2)
    print('Recording audio...')
    command = [
        "arecord",
        "-D", "hw:3,0",
        "-f", "S16_LE",
        "-c", "1",
        "-t", "wav",
        "-d", str(duration),
        "-r", "44100",
        filename
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error recording audio: {result.stderr}")
    else:
        print("Audio recorded successfully.")


def record_video(picam2, filename, duration):
    video_config = picam2.create_video_configuration(main={"size": (640, 480)})
    picam2.configure(video_config)
   
    time.sleep(2)
    print('Recording video...')
    picam2.start_and_record_video(filename, duration=duration)
    picam2.stop_recording()
    print('Video finished.')

def send_ack():
    server_ip = "10.28.67.68"
    server_port = 8080
   
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    client_socket.send("ACK".encode())
    client_socket.close()

def await_cmp():
    global waiting_for_cmp
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8080))
    server_socket.listen(1)
   
    while True:
        client_socket, addr = server_socket.accept()
        message = client_socket.recv(1024).decode()
        if message == "CMP":
            print("Process Complete")
            process_led_off()
            waiting_for_cmp = False  # Reset waiting flag
            client_socket.close()
            continue
        client_socket.close()

def run_tailscale():
    try:
        result = subprocess.run(
            ['sudo', 'tailscale', 'up'],
            check=True,
            text=True,
            capture_output=True
        )
        print(result.stdout, result.stderr)
    except subprocess.CalledProcessError as e:
        print(e.stderr, "There is an error")

if __name__ == '__main__':
    active_led_on()
    rec_led_on()
    process_led_on()
    run_tailscale()
    time.sleep(5)
    picam2 = Picamera2()  # Initialize Picamera2 once
   
    rec_led_off()
    process_led_off()

    try:
        # Start the CMP listener thread
        cmp_thread = threading.Thread(target=await_cmp)
        cmp_thread.daemon = True
        cmp_thread.start()

        while True:
            if GPIO.input(BUTTON_PIN) == GPIO.LOW and not waiting_for_cmp:  # Button pressed
               
               
                audio_thread = threading.Thread(target=record_audio, args=(audio_filename, duration))
                video_thread = threading.Thread(target=record_video, args=(picam2, video_filename, duration))
               
                rec_led_on()
                audio_thread.start()
                video_thread.start()
           
                audio_thread.join()
                video_thread.join()

                print('Recording completed.')
                rec_led_off()
               
                send_ack()  # Send ACK after recording
                process_led_on()  # Turn on process LED

                waiting_for_cmp = True  # Set flag to indicate waiting for CMP
                # Wait for CMP in the background thread

    finally:
        picam2.close()  # Clean up and release resources when done
        active_led_off()