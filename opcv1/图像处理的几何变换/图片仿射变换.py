import cv2
import numpy as np

img = cv2.imread('image0.jpg',1)
cv2.imshow('src',img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
#src 3个点 -> dst 3个点(左上角，左下角，右上角)
matsrc = np.float32([[0,0],[0,height-1],[width-1,0]])
matDst = np.float32([[50,50],[300,height-200],[width-300,100]])
#组合,仿射变换矩阵
matAffine = cv2.getAffineTransform(matsrc,matDst)##mat中src和dst
dst = cv2.warpAffine(img,matAffine,(width,height))
cv2.imshow('dst',dst)
cv2.waitKey(0)