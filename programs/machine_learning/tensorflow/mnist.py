import tensorflow as tf
import numpy as np

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data',one_hot = True)


sess = tf.InteractiveSession()

x = tf.placeholder(tf.float32,shape=[None,784])
y = tf.placeholder(tf.float32,shape=[None,10])

w = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))

sess.run(tf.global_variables_initializer())

yp = tf.matmul(x,w)+b

ce = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y,logits=yp))
train = tf.train.GradientDescentOptimizer(0.5).minimize(ce)
cp = tf.equal(tf.argmax(y,1),tf.argmax(yp,1))
acc = tf.reduce_mean(tf.cast(cp,tf.float32))

for i in range(1000):
    batch = mnist.train.next_batch(100)
    train.run(feed_dict = {x:batch[0],y:batch[1]})
print acc.eval(feed_dict = {x:mnist.test.images,y:mnist.test.labels})
