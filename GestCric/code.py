import cv2
import time
import os
import numpy as np
import mediapipe as mp
import random
import streamlit as st 

class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode=mode
        self.maxHands=maxHands
        self.detectionCon=detectionCon
        self.trackCon=trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils


    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img


    def findPosition(self, img, handNo =0, draw=True):

        lmList=[]
        if self.results.multi_hand_landmarks:
            myHand=self.results.multi_hand_landmarks[handNo]


            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                #print(id, cx, cy)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        return lmList

def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector=handDetector()
    while True:
        success, img = cap.read()
        img=detector.findHands(img)
        lmList=detector.findPosition(img)
        if len(lmList)!=0:
            print(lmList[4])

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 3)
        #cv2.imshow("Image", img)
        cv2.waitKey(1)





def hd():
    number=int(0)
    TIMER = int(2)
    cap = cv2.VideoCapture(0)
    folderPath="fingerimage"
    myList=os.listdir(folderPath)
    #print(myList)
    overlayList = []

    for imPath in myList:
        image=cv2.imread(f'{folderPath}/{imPath}')
        #print(f'{folderPath}/{imPath}')
        overlayList.append(image)

    #print(len(overlayList))
    pTime=0

    detector= handDetector(detectionCon=0.75)
    tipIds=[4, 8, 12, 16, 20]

    while True:
        ret, img = cap.read()
        #cv2.imshow('a', img)

        # check for the key pressed
        k = cv2.waitKey(125)
        if k == ord('q'):
            prev = time.time()

            while TIMER >= 0:
                ret, img = cap.read()
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(img, str(TIMER),
                            (200, 250), font,
                            7, (0, 255, 255),
                            4, cv2.LINE_AA)
                #cv2.imshow('a', img)
                cv2.waitKey(125)
                cur = time.time()

                # Update timer
                if cur-prev >= 1:
                    prev = cur
                    TIMER = TIMER-1

            else:
                ret, img = cap.read()
                img = detector.findHands(img)
                lmList = detector.findPosition(img, draw=False)
                # print(lmList)

                if len(lmList) != 0:
                    fingers = []

                    # 5
                    if lmList[tipIds[0]][1] > lmList[tipIds[0] - 2][1] and lmList[tipIds[1]][2] < lmList[tipIds[1] - 2][
                        2] and lmList[tipIds[2]][2] < lmList[tipIds[2] - 2][2] and lmList[tipIds[3]][2] < \
                            lmList[tipIds[3] - 2][2] and lmList[tipIds[4]][2] < lmList[tipIds[4] - 2][2]:
                        img[0:200, 0:200] = overlayList[4]
                        cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
                        cv2.putText(img, str('5'), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)
                        number=5

                    # 4
                    if lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1] and lmList[tipIds[1]][2] < lmList[tipIds[1] - 2][
                        2] and lmList[tipIds[2]][2] < lmList[tipIds[2] - 2][2] and lmList[tipIds[3]][2] < \
                            lmList[tipIds[3] - 2][2] and lmList[tipIds[4]][2] < lmList[tipIds[4] - 2][2]:
                        img[0:200, 0:200] = overlayList[3]
                        cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
                        cv2.putText(img, str('4'), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)
                        number=4

                    # 3
                    if lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1] and lmList[tipIds[1]][2] < lmList[tipIds[1] - 2][
                        2] and lmList[tipIds[2]][2] < lmList[tipIds[2] - 2][2] and lmList[tipIds[3]][2] < \
                            lmList[tipIds[3] - 2][2] and lmList[tipIds[4]][2] > lmList[tipIds[4] - 2][2]:
                        img[0:200, 0:200] = overlayList[2]
                        cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
                        cv2.putText(img, str('3'), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)
                        number=3

                    # 2
                    if lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1] and lmList[tipIds[1]][2] < lmList[tipIds[1] - 2][
                        2] and lmList[tipIds[2]][2] < lmList[tipIds[2] - 2][2] and lmList[tipIds[3]][2] > \
                            lmList[tipIds[3] - 2][2] and lmList[tipIds[4]][2] > lmList[tipIds[4] - 2][2]:
                        img[0:200, 0:200] = overlayList[1]
                        cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
                        cv2.putText(img, str('2'), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)
                        number=2

                    # 1
                    if lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1] and lmList[tipIds[1]][2] < lmList[tipIds[1] - 2][
                        2] and lmList[tipIds[2]][2] > lmList[tipIds[2] - 2][2] and lmList[tipIds[3]][2] > \
                            lmList[tipIds[3] - 2][2] and lmList[tipIds[4]][2] > lmList[tipIds[4] - 2][2]:
                        img[0:200, 0:200] = overlayList[0]
                        cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
                        cv2.putText(img, str('1'), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)
                        number=1

                    # 6
                    if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1] and lmList[tipIds[1]][2] > lmList[tipIds[1] - 2][
                        2] and lmList[tipIds[2]][2] > lmList[tipIds[2] - 2][2] and lmList[tipIds[3]][2] > \
                            lmList[tipIds[3] - 2][2] and lmList[tipIds[4]][2] > lmList[tipIds[4] - 2][2]:
                        img[0:200, 0:200] = overlayList[5]
                        cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
                        cv2.putText(img, str('6'), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)
                        number=6

                cTime = time.time()
                fps = 1 / (cTime - pTime)
                pTime = cTime

                cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN,
                            3, (255, 0, 0), 3)
                #cv2.imshow("Image", img)
                #cv2.waitKey(0)

                #Reset TIMER
                TIMER = 5
        elif k==27:
            break

    cap.release()
    cv2.destroyAllWindows()
    return number



