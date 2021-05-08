import cv2
import time
import os
import numpy as np
from player import hd
from game import printscore
from game import printresult

import random


def mains():
    flag=1
    score1=0
    score2=0
    while True:
        player_turn=hd()
        #print(player_turn)
        score1 = score1 + player_turn

        computer_turn = random.randint(1,6)
        img = np.zeros((512, 512, 3), np.uint8)
        cv2.rectangle(img, (181, 156), (331, 356), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "Computer", (150, 100), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        cv2.putText(img, str(computer_turn), (206, 306), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)
        cv2.imshow('Image', img)
        cv2.waitKey(0)

        #print(computer_turn)
        score2 = score2 + computer_turn

        printscore(player_turn,computer_turn)
        if player_turn == computer_turn :
            flag=0
            break
        else:
            continue

    if flag==0:
        printresult(score1, score2)

cv2.destroyAllWindows()

mains()
