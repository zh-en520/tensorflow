import cv2
import numpy as np

newImageInfo = (500,500,3)
dst = np.zeros(newImageInfo,np.uint8)
#dst\左上角\右下角\颜色\-1:需要填充--n>0:边的宽度
cv2.rectangle(dst,(50,100),(200,300),(0,0,255),-1)
#dst|圆心|半径|颜色|-1:需要填充--n>0:边的宽度
cv2.circle(dst,(250,250),(50),(0,255,0),2)
#dst|center|轴长|偏转角度|圆弧起始角度|终止角度|颜色|-1:需要填充--n>0:边的宽度
cv2.ellipse(dst,(256,256),(150,100),0,0,180,(255,255,0),-1)

points = np.array([[150,50],[140,140],[200,170],[250,250],[150,50]],np.int32)
print(points.shape)
points = points.reshape((-1,1,2))
print(points.shape)
cv2.polylines(dst,[points],True,(0,255,255))
cv2.imshow('dst',dst)
cv2.waitKey(0)