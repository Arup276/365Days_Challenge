import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
cost = []

x_train = [2,3,4,5,6]
Y_train = [4,6,8,10,12]
w = tf.Variable(dtype=tf.float32,initial_value=[1.0])
c = tf.Variable(dtype=tf.float32,initial_value=[1.0])

x = tf.placeholder(dtype=tf.float32)
y_input = tf.placeholder(dtype=tf.float32)

# y = W*x + cw
y_output = tf.add(x=tf.multiply(x=w,y=x,name='multiply'),y=c,name='add')

# Calculate the loss
loss = tf.reduce_sum(input_tensor=tf.square(x=y_output - y_input,name='loss'))
# To minimize the loss function with changing the values of W and c
train_step = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(loss=loss)

# start the session
session = tf.Session()
# initialize the variables
session.run(tf.global_variables_initializer())
# Put the values in the placeholders ,follow from backward computation node
print(session.run(fetches=loss,feed_dict={x:x_train,y_input:Y_train}))

# training step
for i in range(1000):
    session.run(fetches=train_step,feed_dict={x:x_train,y_input:Y_train})
    cost = np.append(cost,session.run(fetches=loss,feed_dict={x:x_train,y_input:Y_train}))
# After training the loss and value of w and c
print(session.run(fetches=[loss,w,c],feed_dict={x:x_train,y_input:Y_train}))
print(session.run(fetches=y_output,feed_dict={x:[7.0,8.0,9.0,10.0]}))

plt.plot(cost)
plt.show()