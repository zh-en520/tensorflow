#矩阵 -- 类比方法
#数组 M行N列[]  内部[]  [里面 列数据]  [] 中括号整体 行数
#[[6,6]]一行两列
import tensorflow as tf
data1 = tf.constant([[6,6]])#一行两列
data2 = tf.constant([[2],[2]])#两行一列
data3 = tf.constant([[3,3]])#一行两列
data4 = tf.constant([[1,2],[3,4],[5,6]])#三行两列
print(data4.shape)#维度
# with tf.Session() as sess:
#     print(sess.run(data4))#打印整体
#     print(sess.run(data4[0]))#打印某一行
#     print(sess.run(data4[:,0]))#所有行第1列
#     print(sess.run(data4[0,0]))#第一行第一列
matMul = tf.matmul(data1,data2)
matAdd = tf.add(data1,data3)
with tf.Session() as sess:
    print(sess.run(matMul))
    print(sess.run(matAdd))