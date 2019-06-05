import cv2
import numpy as np
import random
import math

img = cv2.imread('image1.jpg',1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
cv2.imshow('src',img)
#sobel 1 算子模板 2图片卷积 3阙值判决
# [1   2   1               [ 1 0 -1
#  0   0   0                 2 0 -2
#  -1 -2   -1 ]              1 0 -1 ]

#[1 2 3 4] [a b c d]  a*1+b*2+c*3+d*4 = dst
#sqrt(a*a+b*b) = f > th(判决明线)      竖直方向梯度平方+水平方向梯度平方
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
dst = np.zeros((height,width,1),np.uint8)
for i in range(0,height-2):
    for j in range(0,width-2):
        gy = gray[i,j]*1+gray[i,j+1]*2+gray[i,j+2]*1-gray[i+2,j]*1-gray[i+2,j+1]*2-gray[i+2,j+2]*1
        gx = gray[i,j]*1+gray[i+1,j]*2+gray[i+2,j]*1-gray[i,j+2]*1-gray[i+1,j+2]*2-gray[i+2,j+2]*1
        grad = np.math.sqrt(gx*gx+gy*gy)
        if grad > 50:
            dst[i,j] = 230#白色
        else:
            dst[i,j] = 0
cv2.imshow('dst',dst)
cv2.waitKey(0)