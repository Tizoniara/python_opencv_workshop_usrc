import cv2
import matplotlib.pyplot as plt
import numpy as np

pic = cv2.imread('photos\collage.png')
uncanny = cv2.Canny(pic, 100, 200)

pentagon = cv2.imread('photos\pentagon.png')
pentCanny = cv2.Canny(pentagon, 100, 200)
pentContours, hierarchy = cv2.findContours(pentCanny, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

pentBlank = np.zeros(pentagon.shape)
cv2.polylines(pentBlank, pentContours, True, (255), 1)

pentMoments = cv2.moments(pentContours[1])
pentHuMoments = cv2.HuMoments(pentMoments)

contours, hierarchy = cv2.findContours(uncanny, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

blankImage = np.zeros(uncanny.shape)

goodContours = []
for contour in contours:
    if cv2.contourArea(contour)>100:
        contourMoments = cv2.moments(contour)
        contourHuMoments = cv2.HuMoments(contourMoments)
        delta = np.sum(pentHuMoments - contourHuMoments)
        if(np.abs(delta)<0.002):
            goodContours.append(contour)
            cv2.polylines(blankImage, contour, isClosed = True, color = (255), thickness=1)

cv2.imshow('final', blankImage)

cv2.waitKey(0)
cv2.destroyAllWindows()
