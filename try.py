import cv2
import time
import numpy as np
# Open the camera
cap = cv2.VideoCapture(0)
 
while True:
    # Read and display each frame
    ret, img = cap.read()
    cv2.rectangle(img, (100, 100), (300, 300), (0, 255, 0), 0)
    cv2.imshow('a',img)
    k = cv2.waitKey(125)
    # Specify the countdown
    j = 30
    # set the key for the countdown to begin
    if k == ord('q'):
        while j>=10:
            ret, img = cap.read()
            # Display the countdown after 10 frames so that it is easily visible otherwise,
            # it will be fast. You can set it to anything or remove this condition and put 
            # countdown on each frame
            if j%10 == 0:
                # specify the font and draw the countdown using puttext
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(img,str(j//10),(250,250), font, 7,(255,255,255),10,cv2.LINE_AA)
            cv2.imshow('a',img)
            cv2.waitKey(125)
            j = j-1
        else:
            ret, frame = cap.read()
            # Display the clicked frame for 1 sec.
            # You can increase time in waitKey also
            # cv2.imshow('Image',frame)
            # cv2.waitKey(5000)
            # Save the frame
            # cv2.imwrite('D:/downloads/camera.jpg',img)
            cv2.rectangle(frame, (100, 100), (300, 300), (0, 255, 0), 0)
            crop_image = frame[100:300, 100:300]
            # cv2.imshow('Image',crop_image)
            # cv2.waitKey(5000)
            blur = cv2.GaussianBlur(crop_image, (3, 3), 0)
            #Change to HSV color scheme
            hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
            mask2 = cv2.inRange(hsv, np.array([0, 48, 80]), np.array([20, 255, 255]))

            kernel = np.ones((5, 5))
            dilation = cv2.dilate(mask2, kernel, iterations=1)
            erosion = cv2.erode(dilation, kernel, iterations=1)

            # Apply Gaussian Blur and Threshold

            filtered = cv2.GaussianBlur(erosion, (3, 3), 0)
            ret, thresh = cv2.threshold(filtered, 127, 255, 0)
            cv2.imshow("Thresholdeded Image", thresh)
            cv2.waitKey(5000)

            #contours  
            contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            try:
                contour = max(contours, key=lambda x: cv2.contourArea(x))
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(crop_image, (x, y), (x + w, y + h), (0, 0, 255), 0)

                #Convex Hull
                hull = cv2.convexHull(contour)
                drawing = np.zeros(crop_image.shape, np.uint8)
                cv2.drawContours(drawing, [contour], -1, (0, 255, 0), 0)
                cv2.drawContours(drawing, [hull], -1, (0, 0, 255), 0)

                hull = cv2.convexHull(contour, returnPoints=False)
                defects = cv2.convexityDefects(contour, hull)
                count_defects = 0

                for i in range(defects.shape[0]):
                    s, e, f, d = defects[i, 0]
                    start = tuple(contour[s][0])
                    end = tuple(contour[e][0])
                    far = tuple(contour[f][0])
                    
                    a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
                    b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
                    c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
                    angle = (math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * 180) / 3.14
                    if angle <= 90:
                        count_defects += 1
                        cv2.circle(crop_image, far, 1, [0, 0, 255], -1)

                    cv2.line(crop_image, start, end, [0, 255, 0], 2)

                if count_defects == 0:
                    cv2.putText(frame, "ONE", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
                elif count_defects == 1:
                    cv2.putText(frame, "TWO", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
                elif count_defects == 2:
                    cv2.putText(frame, "THREE", (5, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
                elif count_defects == 3:
                    cv2.putText(frame, "FOUR", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
                elif count_defects == 4:
                    cv2.putText(frame, "FIVE", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
                else:
                    pass

            except:
                pass

            cv2.imshow("Gesture", frame)
            if cv2.waitKey(1) == ord('q'):
                break

    # Press Esc to exit
    elif k == 27:
        break
cap.release()
cv2.destroyAllWindows()