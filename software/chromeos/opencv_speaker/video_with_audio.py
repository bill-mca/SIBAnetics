# Forked from MIT licensed code by otamajakusi
# https://github.com/otamajakusi/opencv_video_with_audio
# https://i7y.org/en/how-to-handle-video-and-audio-with-opencv/

import cv2
import time

# for WithPyAudio
import pyaudio
import wave

# for WithMediaPlayer
from ffpyplayer.player import MediaPlayer

class AudioDataMixin:
    def process_audio(self, data, width, channels, framerate):
        print(f"{width=},{channels=},{framerate=}")

class WithPyAudio(AudioDataMixin):
    # https://people.csail.mit.edu/hubert/pyaudio/docs/#example-callback-mode-audio-i-o

    def __init__(self, audio_file):
        super().__init__()
        wf = wave.open(audio_file, "rb")
        p = pyaudio.PyAudio()

        self.wf = wf
        self.p = p
        print(f"{wf.getsampwidth()=},{wf.getnchannels()=},{wf.getframerate()=}")

        self.stream = p.open(
            format=p.get_format_from_width(wf.getsampwidth()),
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            output=True,
            stream_callback=self._stream_cb,
        )

    def get_frame(self):
        if not self.stream.is_active():
            return False
        return True

    def close(self):
        self.stream.stop_stream()
        self.stream.close
        self.p.terminate()
        self.wf.close()

    def _stream_cb(self, in_data, frame_count, time_info, status):
        data = self.wf.readframes(frame_count)
        if self.process_audio:  # mixin
            wf = self.wf
            self.process_audio(
                data[:], wf.getsampwidth(), wf.getnchannels(), wf.getframerate()
            )
        return (data, pyaudio.paContinue)


class WithMediaPlayer:
    def __init__(self, audio_file):
        self.player = MediaPlayer(audio_file)

    def get_frame(self):
        _, val = self.player.get_frame(show=False)
        if val == "eof":
            return False
        return True

    def close(self):
        if self.player:
            self.player.close_player()
            self.player = None


def main(video_file, audio_file, use_pyaudio=True):
    print(f"{video_file=},{audio_file=},{use_pyaudio=}")
    cap = cv2.VideoCapture(video_file)

    if use_pyaudio:
        player = WithPyAudio(audio_file)
    else:
        player = WithMediaPlayer(audio_file)
    start_time = time.time()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if not player.get_frame():
            break

        cv2.imshow(video_file, frame)

        elapsed = (time.time() - start_time) * 1000  # msec
        play_time = int(cap.get(cv2.CAP_PROP_POS_MSEC))
        sleep = max(1, int(play_time - elapsed))
        if cv2.waitKey(sleep) & 0xFF == ord("q"):
            break

    player.close()
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    import argparse
    from distutils.util import strtobool

    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("--video", required=True)
    parser.add_argument(
        "--audio",
        help="`.wav` file.\n"
        "`.wav` file can be retrieved from video stream by:\n"
        "ffmpeg -i my_video.mp4 -vn -f wav my_audio.wav",
        required=True,
    )
    parser.add_argument(
        "--use-pyaudio",
        help="Use pyadio or ffpyplayer. default pyaudio.\n"
        "If this option is set as false, the same file can be specified for video and audio.",
        default="yes",
    )
    args = parser.parse_args()
    main(args.video, args.audio, strtobool(args.use_pyaudio))
