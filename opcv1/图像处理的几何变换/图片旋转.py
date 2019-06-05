import cv2
import numpy as np

img = cv2.imread('image0.jpg',1)
cv2.imshow('src',img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
#
matRotate = cv2.getRotationMatrix2D((height*0.5,width*0.5),45,0.5)#mat矩阵:旋转的中心点，旋转的角度，缩放的系数
#100*100->25度因为旋转会导致四个角超出图的范围，所以缩放
dst = cv2.warpAffine(img,matRotate,(height,width))
cv2.imshow('dst',dst)
cv2.waitKey(0)