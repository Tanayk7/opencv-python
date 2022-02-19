import numpy as np 
import cv2
from matplotlib import pyplot as plt

rows = 2
columns = 4 
fig = plt.figure(figsize=(10,7))

bright = cv2.imread('images/bright.jpg')
bright = bright[:,:,::-1]

dark = cv2.imread('images/dark.jpg')
dark = dark[:,:,::-1]

# extract original values 
bright_r = bright[:,:,0]
bright_g = bright[:,:,1]
bright_b = bright[:,:,2]

dark_r = dark[:,:,0]
dark_g = dark[:,:,1]
dark_b = dark[:,:,2]

# red_bright = np.zeros(bright.shape)
# red_bright[:,:,2] = bright_r

fig.add_subplot(rows,columns,1)
plt.imshow(bright)
plt.axis('off')
plt.title('bright')

fig.add_subplot(rows, columns, 2)
plt.imshow(bright_r, cmap='gray')
plt.axis('off')
plt.title('bright_red')

fig.add_subplot(rows, columns, 3)
plt.imshow(bright_g, cmap='gray')
plt.axis('off')
plt.title("bright_green")

fig.add_subplot(rows, columns, 4)
plt.imshow(bright_b, cmap='gray')
plt.axis('off')
plt.title("bright_blue")

fig.add_subplot(rows,columns,5)
plt.imshow(dark)
plt.axis('off')
plt.title('dark')

fig.add_subplot(rows, columns, 6)
plt.imshow(dark_r, cmap='gray')
plt.axis('off')
plt.title('dark_red')

fig.add_subplot(rows, columns, 7)
plt.imshow(dark_g, cmap='gray')
plt.axis('off')
plt.title("dark_green")

fig.add_subplot(rows, columns, 8)
plt.imshow(dark_b, cmap='gray')
plt.axis('off')
plt.title("dark_blue")

plt.show()

bright = cv2.imread('images/bright.jpg')
dark = cv2.imread('images/dark.jpg')
brightLAB = cv2.cvtColor(bright, cv2.COLOR_BGR2LAB)
darkLAB = cv2.cvtColor(dark, cv2.COLOR_BGR2LAB)

bright_l = bright[:,:,0]
bright_a = bright[:,:,1]
bright_b = bright[:,:,2]

dark_l = dark[:,:,0]
dark_a = dark[:,:,1]
dark_b = dark[:,:,2]

fig2 = plt.figure(figsize=(10,7))

fig2.add_subplot(rows,columns,1)
plt.imshow(brightLAB)
plt.axis('off')
plt.title('bright')

fig2.add_subplot(rows, columns, 2)
plt.imshow(bright_l)
plt.axis('off')
plt.title('L')

fig2.add_subplot(rows, columns, 3)
plt.imshow(bright_a)
plt.axis('off')
plt.title("A")

fig2.add_subplot(rows, columns, 4)
plt.imshow(bright_b)
plt.axis('off')
plt.title("B")

fig2.add_subplot(rows,columns,5)
plt.imshow(darkLAB)
plt.axis('off')
plt.title('dark')

fig2.add_subplot(rows, columns, 6)
plt.imshow(dark_l)
plt.axis('off')
plt.title('L')

fig2.add_subplot(rows, columns, 7)
plt.imshow(dark_a)
plt.axis('off')
plt.title("A")

fig2.add_subplot(rows, columns, 8)
plt.imshow(dark_b)
plt.axis('off')
plt.title("B")

plt.show()

horiz = np.hstack((bright_l,bright_a,bright_b))
print(horiz.shape)
cv2.imshow('bright lab channels', horiz)
cv2.waitKey()

horiz = np.hstack((dark_l,dark_a,dark_b))
print(horiz.shape)
cv2.imshow('bright lab channels', horiz)
cv2.waitKey()



# mask_in = np.random.randint(2, size = (2, 8))
# mask_ot = np.random.randint(2, size = (6, 16))
# mask_in_amp = mask_in

# dif_row = mask_ot.shape[0]-mask_in_amp.shape[0]
# dif_col = mask_ot.shape[1]-mask_in_amp.shape[1]

# complete_row = dif_row / 2
# complete_col = dif_col / 2

# mask_in_amp = np.vstack((mask_in_amp, np.zeros((complete_row, mask_in_amp.shape[1]))))
# mask_in_amp = np.vstack((np.zeros((complete_row, mask_in_amp.data.shape[1])), mask_in_amp))

# mask_in_amp = np.hstack((mask_in_amp, np.zeros((mask_in_amp.shape[0],complete_col))))
# mask_in_amp = np.hstack((np.zeros((mask_in_amp.shape[0],complete_col)), mask_in_amp))