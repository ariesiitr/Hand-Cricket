import cv2
import time
import os
import numpy as np


import random

def mains():
    computer_turn = random.randint(1, 6)

    img = np.zeros((512, 512, 3), np.uint8)
    cv2.rectangle(img, (181, 156), (331, 356), (0, 255, 0), cv2.FILLED)
    cv2.putText(img, "Computer", (150, 100), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.putText(img, str(computer_turn), (206, 306), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)

    cv2.imshow("Image", img)
    cv2.waitKey(0)

    return computer_turn

mains()