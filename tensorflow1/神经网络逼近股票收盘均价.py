import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

date = np.linspace(1,15,15)
endPrice = np.array([2511.90,2538.68,2591.66,2732.98,2701.69,2701.29,2678.67,2726.50,2681.50,2739.17,2715.07,2823.53,2864.90,2019.68,2526.32])
beginPrice = np.array([2438.71,2500.88,2534.95,2512.52,2594.04,2743.26,2697.47,2695.24,2678.23,2722.13,2674.93,2744.13,2717.46,2832.73,2653.20])
print(date)
plt.figure()#定义绘图
for i in range(0,15):
    dateone = np.zeros([2])
    dateone[0] = i
    dateone[1] = i
    priceone = np.zeros([2])
    priceone[0] = beginPrice[i]
    priceone[1] = endPrice[i]
    if endPrice[i] > beginPrice[i]:
        plt.plot(dateone,priceone,'r',lw=8)
    else:
        plt.plot(dateone,priceone,'g',lw=8)
# plt.show()
dateNormal = np.zeros([15,1])
priceNormal = np.zeros([15,1])
for i in range(0,15):
    dateNormal[i,0] = i/14.0
    priceNormal[i,0] = endPrice[i]/3000.0
x = tf.placeholder(tf.float32,[None,1])
y = tf.placeholder(tf.float32,[None,1])
#B
w1 = tf.Variable(tf.random_uniform([1,10],0,1))
b1 = tf.Variable(tf.zeros([1,10]))
wb1 = tf.matmul(x,w1)+b1
layer1 = tf.nn.relu(wb1)#激励函数,将当前运算结果成为映射，变成另外一个值
#C
w2 = tf.Variable(tf.random_uniform([10,1],0,1))
b2 = tf.Variable(tf.zeros([15,1]))
wb2 = tf.matmul(layer1,w2)+b2
layer2 = tf.nn.relu(wb2)
loss = tf.reduce_mean(tf.square(y-layer2))#y:真实值 layer2:计算值
#梯度下降法
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)#每次调整的步长,梯度下降法，每次减少0.1,目的是减小loss
#开始运行
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(0,10000):
        sess.run(train_step,feed_dict={x:dateNormal,y:priceNormal})
    pred = sess.run(layer2,feed_dict={x:dateNormal})
    predPrice = np.zeros([15,1])
    for i in range(0,15):
        predPrice[i,0] = (pred*3000)[i,0]
    plt.plot(date,predPrice,'b',lw=1)
plt.show()