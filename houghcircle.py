import cv2
import numpy as np

img = cv2.imread('hahaha.bmp', 0)
img = cv2.medianBlur(img,5)
gray = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1=290,param2=55,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))
cropSize = (100, 100)
for i in circles[0,:]:
    cv2.circle(gray,(i[0],i[1]),i[2],(0,255,0),2)
    cv2.circle(gray,(i[0],i[1]),2,(0,0,255),3)
    cropCoords = (max(0, i[1]-cropSize[0]//2), min(img.shape[0], i[1]+cropSize[0]//2), max(0, i[0]-cropSize[1]//2), min(img.shape[1], i[0]+cropSize[1]//2))
    crop = gray[cropCoords[0]:cropCoords[1],cropCoords[2]:cropCoords[3]]

cv2.imshow('final',crop)
cv2.waitKey(0)
cv2.destroyAllWindows()

