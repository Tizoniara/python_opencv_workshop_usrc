import cv2
import matplotlib.pyplot as plt

def main():
    pic = cv2.imread('photos\Mascot.png')
    cv2.imshow('cube', pic)
    cv2.waitKey()

if '__name__' == '__main__':
    main()