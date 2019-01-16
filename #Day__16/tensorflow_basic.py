
# coding: utf-8

# In[35]:


import tensorflow as tf


# In[36]:


a = tf.constant(4.0,tf.float32)
b = tf.constant(6.0,tf.float32)

c = tf.multiply(a,b)
#c = a*b
#sess = tf.Session()
#print(sess.run(c))
#sess.close()

with tf.Session() as sess:
    file_writer = tf.summary.FileWriter('tb_graph',sess.graph) # Create a graph for visualization
    
    c = sess.run(c)
    print(c)


# In[37]:


#  Placeholders helps to assign the value in run time

a = tf.placeholder(tf.int32)
b = tf.placeholder(tf.int32)

c = a + b
sess = tf.Session()
val = sess.run(c,{a:[1,4],b:[7,8]})
print(val)
sess.close()


# ### Neural Network

# In[53]:


# parameters
w = tf.Variable([1.0],tf.float32)
b = tf.Variable([-1.0],tf.float32)

# input and training output
x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)


pred = w*x + b # operation 
square = tf.square(pred - y) # finding the loss
loss = tf.reduce_sum(square) # minimize the loss

optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)


init = tf.global_variables_initializer() # Initialize the variables

sess = tf.Session() # start the session 
sess.run(init) # run the opperation
#print(sess.run(loss,{x:[1,2,3,4],y:[0,1,1,0]})) # print the loss

for i in range(1000):
    sess.run(train,{x:[1,2,3,4],y:[0,-1,1,0]})

print(sess.run([w,b]))

