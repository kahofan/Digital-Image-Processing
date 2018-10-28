# -*- coding: utf-8 -*-
"""
the code based on official TensorFlow
Created on Fri Oct 26 01:33:08 2018

@author: Lionel
"""

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot = True)

x = tf.placeholder(tf.float32, [None, 784])#定义图片的占位符
W = tf.Variable(tf.zeros([784,10]))#定义权重
b = tf.Variable(tf.zeros([10]))#定义偏移量
y = tf.nn.softmax(tf.matmul(x,W) + b)#猜想值，由0和1组成
y_ = tf.placeholder("float", [None,10])#真实值
cross_entropy = -tf.reduce_sum(y_*tf.log(y))#计算真实值和猜想值的交叉熵
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)#梯度下降算法
init = tf.initialize_all_variables()#定义初始化指令
sess = tf.Session()
print('初始化启动！')
sess.run(init)#初始化启动
print('工作中……')
for i in range(1000):#迭代1000次
  batch_xs, batch_ys = mnist.train.next_batch(100)
  sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})#对抓取的100个点进行梯度下降算法，目的是是的交叉熵最小

correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
print('对手写数字的识别正确率为：',sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}) * 100, '%')