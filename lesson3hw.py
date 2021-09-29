import cv2
import numpy as np


img = cv2.imread('Faces/usrc_cropped.png')

grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

picFrame = cv2.imread('Faces/imageframe.png')

haarCascade=cv2.CascadeClassifier('Lesson 3 -Faces/haar_face.xml')

facesRect = haarCascade.detectMultiScale(grey,scaleFactor=1.1,minNeighbors=5)

faceCount = 1


for (x,y,w,h) in facesRect:
    faceROI = img[y:y+h,x:x+w,:]
    currentPicFrame = np.zeros((w+40,h+40,3))
    currentPicFrame = cv2.copyTo(picFrame,None)
    currentPicFrame = cv2.resize(currentPicFrame,(w+40,h+40))
    currentPicFrame[20:h+20, 20:w+20,:] = faceROI

    cv2.imwrite('Framed/Image' + str(faceCount) + '.png', currentPicFrame)
    faceCount += 1

cv2.waitKey(-1)
