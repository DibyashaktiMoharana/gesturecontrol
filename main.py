import mediapipe as mp
import cv2
import numpy as np
import screen_brightness_control as sbc
from math import hypot

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
flag = 0

while True:
    a, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    lmList = []
    if results.multi_hand_landmarks:
        for handlandmark in results.multi_hand_landmarks:
            for id, lm in enumerate(handlandmark.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                lmList.append([id, cx, cy])
            mpDraw.draw_landmarks(img, handlandmark, mpHands.HAND_CONNECTIONS)
    
    
    if len(lmList) != 0:
        x1, y1 = lmList[4][1], lmList[4][2] #thumb hai
        x2, y2 = lmList[8][1], lmList[8][2] #index ka tip hai
        
        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
        length = hypot(x2-x1, y2-y1)
        brightness = np.interp(length, [15, 220], [0, 100])
        


        sbc.set_brightness(int(brightness))
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.getWindowProperty('Image', cv2.WND_PROP_VISIBLE) < 1:
        sbc.set_brightness(100)
        flag = 1 
        break

if flag == 1:
    cap.release()
    cv2.destroyAllWindows()
        



   