# mouth-open
Detecting when a human's mouth is open

Forked from MIT licesed [code by Mauck](https://github.com/mauckc/mouth-open/tree/master).

## Dependencies
Python modules for:
* scipy
* imutils
* numpy
* dlib
* cv2

## Usage
This sample version uses your webcam, so make sure that the device you are using has one.  Otherwise, you will need to change the code to take in a video file.

#### To run the code
```bash
python detect_open_mouth.py
```

[dlib shape predictor](https://github.com/AKSHAYUBHAT/TensorFace/blob/master/openface/models/dlib/shape_predictor_68_face_landmarks.dat)

![sample gif](https://github.com/mauckc/mouth-open/raw/master/video/mouth_open.gif)

![sample gif](https://github.com/mauckc/mouth-open/raw/master/video/facial_landmarks_68markup-768x619.jpg)


![trump-mouth](./video/out_trump.gif)