def printscore(s1,s2):
    img = np.zeros((512, 512, 3), np.uint8)
    cv2.putText(img, "INSTANT SCORE", (75, 100), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)

    cv2.rectangle(img, (53, 256), (203, 456), (0, 255, 0), cv2.FILLED)
    cv2.putText(img, "Computer", (5, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.putText(img, str(s2), (78, 406), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)

    cv2.rectangle(img, (309, 256), (459, 456), (0, 255, 0), cv2.FILLED)
    cv2.putText(img, "Player", (299, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.putText(img, str(s1), (334, 406), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)

    #cv2.imshow('Image', img)
    cv2.waitKey(0)

def printresult(s1, s2):
    img = np.zeros((512, 512, 3), np.uint8)
    cv2.rectangle(img, (150, 156), (362, 356), (0, 255, 0), cv2.FILLED)
    cv2.putText(img, "Player Score", (110, 100), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.putText(img, str(s1), (156, 306), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 8)

    if s1>s2:

        cv2.putText(img, "PLAYER WIN", (125, 450), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
        #cv2.putText(img, "WIN", (75, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        #cv2.imshow('Image', img)
        cv2.waitKey(0)

    elif s1<s2:

        cv2.putText(img, "COMPUTER WIN", (85, 450), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
        #cv2.putText(img, "WIN", (75, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        #cv2.imshow('Image', img)
        cv2.waitKey(0)

    else:

        cv2.putText(img, "TIE", (165, 470), cv2.FONT_HERSHEY_PLAIN, 7, (0, 0, 255), 5)
        #cv2.imshow('Image', img)
        cv2.waitKey(0)




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
        #cv2.imshow('Image', img)
        cv2.waitKey(0)

        #print(computer_turn)
        score2 = score2 + computer_turn

        #printscore(player_turn,computer_turn)
        st.text(player_turn)
        st.text(computer_turn)
        if player_turn == computer_turn :
            flag=0
            break
        else:
            continue

    if flag==0:
        st.text(score1)
        st.text(score2)
        #printresult(score1, score2)

#cv2.destroyAllWindows()

mains()