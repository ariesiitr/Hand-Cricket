import cv2
import time
import os
import HandTrackingModule as htm

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

    detector= htm.handDetector(detectionCon=0.75)
    tipIds=[4, 8, 12, 16, 20]

    while True:
        ret, img = cap.read()
        cv2.imshow('a', img)

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
                cv2.imshow('a', img)
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
                cv2.imshow("Image", img)
                cv2.waitKey(0)

                #Reset TIMER
                TIMER = 5
        elif k==27:
            break

    cap.release()
    cv2.destroyAllWindows()
    return number

hd()