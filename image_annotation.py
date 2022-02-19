from email.mime import image
from turtle import color
import cv2 

img = cv2.imread('images/sample.jpg')

cv2.imshow('Origninal image', img)
cv2.waitKey(0)

if img is None:     
    print('Count not read image')

# to draw a line on an image

imageLine = img.copy()

pointA = (200,80)
pointB = (450,80)

# line(image, start_point, end_point, color, thickness)
cv2.line(imageLine, pointA, pointB, (255,255,0), thickness=3, lineType=cv2.LINE_AA)
cv2.imshow('Image line', imageLine)
cv2.waitKey()

# to draw a circle on an image 

imageCircle = img.copy()
circle_center = (415,190)
radius = 100

cv2.circle(imageCircle, circle_center, radius, (0,0,255), thickness=1, lineType=cv2.LINE_AA)
cv2.imshow('Image circle', imageCircle)
cv2.waitKey()

# to draw a filled circle 
imageFilledCircle = img.copy()
circle_center = (415,190)
radius = 100

cv2.circle(imageFilledCircle, circle_center, radius, (255,0,0), thickness=-1, lineType=cv2.LINE_AA)
cv2.imshow('Image with filled circle',imageFilledCircle)
cv2.waitKey()

# to draw a rectangle 
imageRectangle = img.copy()
start_point = (300,115)
end_point = (475,225)

cv2.rectangle(imageRectangle, start_point, end_point, (0,0,255), thickness=1, lineType=cv2.LINE_8)
cv2.imshow('image rectangle', imageRectangle)
cv2.waitKey(0)

# draw an ellipse 
imageEllipse = img.copy()
ellipse_center = (415,190)
axis1 = (100,50)
axis2 = (125,50)

# ellipse(image, centerCoordinates, axesLength, angle, startAngle, endAngle, color, thickness)
cv2.ellipse(imageEllipse, ellipse_center, axis1, 0,0,360,(255,0,0), thickness=1) # horizontal 
cv2.ellipse(imageEllipse, ellipse_center, axis2, 90,0,360,(0,0,255), thickness=1) # vertical 
cv2.imshow('ellipse Image', imageEllipse)
cv2.waitKey()

# adding text - putText(image, text, org, font, fontScale, color)

imageText = img.copy()
text = 'I am a happy dog!'
org = (50,350)

cv2.putText(imageText, text, org, fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale= 1.5, color=(250,225,100))
cv2.imshow('Image text', imageText)
cv2.waitKey()
cv2.destroyAllWindows()
