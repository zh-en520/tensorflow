import cv2
import numpy as np

#算法优化：
#定点操作>浮点操作   加减法>乘除法   >>移位操作要更快
img = cv2.imread('image0.jpg',1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
dst = np.zeros((height,width,3),np.uint8)
for i in range(0,height):
    for j in range(0, width):
        (b, g, r) = img[i, j]
        b = int(b)
        g = int(g)
        r = int(r)
        gray = (r*1+g*2+b*1)/4
        # gray = (r+(g>>1)+b)>>2
        dst[i,j] = np.uint8(gray)
cv2.imshow('dst',dst)
cv2.waitKey(0)