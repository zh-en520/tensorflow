#转化为gray
#划分为7*7 8*8 10*10 等若干小方块，0-255中有256个灰度等级，分为若干个等级,每个段灰度等级为256/n,比如8个段，灰度等级为32
#判断每个小方块属于哪个灰度等级
#找到每个方块中灰度等级最多的所有的像素，并求取像素的均值（灰度段中像素的个数）
#用统计出来的均值替代原来的像素值

import cv2
import numpy as np
img = cv2.imread('image1.jpg',1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]

gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
dst = np.zeros((height,width,3),np.uint8)
for i in range(4,height-4):
    for j in range(4,width-4):
        array1 = np.zeros(8,np.uint8)
        for m in range(-4,4):
            for n in range(-4,4):
                p1 = int(gray[i+m,j+n]/32)
                array1[p1] = array1[p1] + 1
        currentMax = array1[0]
        l = 0
        for k in range(0,8):
            if currentMax < array1[k]:
                currentMax = array1[k]
                l = k
        #简化均值
        for m in range(-4,4):
            for n in range(-4,4):
                if gray[i+m,j+n]>=(l*32) and gray[i+m,j+n]<=((l+1)*32):
                    (b,g,r) = img[i+m,j+n]
        dst[i,j] = (b,g,r)
cv2.imshow('dst',dst)
cv2.waitKey(0)