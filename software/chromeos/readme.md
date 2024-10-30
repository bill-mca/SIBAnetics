# Software testing
There are several programs here that I am testing to try to identify who is speaking in a video.

## mouth open
Python, opencv and dlib to track the coordinates of someones mouth and (based on the aspect ratio, decide if it is open or closed.
This needs to be set to capture a stream and log through time if we want to use it for FH.

## opencv stream
This code is python opencv and it can read a stream of images from the ESP32S3 and identify yellow objects in them.
The next step is to merge this code with one of the scripts that identifys speakers.

## opencv speaker
This is based on some fragments of example code that I found. It is more deliberately trying to identify who is talking rather than if there is an open mouth on camera.

## Flask
A webserver that actively updates as information streams in from the ML models.