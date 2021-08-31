import cv2
import matplotlib.pyplot as plt
import numpy as np

pic = cv2.imread('photos\Mascot.png')
(height, width) = pic.shape[:2]

#rescale
scale = 0.5
width = int(pic.shape[1]*scale)
height = int(pic.shape[0]*scale)
dimensions = width, height
rescaled = cv2.resize(pic, dimensions)

#draw a thingy
square_height_center = height/2

height = int(pic.shape[0]/2)
width = int(pic.shape[1]/2)
squared = cv2.rectangle(pic, (height - 100, width -100), (height+100, width+100),(200,100,200), thickness = 10)

#greyscale, blur and canny layer
greyed = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(greyed, (9,9), cv2.BORDER_DEFAULT)
cannied = cv2.Canny(blurred, 125, 200)


#rotate
rotPoint = (width/2, height/2)
rotMat = cv2.getRotationMatrix2D(rotPoint, 45,scale = 1.0)
rotated = cv2.warpAffine(pic, rotMat, (width,height))

cv2.imshow('rescaled', rescaled)
cv2.imshow('squarey', squared)
cv2.imshow('uncanny', cannied)
cv2.imshow('rotary', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()