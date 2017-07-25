import tensorflow as tf
import pdb

x = tf.placeholder(dtype=tf.float32)
y = tf.placeholder(dtype=tf.float32)

xt = [1,2,3,4,5]
yt = [5,4,3,2,1]

w = tf.Variable([0.1])
b = tf.Variable([0.1])

lin = w*x + b

init = tf.global_variables_initializer()
sess = tf.Session()

#pdb.set_trace()
sess.run(init)

loss = tf.reduce_sum(tf.square(lin-y))
grad  =tf.train.GradientDescentOptimizer(0.001).minimize(loss)

#pdb.set_trace()

for i in range(10000): 
    sess.run(grad,{x:xt,y:yt})
print sess.run(lin,{x:0})

