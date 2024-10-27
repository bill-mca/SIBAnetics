#! /usr/bin/python

# Following a guide from a Medium article
# https://medium.com/@WebDevSid/audio-visual-active-speaker-detection-on-video-for-ai-tools-dc297443f0be

import cv2
import webrtcvad

# Load DNN model
net = cv2.dnn.readNetFromCaffe("deploy.prototxt", "res10_300x300_ssd_iter_140000_fp16.caffemodel")

# Load the face detector
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load the mouth detector
mouth_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')

video_path = 'test.mp4'  # Replace with your video file path

def measure_mouth_openness(detections):
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:  # Confidence threshold
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            # Get the region of interest for the detected face
            face_roi = frame[startY:endY, startX:endX]
            gray = cv2.cvtColor(face_roi, cv2.COLOR_BGR2GRAY)
            dlib_faces = detector(gray)

            for dlib_face in dlib_faces:
                landmarks = predictor(gray, dlib_face)

                # Get mouth landmarks (48 to 67)
                upper_lip = np.array([(landmarks.part(i).x, landmarks.part(i).y) for i in range(48, 54)])
                lower_lip = np.array([(landmarks.part(i).x, landmarks.part(i).y) for i in range(54, 68)])

                # Calculate mouth openness
                upper_center = np.mean(upper_lip, axis=0)
                lower_center = np.mean(lower_lip, axis=0)

                mouth_openness = np.linalg.norm(lower_center - upper_center)  # Euclidean distance
                return mouth_openness

# Initialize the video capture
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("End of video or error.")
        break

    # Use Haar Cascade for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # # Use DNN for face detection
    # h, w = frame.shape[:2]
    # blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
    # net.setInput(blob)
    # faces = net.forward()

    #print (detections)

    # Display the resulting frame
    cv2.imshow('Video Preview', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()


# # Initialize VAD
# vad = webrtcvad.Vad(2)  # Aggressiveness mode from 0 to 3
#
# def voice_activity_detection(audio_frame, sample_rate=16000):
#     return vad.is_speech(audio_frame, sample_rate)
#
#
# lip_distance = abs(top_lip_center - bottom_lip_center)
#
#     # Audio detection
#     is_speaking_audio = voice_activity_detection(audio_frame)
#
#     # Combine visual and audio cues
#     if lip_distance > 10 and is_speaking_audio:  # Adjust the threshold as needed
#         return True
#     return False