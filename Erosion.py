import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("C:\\Users\\admin\\Pictures\\1.jpg",0)

kernel=np.ones((20,20),np.uint8)
erosion=cv2.erode(img,kernel,1)
plt.subplot(1,2,1),plt.imshow(img,'gray')
plt.subplot(1,2,2),plt.imshow(erosion,'gray')
plt.xticks([],plt.yticks([]))
plt.show()
