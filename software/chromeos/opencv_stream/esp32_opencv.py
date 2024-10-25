#! /usr/bin/python

# code adapted from Projecto Official
# https://github.com/ProjectoOfficial/ESP32/blob/main/ESP32_CAM_PYTHON_STREAM_OPENCV/ESP32_CAM_PYTHON_STREAM_OPENCV.py

import cv2
import numpy as np

import requests

'''
INFO SECTION
- if you want to monitor raw parameters of ESP32CAM, open the browser and go to http://192.168.x.x/status
- command can be sent through an HTTP get composed in the following way http://192.168.x.x/control?var=VARIABLE_NAME&val=VALUE (check varname and value in status)
'''

# ESP32 URL
URL = "http://192.168.0.4"
AWB = True
processed_save_path = '../socket_test/image.jpg'

# Face recognition and opencv setup
cap = cv2.VideoCapture(URL + ":81/stream")

def count_yellow_objects_on_cam(img):
    objectCounter = 0

    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    fontThickness = 2
    color = (0, 255, 0)

    # Take a still that we will analyse
    #img = picam2.capture_array()
    #img_copy = img.copy()

    ## Analyse

    hsvFrame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    yellow_lower = np.array([15, 120, 120], np.uint8)
    yellow_upper = np.array([30, 255, 255], np.uint8)
    yellow_mask = cv2.inRange(hsvFrame, yellow_lower, yellow_upper)

    # DOWNSCALE
    # Taking a matrix of size 5 as the kernel
    kernel = np.ones((5, 5), np.uint8)
    eroded_mask = cv2.erode(yellow_mask, kernel, iterations=1)
    dilated_mask = cv2.dilate(yellow_mask, kernel, iterations=8)
    #cv2.imwrite("cv2-eroded-mask-test.png", eroded_mask)

    ## Count

    # from https://stackoverflow.com/questions/71491995/how-to-count-the-color-detected-objects-using-opencv/71492126#71492126

    # Find the contours on the binary image:
    contours, hierarchy = cv2.findContours(dilated_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Store bounding rectangles and object id here:
    objectData = []

    # Look for the outer bounding boxes (no children):
    for _, c in enumerate(contours):
        # Get the contour's bounding rectangle:
        boundRect = cv2.boundingRect(c)

        # Store in list:
        objectData.append((objectCounter, boundRect))

        # Get the dimensions of the bounding rect:
        rectX = boundRect[0]
        rectY = boundRect[1]
        rectWidth = boundRect[2]
        rectHeight = boundRect[3]

        # Draw bounding rect:
        color = (0, 0, 255)
        cv2.rectangle(img, (int(rectX), int(rectY)),
                    (int(rectX + rectWidth), int(rectY + rectHeight)), color, 2)

        # Draw object counter:
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        fontThickness = 2
        color = (0, 255, 255)
        cv2.putText(img, str(objectCounter), (int(rectX), int(rectY)),
                    font, fontScale, color, fontThickness)

        #cv2.imwrite("cv2-object-{}.png".format(objectCounter), img_copy)

        # Increment object counter
        objectCounter += 1
        
    #print(objectCounter)
    cv2.putText(img, str(objectCounter), (100, 100),
                    font, fontScale, color, fontThickness)
    return(objectCounter, img)

def set_resolution(url: str, index: int=1, verbose: bool=False):
    try:
        if verbose:
            resolutions = "10: UXGA(1600x1200)\n9: SXGA(1280x1024)\n8: XGA(1024x768)\n7: SVGA(800x600)\n6: VGA(640x480)\n5: CIF(400x296)\n4: QVGA(320x240)\n3: HQVGA(240x176)\n0: QQVGA(160x120)"
            print("available resolutions\n{}".format(resolutions))

        if index in [10, 9, 8, 7, 6, 5, 4, 3, 0]:
            requests.get(url + "/control?var=framesize&val={}".format(index))
        else:
            print("Wrong index")
    except:
        print("SET_RESOLUTION: something went wrong")

def set_quality(url: str, value: int=1, verbose: bool=False):
    try:
        if value >= 10 and value <=63:
            requests.get(url + "/control?var=quality&val={}".format(value))
    except:
        print("SET_QUALITY: something went wrong")

def set_awb(url: str, awb: int=1):
    try:
        awb = not awb
        requests.get(url + "/control?var=awb&val={}".format(1 if awb else 0))
    except:
        print("SET_QUALITY: something went wrong")
    return awb

if __name__ == '__main__':
    set_resolution(URL, index=8)

    while True:
        if cap.isOpened():
            ret, frame = cap.read()

            objectCounter, yellow_bounded = count_yellow_objects_on_cam(frame)

            cv2.imshow("Yellow stuff!", frame)            
            #cv2.imwrite("cv2-object-{}.jpg".format(objectCounter), 
            #            yellow_bounded)
            #bgr_bounded = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)
            cv2.imwrite(processed_save_path, frame)
            
            key = cv2.waitKey(1)

            if key == ord('r'):
                idx = int(input("Select resolution index: "))
                set_resolution(URL, index=idx, verbose=True)

            elif key == ord('q'):
                val = int(input("Set quality (10 - 63): "))
                set_quality(URL, value=val)

            elif key == ord('a'):
                AWB = set_awb(URL, AWB)

            elif key == 27:
                break

    cv2.destroyAllWindows()
    cap.release()
