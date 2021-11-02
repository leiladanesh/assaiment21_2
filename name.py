import numpy as np
import cv2

image = np.zeros((600, 600), dtype = "uint8")
image [:,:] = 255

image[150:400,170:210] = 0
image[400:440,170:400]= 0

cv2.imwrite('name.jpg', image)
cv2.imshow('name', image)
cv2.waitKey()