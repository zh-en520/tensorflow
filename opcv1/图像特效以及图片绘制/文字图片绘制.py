import cv2
import numpy as np
# img = cv2.imread('image1.jpg',1)
# font = cv2.FONT_HERSHEY_SIMPLEX#定义字体
# cv2.rectangle(img,(200,100),(500,400),(0,255,0),3)#方框：起始位置，当前文字的位置,颜色,宽度
# cv2.putText(img,'this is flow',(100,300),font,1,(200,100,255),2,cv2.LINE_AA)#dst,文字内容,坐标,字体，字体大小，颜色，字体粗细，线条类型
# cv2.imshow('src',img)
# cv2.waitKey(0)


img = cv2.imread('image1.jpg',1)
height = int(img.shape[0]*0.2)
width = int(img.shape[1]*0.2)
imgResize = cv2.resize(img,(width,height))
for i in range(0,height):
    for j in range(0,width):
        img[i+50,j+50] = imgResize[i,j]
cv2.imshow('src',img)
cv2.waitKey(0)