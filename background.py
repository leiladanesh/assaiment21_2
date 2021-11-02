# import cv2
# import numpy as np
# img = np.arange(0, 62500, 1, np.uint8)
# img = np.reshape(img, (250,250))
# w,h = img.shape
# for i in range(w):
#         img[i:i+1,:]=255-i
        
# cv2.imshow("gradiant",img)
# cv2.waitKey()


import numpy as np
import cv2

image = np.zeros((500, 500), dtype = "uint8")

for i in range (0,500):
    image[i , 0:500] = 255 - (i/2.5)

cv2.imwrite('gradian.jpg', image)
cv2.imshow('gradian', image)
cv2.waitKey()