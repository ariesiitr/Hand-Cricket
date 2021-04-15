import cv2 
import numpy as np

capture = cv2.VideoCapture(0);
while capture.isOpened():
    ret,frame = capture.read()
    cv2.rectangle(frame, (100, 100), (300, 300), (0, 255, 0), 0)
    crop_image = frame[100:300, 100:300] 