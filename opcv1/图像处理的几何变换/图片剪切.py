#x:500->800
#y:1000->1300
import cv2
img = cv2.imread('image0.jpg',1)
imgInfo = img.shape
dst = img[500:1000,200:1300]
cv2.imshow('image',dst)
cv2.waitKey(0)