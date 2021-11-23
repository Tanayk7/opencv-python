import cv2
import numpy as np

image = cv2.imread('images/test.jpg')
cv2.imshow('Original image', image)

b = image[:, :, 0]
g = image[:, :, 1]
r = image[:, :, 2]

print(f'blue channel: {b}')
print(f'green channel: {g}')
print(f'red channel: {r}')

height, width, channels = image.shape
print('height: ', height, ' width: ', width, ' channels: ', channels)

down_width = width // 4
down_height = height // 4

scale_down_x = 0.2
scale_down_y = 0.2

# resize using width and height
# resized_down = cv2.resize(
#     image, (down_width, down_height), interpolation=cv2.INTER_LINEAR)

# resize using scale factor
resized_down = cv2.resize(image, None, fx=scale_down_x,
                          fy=scale_down_y, interpolation=cv2.INTER_CUBIC)
cv2.imshow('Resized down', resized_down)

res_inter_nearest = cv2.resize(
    image, None, fx=scale_down_x, fy=scale_down_y, interpolation=cv2.INTER_NEAREST)
res_inter_linear = cv2.resize(
    image, None, fx=scale_down_x, fy=scale_down_y, interpolation=cv2.INTER_LINEAR)
res_inter_area = cv2.resize(
    image, None, fx=scale_down_x, fy=scale_down_y, interpolation=cv2.INTER_AREA)

vertical = np.concatenate(
    (res_inter_nearest, res_inter_linear, res_inter_area), axis=1)
# Display the image Press any key to continue
cv2.imshow('Inter Nearest :: Inter Linear :: Inter Area', vertical)

cv2.waitKey()
cv2.destroyAllWindows()
