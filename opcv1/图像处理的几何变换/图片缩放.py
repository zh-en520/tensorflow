#图片加载load 图片信息info 调用resize方法 检查check
import cv2
img = cv2.imread('image0.jpg',1)
imgInfo = img.shape
print(imgInfo)
height = imgInfo[0]
width = imgInfo[1]
mode = imgInfo[2]
#放大 缩小 等比例 非等比例
dstHeight = int(height*0.5)
dstwidth = int(width*0.5)
#最近邻域插值 双线性插值 像素关系重采样 立方插值
dst = cv2.resize(img,(dstwidth,dstHeight))
cv2.imshow('image',dst)
cv2.waitKey(0)