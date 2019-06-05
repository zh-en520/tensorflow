import matplotlib.pyplot as plt
import numpy as np
x = np.array([1,2,3,4,5,6,7,8])
y = np.array([13,25,17,36,21,16,10,15])
# plt.plot(x,y,'r')#折线 1 x  2 y  3 color
# plt.plot(x,y,'g',lw=10)#line宽度
plt.bar(x,y,0.5,alpha=1,color='b')#颜色，透明度，柱状图占用宽度比，x\y轴坐标
plt.show()