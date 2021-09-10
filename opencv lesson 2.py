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

# frame = cv2.imread ('..\Photos/collage.png')
# edges = cv2.Canny(frame,100,200) # This uses the canny edge detector. The 100 and 200 are rather arbitrary parameters; the second should be larger than the first, play around to see what numbers work best for each image.

# contours, hierarchy = cv2.findContours(edges,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
# # Get rid of the ones with an area smaller than tiny

# #edges.shape returns a tuple containing width and height
# blankImage = np.zeros(edges.shape)

# goodContours=[]
# for contour in contours:
#     #check if the contour area is greater than 100 non zero pixels
#     if cv2.contourArea(contour)>100:
#         goodContours.append(contour)
#         #redraw our good contours onto our blank canvas
#         #isClosed = is our contour a closed loop
#         #color = white
#         cv2.polylines(blankImage,contour,isClosed=True,color=(255),thickness=1)

# cv2.imshow("original", frame)
# cv2.imshow("edges", edges) 
# cv2.imshow("big contours", blankImage) 
# cv2.waitKey(-1)