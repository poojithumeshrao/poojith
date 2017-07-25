import tensorflow as tf
import numpy as np
import pdb

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data',one_hot = True)


#sess = tf.InteractiveSession()

x = tf.placeholder(tf.float32,shape=[None,784])
y = tf.placeholder(tf.float32,shape=[None,10])

w1 = tf.Variable(tf.truncated_normal([5,5,1,32],stddev=0.1))
b1 = tf.Variable(tf.truncated_normal([32],stddev=0.1))
w2 = tf.Variable(tf.truncated_normal([5,5,32,64],stddev=0.1))
b2 = tf.Variable(tf.truncated_normal([64],stddev=0.1))


xconv = tf.reshape(x,[-1,28,28,1])
h1 = tf.nn.relu(tf.nn.conv2d(xconv,w1,strides=[1,1,1,1],padding='SAME')+b1)
p1 = tf.nn.max_pool(h1,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')
h2 = tf.nn.relu(tf.nn.conv2d(p1,w2,strides=[1,1,1,1],padding='SAME')+b2)
p2 = tf.nn.max_pool(h2,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')

#print p2.eval()

w3 = tf.Variable(tf.truncated_normal([7*7*64,1024],stddev=0.1))
b3 = tf.Variable(tf.truncated_normal([1024],stddev=0.1))
w4 = tf.Variable(tf.truncated_normal([1024,10],stddev=0.1))
b4 = tf.Variable(tf.truncated_normal([10],stddev=0.1))
                 
x3 = tf.reshape(p2,[-1,7*7*64])
p3 = tf.nn.relu(tf.matmul(x3,w3) + b3)
p4 = tf.nn.relu(tf.matmul(p3,w4) + b4)


ce = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y , logits = p4))
train = tf.train.AdamOptimizer(1e-4).minimize(ce)
                 

#sess.run(tf.global_variables_initializer())

#pdb.set_trace()

cp = tf.equal(tf.argmax(y,1),tf.argmax(p4,1))
acc = tf.reduce_mean(tf.cast(cp,tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    i = 0
    while True:
        batch = mnist.train.next_batch(50)
        train.run(feed_dict = {x:batch[0],y:batch[1]})
        if i%100 == 0:
            print sess.run(ce,feed_dict = {x:batch[0],y:batch[1]})
            print i
            print acc.eval(feed_dict = {x:batch[0],y:batch[1]})
            print '------------------'
        i+=1
