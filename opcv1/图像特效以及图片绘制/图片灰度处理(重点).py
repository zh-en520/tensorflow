import cv2
import numpy as np
#方法1
# img = cv2.imread('image0.jpg',0)
# imgInfo = img.shape
# print(imgInfo)
# cv2.imshow('src',img)
# cv2.waitKey(0)

#方法2
# img = cv2.imread('image0.jpg',1)
# imgInfo = img.shape
# height = imgInfo[0]
# width = imgInfo[1]
# dst = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)#颜色空间转换：data数据，BGR->gray
# cv2.imshow('dst',dst)
# cv2.waitKey(0)

#方法3
# img = cv2.imread('image0.jpg',1)
# imgInfo = img.shape
# height = imgInfo[0]
# width = imgInfo[1]
# dst = np.zeros((height,width,3),np.uint8)
# for i in range(0,height):
#     for j in range(0,width):
#         (b,g,r) = img[i,j]
#         gray = (int(r)+int(g)+int(b))/3
#         dst[i,j] = np.uint8(gray)
# cv2.imshow('dst',dst)
# cv2.waitKey(0)

#方法4
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
        gray = b*0.299+g*0.587+r*0.114
        dst[i,j] = np.uint8(gray)
cv2.imshow('dst',dst)
cv2.waitKey(0)