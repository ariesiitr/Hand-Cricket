import cv2
import time
import os
import numpy as np



def printscore(s1,s2):
    img = np.zeros((512, 512, 3), np.uint8)
    cv2.putText(img, "TOTAL", (175, 100), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.rectangle(img, (53, 256), (203, 456), (0, 255, 0), cv2.FILLED)
    cv2.putText(img, "Computer", (5, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.putText(img, str(s2), (78, 406), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 8)

    cv2.rectangle(img, (309, 256), (459, 456), (0, 255, 0), cv2.FILLED)
    cv2.putText(img, "Player", (299, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.putText(img, str(s1), (334, 406), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 8)

    cv2.imshow('Image', img)
    cv2.waitKey(0)

def printresult(s1, s2):
    if s1>s2:
        img = np.zeros((256, 256, 3), np.uint8)
        cv2.putText(img, "PLAYER", (45, 100), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        cv2.putText(img, "WIN", (75, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        cv2.imshow('Image', img)
        cv2.waitKey(0)

    elif s1<s2:
        img = np.zeros((256, 256, 3), np.uint8)
        cv2.putText(img, "COMPUTER", (5, 100), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        cv2.putText(img, "WIN", (75, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        cv2.imshow('Image', img)
        cv2.waitKey(0)

    else:
        img = np.zeros((256, 256, 3), np.uint8)
        cv2.putText(img, "TIE", (55, 150), cv2.FONT_HERSHEY_PLAIN, 7, (255, 0, 0), 5)
        cv2.imshow('Image', img)
        cv2.waitKey(0)


