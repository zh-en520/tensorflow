import cv2
import numpy as np
import random

img = cv2.imread('image1.jpg',1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
cv2.imshow('src',img)
#canny(边缘检测) gray->高斯滤波->边缘检测
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
imgG = cv2.GaussianBlur(gray,(3,3),0)#高斯滤波:src,ksize,sigMax:
dst = cv2.Canny(img,50,50)#canny:image,threshold1(原线),threshold2;图片经过卷积后-->大于threshold就认为是边缘点
cv2.imshow('dst',dst)
cv2.waitKey(0)
