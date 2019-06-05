#最近邻域插值 双线性插值 原理
#src 10*20 dst 5*10
#dsr<-src
#(1,2) <- (2,4)
#dst x->src x:newx
#newx = x*(src行/dst行) ->newx = x(dst:2)*(10/5)=4(src:x)
#newy = y*(src列/dst列)
#12.3 = 12取最近的整数，这就是最近邻域插值

#双线性插值
#A1 = 20% 上+80%下
#B2 = 30% 左+70%右
#1最重点 = A1*20% + A2*80%
#2最重点 = B1*30% + B2*70%
import cv2
import numpy as np
img = cv2.imread('image0.jpg',1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
dstheight = int(height/2)
dstwidth = int(width/2)
dstImage = np.zeros((dstheight,dstwidth,3),np.uint8)#0-255
for i in range(0,dstheight):#行信息
    for j in range(0,dstwidth):#列信息
        iNew= int(i*(height*1.0/dstheight))#乘以1.0是因为要把整数转换为小数位
        jNew = int(j*(width*1.0/dstwidth))
        dstImage[i,j] = img[iNew,jNew]
cv2.imshow('dst',dstImage)
cv2.waitKey(0)