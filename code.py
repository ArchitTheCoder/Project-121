import cv2
import time
import numpy as np


cap = cv2.VideoCapture(0)
img = cv2.imread("pic.jpeg")

while (cap.isOpened()):
    ret, background = cap.read()

    background = cv2.resize(background, (640, 480))
    img = cv2.resize(img, (640, 480))

    u_black = np.array([104, 153, 70])
    l_black = np.array([30, 30, 0])

    mask = cv2.inRange(background, l_black, u_black)
    res = cv2.bitwise_and(background, background, mask= mask)

    f = background - res
    f = np.where(f == 0, img, f)

    cv2.imshow("blackscreen", background)
    cv2.imshow("maskedvid", f)
    if cv2.waitKey(1):
        break 

cap.release() 
cv2.destroyAllWindows() 