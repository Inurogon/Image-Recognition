import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread("F:\\2.png", 0)
img=cv2.GaussianBlur(img,(3,3),0)
dst=cv2.Canny(img,100,150)
print(img.shape)
circles=cv2.HoughCircles(dst,cv2.HOUGH_GRADIENT,1,100,param1=100,param2=30,minRadius=5,maxRadius=300)
#输出返回值,方便查看类型
print(circles)
#输出检测到圆的个数
#print(len(circles[0]))

print('-------------我是条分割线-----------------')
for circle in circles[0]:
   if circle[2]<=50:
        print(circle[2])
        x=int(circle[0])
        y=int(circle[1])
        r=int(circle[2])
        dst=cv2.circle(dst,(x,y),r,(220,20,60),0)   
cv2.imshow('res',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
