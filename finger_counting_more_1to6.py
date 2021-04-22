import cv2
import time
import os
import HandTrackingModule as htm

wCam, hCam=640, 480
cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4, hCam)

folderPath="fingerimage"
myList=os.listdir(folderPath)
print(myList)
overlayList = []

for imPath in myList:
  image=cv2.imread(f'{folderPath}/{imPath}')
  #print(f'{folderPath}/{imPath}')
  overlayList.append(image)

print(len(overlayList))
pTime=0

detector= htm.handDetector(detectionCon=0.75)
tipIds=[4, 8, 12, 16, 20]
while True:
  success, img=cap.read()
  img=detector.findHands(img)
  lmList=detector.findPosition(img, draw=False)
  #print(lmList)

  if len(lmList)!=0:
    fingers=[]

    # 5
    if lmList[tipIds[0]][1]>lmList[tipIds[0]-2][1] and lmList[tipIds[1]][2]<lmList[tipIds[1]-2][2] and lmList[tipIds[2]][2]<lmList[tipIds[2]-2][2] and lmList[tipIds[3]][2]<lmList[tipIds[3]-2][2] and lmList[tipIds[4]][2]<lmList[tipIds[4]-2][2]:
      img[0:200, 0:200] = overlayList[4]
      cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
      cv2.putText(img, str('5'), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)

    # 4
    if lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1] and lmList[tipIds[1]][2]<lmList[tipIds[1]-2][2] and lmList[tipIds[2]][2]<lmList[tipIds[2]-2][2] and lmList[tipIds[3]][2]<lmList[tipIds[3]-2][2] and lmList[tipIds[4]][2]<lmList[tipIds[4]-2][2]:
      img[0:200, 0:200] = overlayList[3]
      cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
      cv2.putText(img, str('4'), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)

    # 3
    if lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1] and lmList[tipIds[1]][2]<lmList[tipIds[1]-2][2] and lmList[tipIds[2]][2]<lmList[tipIds[2]-2][2] and lmList[tipIds[3]][2]<lmList[tipIds[3]-2][2] and lmList[tipIds[4]][2]>lmList[tipIds[4]-2][2]:
      img[0:200, 0:200] = overlayList[2]
      cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
      cv2.putText(img, str('3'), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)

    # 2
    if lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1] and lmList[tipIds[1]][2]<lmList[tipIds[1]-2][2] and lmList[tipIds[2]][2]<lmList[tipIds[2]-2][2] and lmList[tipIds[3]][2]>lmList[tipIds[3]-2][2] and lmList[tipIds[4]][2]>lmList[tipIds[4]-2][2]:
      img[0:200, 0:200] = overlayList[1]
      cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
      cv2.putText(img, str('2'), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)

    # 1
    if lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1] and lmList[tipIds[1]][2]<lmList[tipIds[1]-2][2] and lmList[tipIds[2]][2]>lmList[tipIds[2]-2][2] and lmList[tipIds[3]][2]>lmList[tipIds[3]-2][2] and lmList[tipIds[4]][2]>lmList[tipIds[4]-2][2]:
      img[0:200, 0:200] = overlayList[0]
      cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
      cv2.putText(img, str('1'), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)

    # 6
    if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1] and lmList[tipIds[1]][2]>lmList[tipIds[1]-2][2] and lmList[tipIds[2]][2]>lmList[tipIds[2]-2][2] and lmList[tipIds[3]][2]>lmList[tipIds[3]-2][2] and lmList[tipIds[4]][2]>lmList[tipIds[4]-2][2]:
      img[0:200, 0:200] = overlayList[5]
      cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
      cv2.putText(img, str('6'), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)

    # 7
    if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1] and lmList[tipIds[1]][2]<lmList[tipIds[1]-2][2] and lmList[tipIds[2]][2]>lmList[tipIds[2]-2][2] and lmList[tipIds[3]][2]>lmList[tipIds[3]-2][2] and lmList[tipIds[4]][2]>lmList[tipIds[4]-2][2]:
      img[0:200, 0:200] = overlayList[6]
      cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
      cv2.putText(img, str('e'), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)

    # 8
    if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1] and lmList[tipIds[1]][2]<lmList[tipIds[1]-2][2] and lmList[tipIds[2]][2]<lmList[tipIds[2]-2][2] and lmList[tipIds[3]][2]>lmList[tipIds[3]-2][2] and lmList[tipIds[4]][2]>lmList[tipIds[4]-2][2]:
      img[0:200, 0:200] = overlayList[7]
      cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
      cv2.putText(img, str('e'), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)

    # 9
    if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1] and lmList[tipIds[1]][2]<lmList[tipIds[1]-2][2] and lmList[tipIds[2]][2]<lmList[tipIds[2]-2][2] and lmList[tipIds[3]][2]<lmList[tipIds[3]-2][2] and lmList[tipIds[4]][2]>lmList[tipIds[4]-2][2]:
      img[0:200, 0:200] = overlayList[8]
      cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
      cv2.putText(img, str('e'), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)

    # 10
    if lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1] and lmList[tipIds[1]][2]>lmList[tipIds[1]-2][2] and lmList[tipIds[2]][2]>lmList[tipIds[2]-2][2] and lmList[tipIds[3]][2]>lmList[tipIds[3]-2][2] and lmList[tipIds[4]][2]>lmList[tipIds[4]-2][2]:
      img[0:200, 0:200] = overlayList[9]
      cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
      cv2.putText(img, str('e'), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)

  cTime=time.time()
  fps=1/(cTime-pTime)
  pTime=cTime

  cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN,
              3, (255, 0, 0), 3)
  cv2.imshow("Image", img)
  cv2.waitKey(1)