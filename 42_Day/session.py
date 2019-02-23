import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
session = tf.Session()
'''
#Constants
cons_1 = tf.constant(value = [[1.0,2.0]],
                     dtype = tf.float32,
                     name = 'cons_1')

cons_2 = tf.constant(value = [[3.0,4.0]],
                     dtype = tf.float32,
                     name = 'cons_1')

session = tf.Session()
print(session.run(cons_1),session.run(cons_2))


#Variables
var_1 = tf.Variable(initial_value=[1.0],
                    trainable=True,
                    dtype=tf.float32) # if true model can change its value if False then its can't

init = tf.global_variables_initializer() # we have to call this function to initialize the variable value
session.run(init)
print(session.run(var_1))

var_2 = var_1.assign(value=[2.0])
print(session.run(var_2))

# Placeholder
placeholder_1 = tf.placeholder(dtype=tf.float32,
                               shape = (1,4),
                               name='placeholder_1')

print(placeholder_1)
print(session.run(fetches=placeholder_1,feed_dict={placeholder_1:[[1.0,2.0,3.0,4.0]]}))'''

# Operation Node
cons_1 = tf.constant(value=[1.0])
cons_2 = tf.constant(value=[2.0])
placeholder_1 = tf.placeholder(dtype=tf.float32)
#result = cons_1 + cons_2
result = tf.add(x=placeholder_1,y=cons_2,name='result')
#print(session.run(fetches=result,feed_dict={placeholder_1:[2.0]}))

# Y = m*x + c

m = tf.constant(value=[2.0],
                dtype=tf.float32)
c = tf.constant(value=[3.0],
                dtype=tf.float32)
x = tf.placeholder(dtype=tf.float32)

#y = m*x + c

mult = tf.multiply(x=m,y=x,name='multiply')

y = tf.add(x=mult,y=c)

print(session.run(fetches=y,feed_dict={x:[3.0]}))

