#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pyaudio
import numpy
import wave


# In[4]:


# Define parameters
FORMAT = pyaudio.paInt16  # Audio format
CHANNELS = 1               # Mono audio
RATE = 44100               # Sample rate
CHUNK = 1024               # Buffer size
RECORD_SECONDS = 5         # Duration of recording
WAVE_OUTPUT_FILENAME = "output.wav"  # Output file name


# In[5]:


p = pyaudio.PyAudio()


# In[6]:


# Start recording
stream = p.open(format=FORMAT, channels=CHANNELS,
                 rate=RATE, input=True,
                 frames_per_buffer=CHUNK)

print("Recording...")

frames = []

for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

stream.stop_stream()
stream.close()
p.terminate()

print("Recording finished.")


# In[11]:


# Save the recorded data as a WAV file
with wave.open(WAVE_OUTPUT_FILENAME, 'wb') as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))

print(f"Recorded audio saved to {WAVE_OUTPUT_FILENAME}.")


# In[12]:


# Play back the recorded audio
def play_audio(filename):
    wf = wave.open(filename, 'rb')
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                     channels=wf.getnchannels(),
                     rate=wf.getframerate(),
                     output=True)

    data = wf.readframes(CHUNK)
    while data:
        stream.write(data)
        data = wf.readframes(CHUNK)

    stream.stop_stream()
    stream.close()

play_audio(WAVE_OUTPUT_FILENAME)


# In[ ]:




