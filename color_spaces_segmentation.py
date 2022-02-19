from turtle import color
import numpy as np 
import cv2
from matplotlib import pyplot as plt

bright = cv2.imread('images/bright.jpg')
dark = cv2.imread('images/dark.jpg')

bgr = [40,158,16]
thresh = 10 

minBGR = np.array([bgr[0] - thresh, bgr[1] - thresh, bgr[2] - thresh])
maxBGR = np.array([bgr[0] + thresh, bgr[1] + thresh, bgr[2] + thresh])

maskBGR = cv2.inRange(bright, minBGR, maxBGR)
resultBGR = cv2.bitwise_and(bright, bright, mask=maskBGR)

# HSV
brightHSV = cv2.cvtColor(bright, cv2.COLOR_BGR2HSV)

#convert 1D array to 3D, then convert it to HSV and take the first element
# this will be same as shown in the above figure [65, 229, 158]
hsv = cv2.cvtColor( np.uint8([[bgr]] ), cv2.COLOR_BGR2HSV)[0][0]

minHSV = np.array([hsv[0] - thresh, hsv[1] - thresh, hsv[2] - thresh])
maxHSV = np.array([hsv[0] + thresh, hsv[1] + thresh, hsv[2] + thresh])

maskHSV = cv2.inRange(brightHSV, minHSV, maxHSV)
resultHSV = cv2.bitwise_and(brightHSV, brightHSV, mask = maskHSV)

horiz = np.hstack((resultBGR,resultHSV))

cv2.imshow('BGR and HSV masked', horiz)
cv2.waitKey()