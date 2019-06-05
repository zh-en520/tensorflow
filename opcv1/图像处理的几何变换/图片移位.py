import cv2
import numpy as np

img = cv2.imread('image0.jpg',1)
cv2.imshow('src',img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
##
matShift = np.float32([[1,0,100],[0,1,200]])#两行三列
dst = cv2.warpAffine(img,matShift,(height,width))#参数：原始图片data信息；移位矩阵；图片info信息
#目的：移位=矩阵运算
cv2.imshow('dst',dst)
cv2.waitKey(0)

#[[1,0,100],[0,1,200]] 2*3 -->2*2和2*1
#[[1,0],[0,1]] --> 2*2 A
#[[100],[200]] --> 2*1 B
#xy C 输入矩阵
#A*C+B = (2*2)*(2*1)+B = [[1,0],[0,1]]*[[x],[y]]+[[100],[200]] = [[1*x+0*y],[0*x+1*y]]+[[100],[200]]
# = [[x+100],[y+200]]

#像素移位方法
#通过源代码实现图片的移动