import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread("C:\\Users\\admin\\Pictures\\1.jpg",0)

kernel = np.ones((5,5),np.uint8)
closing= cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
plt.subplot(1,2,1),plt.imshow(img,'winter')#默认彩色，另一种彩色bgr
plt.subplot(1,2,2),plt.imshow(closing,'winter')
plt.show()
