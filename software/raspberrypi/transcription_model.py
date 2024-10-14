import os
import speech_recognition as sr
from pydub import AudioSegment

def extract_audio(input_wav_file):
    """Extract audio from a WAV file and return it."""
    try:
        audio = AudioSegment.from_wav(input_wav_file)
        return audio
    except Exception as e:
        print(f"Error loading audio: {e}")
        return None

def audio_to_text(audio_segment):
    """Convert audio segment to text using speech recognition."""
    recognizer = sr.Recognizer()
    
    # Export audio segment to a temporary WAV file for recognition
    temp_audio_file = "temp_audio.wav"
    audio_segment.export(temp_audio_file, format='wav')

    with sr.AudioFile(temp_audio_file) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return "Could not understand audio"
        except sr.RequestError as e:
            return f"Could not request results; {e}"
        finally:
            # Clean up temporary audio file
            try:
                if os.path.exists(temp_audio_file):
                    os.remove(temp_audio_file)
            except PermissionError as e:
                print(f"Error deleting temporary audio file: {e}")

def main(input_wav_file):
    """Main function to extract audio and convert to text."""
    audio_segment = extract_audio(input_wav_file)
    if audio_segment:
        print("Audio loaded successfully.")
        transcription = audio_to_text(audio_segment)
       # print("Transcription:")
        #print(transcription)
        return(transcription)
    else:
        print("Failed to load audio.")

if __name__ == "__main__":
    input_wav_file = r"C:\Users\izaka\LipCoordNet\testing\j.wav"  # Specify the input WAV file path
    if not os.path.exists(input_wav_file):
        print(f"Input file '{input_wav_file}' does not exist.")
    else:
        x=main(input_wav_file)
        print(f'\033[44m{x}\033[0m')
        
