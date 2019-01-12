#!/usr/bin/env python
# coding: utf-8

# In[29]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[30]:


data = [[3,1.5,1],
       [2,1,0],
       [4,1.5,1],
       [3.5,.5,1],
       [2,.5,0],
       [5.5,1,1],
       [1,1,0]]

mistery_flower = [4.5,1]


# In[ ]:





# In[31]:


def sigmoid(x,dev = False):
    if dev == True:
        return sigmoid(x)*(1-sigmoid(x))
    return 1/(1+np.exp(-x))


# In[32]:


T = np.linspace(-6,6,100)
y = sigmoid(T,True)
yp = sigmoid(T)
plt.plot(T,yp,c='r')
plt.plot(T,y)


# In[51]:


# training loop
w1 = np.random.rand()
w2 = np.random.rand()
b = np.random.rand()
costs = []
learning_rate = .2
for i in range(50000):
    ri = np.random.randint(len(data))
    point = data[ri]
    z = point[0]*w1 + point[1]*w2+b
    pred = sigmoid(z)
    target = point[2]
    cost = np.square(pred - target)# L(w,b)
    
    costs.append(cost)
    dcost_pred = 2*(pred - target) # dL/dz
    dpred_dz = sigmoid(z,True)# da
    dz_dw1 = point[0]
    dz_dw2 = point[1]
    dz_db = 1
    #chain rule
    dcost_dw1 = dcost_pred * dpred_dz *dz_dw1
    dcost_dw2 = dcost_pred * dpred_dz *dz_dw2
    dcost_db = dcost_pred * dpred_dz *dz_db
    
    w1 = w1 - learning_rate*dcost_dw1
    w2 = w2 - learning_rate*dcost_dw2
    b = b - learning_rate*dcost_db
plt.plot(costs)


# In[69]:


z = mistery_flower[0]*w1+mistery_flower[1]*w2 +b
pred = sigmoid(z)
print(pred)


# In[70]:


import os


# In[71]:


def which_flower(length,width):
    z = length*w1+width*w2 +b
    pred = sigmoid(z)
    if pred < .5:
        os.system("say blue")
    else:
        os.system("say red")


# In[73]:


which_flower(4.5,1)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




