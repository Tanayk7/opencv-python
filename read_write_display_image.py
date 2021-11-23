import cv2


# img_color = cv2.imread('test.jpg', cv2.IMREAD_COLOR)

# img_grayscale = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)

# img_unchanged = cv2.imread('test.jpg', cv2.IMREAD_UNCHANGED)

#
# The function cv2.imread() is used to read an image
img_grayscale = cv2.imread('images/test.jpg', cv2.IMREAD_GRAYSCALE)
img_grayscale = cv2.resize(img_grayscale, (600, 600))

cv2.imwrite('images/grayscale.jpg', img_grayscale)
# The function cv2.imshow() is used to display an image in a window.
cv2.imshow('grayscale image', img_grayscale)


# waitKey() waits for a key press to close the window and 0 specifies indefinite loop
cv2.waitKey(0)

# cv2.destroyAllWindows() simply destroys all the windows we created
cv2.destroyAllWindows()

# The function cv2.imwrite() is used to write an image.
