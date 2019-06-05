import tensorflow as tf
# data1 = tf.placeholder(tf.float32)
# data2 = tf.placeholder(tf.float32)
# datadd = tf.add(data1,data2)
# with tf.Session() as sess:
#     print(sess.run(datadd,feed_dict={data1:6,data2:2}))
#     #1.datadd 2data (feed_dict={1:6,2:2}
# print('end!')

# mat0 = tf.constant([[0,0,0],[0,0,0]])
# mat1 = tf.zeros([2,3])#全0矩阵
# mat2 = tf.ones([3,2])#全1矩阵
# mat3 = tf.fill([2,3],15)#填充矩阵
# with tf.Session() as sess:
    # print(sess.run(mat0))
    # print(sess.run(mat1))
    # print(sess.run(mat2))
    # print(sess.run(mat3))

    # =========================================

mat1 = tf.constant([[2],[3],[4]])
mat2 = tf.zeros_like(mat1)
mat3 = tf.linspace(0.0,2.0,11)
mat4 = tf.random_uniform([2,3],-1,2)
with tf.Session() as sess:
    print(sess.run(mat2))
    print('-------')
    print(sess.run(mat3))
    print('-------')
    print(sess.run(mat4))