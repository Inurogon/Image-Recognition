import cv2
import numpy as np
#import matplotlib.pyplot as plt
img=cv2.imread("C:\\Users\\admin\\Pictures\\2.png",0)
sift=cv2.xfeatures2d.SIFT_create()
#s2=cv2.SURF()
keypoints=sift.detect(img)
