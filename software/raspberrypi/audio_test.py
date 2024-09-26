## from https://makersportal.com/blog/2018/8/23/recording-audio-on-the-raspberry-pi-with-python-and-a-usb-microphone
# ### download packages
pi@raspberrypi:~ $ sudo apt-get install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev
#install pyaudio
sudo pip3 install pyaudio
#testing py audio and mic
#Open Python 3.x and type the following (I use IDLE):
import pyaudio
p = pyaudio.PyAudio()
for ii in range(p.get_device_count()):
     print(p.get_device_info_by_index(ii).get('name'))

## NOTE USB INDEX:
##Take note of the index of the USB device, because we will need to adjust the pyaudio device index in reference to the sequence above. For example, my USB device is located at index 2 (index 0 is ALSA main, index 1 is IEC958/HDMI, etc…).

import pyaudio
import wave

form_1 = pyaudio.paInt16 # 16-bit resolution
chans = 1 # 1 channel
samp_rate = 44100 # 44.1kHz sampling rate
chunk = 4096 # 2^12 samples for buffer
record_secs = 3 # seconds to record
dev_index = 2 # device index found by p.get_device_info_by_index(ii)
wav_output_filename = 'test1.wav' # name of .wav file

audio = pyaudio.PyAudio() # create pyaudio instantiation

# create pyaudio stream
stream = audio.open(format = form_1,rate = samp_rate,channels = chans, \
                    input_device_index = dev_index,input = True, \
                    frames_per_buffer=chunk)
print("recording")
frames = []

# loop through stream and append audio chunks to frame array
for ii in range(0,int((samp_rate/chunk)*record_secs)):
    data = stream.read(chunk)
    frames.append(data)

print("finished recording")

# stop the stream, close it, and terminate the pyaudio instantiation
stream.stop_stream()
stream.close()
audio.terminate()

# save the audio frames as .wav file
wavefile = wave.open(wav_output_filename,'wb')
wavefile.setnchannels(chans)
wavefile.setsampwidth(audio.get_sample_size(form_1))
wavefile.setframerate(samp_rate)
wavefile.writeframes(b''.join(frames))
wavefile.close()

##The output .wav file should be 3 seconds long (assuming the code above is unchanged) and is sampled at 44.1kHz with a maximum resolution of 16-bits. Depending on the microphone used, the sample rate can be increased to 48kHz. The bit-depth can be changed as well, though I’m not entirely sure of the limitations on the Pi’s capabilities there. 
