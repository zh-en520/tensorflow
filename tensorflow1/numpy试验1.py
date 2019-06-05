import numpy as np
data1 = np.array([1,2,3,4,5])
print(data1)
data2 = np.array([[1,2],[3,4]])
print(data2)

#维度
print(data1.shape,data2.shape)
#zeros , ones
print(np.zeros([2,3]),np.ones([2,2]))
#改，查
data2[1,0] = 5#改，矩阵下标索引从0开始算
print(data2)#[[1,2],[5,4]]
print(data2[1,1])#查，-->4
#基本运算
data3 = np.ones([2,3])
print(data3*2)
print(data3/3)
print(data3+2)
#两个矩阵的加减法
data4 = np.array([[1,2,3],[4,5,6]])
print(data3+data4)
print(data3*data4)