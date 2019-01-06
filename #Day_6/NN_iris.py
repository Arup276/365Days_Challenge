############################# Logistic Resression Algorithm ##############################
import matplotlib.pyplot as plt
#%matplotlib inline
import numpy as np

# Data
data = [[5.1,3.5,1.4,0.2,0],
[4.9,3.0,1.4,0.2,0],
[4.7,3.2,1.3,0.2,0],
[4.6,3.1,1.5,0.2,0],
[5.0,3.6,1.4,0.2,0],
[5.4,3.9,1.7,0.4,0],
[4.6,3.4,1.4,0.3,0],
[5.0,3.4,1.5,0.2,0],
[4.4,2.9,1.4,0.2,0],
[4.9,3.1,1.5,0.1,0],
[5.4,3.7,1.5,0.2,0],
[4.8,3.4,1.6,0.2,0],
[4.8,3.0,1.4,0.1,0],
[4.3,3.0,1.1,0.1,0],
[7.0,3.2,4.7,1.4,1],
[6.4,3.2,4.5,1.5,1],
[6.9,3.1,4.9,1.5,1],
[5.5,2.3,4.0,1.3,1],
[6.5,2.8,4.6,1.5,1],
[5.7,2.8,4.5,1.3,1],
[6.3,3.3,4.7,1.6,1],
[4.9,2.4,3.3,1.0,1],
[6.6,2.9,4.6,1.3,1],
[5.2,2.7,3.9,1.4,1],
[5.0,2.0,3.5,1.0,1],
[5.9,3.0,4.2,1.5,1],
[6.0,2.2,4.0,1.0,1],
[6.1,2.9,4.7,1.4,1],
[5.6,2.9,3.6,1.3,1],
[6.7,3.1,4.4,1.4,1],
[5.6,3.0,4.5,1.5,1],
[5.8,2.7,4.1,1.0,1]]

def NN(x1,x2,x3,x4,w1,w2,w3,w4,b):
    z = w1*x1 +w2*x2+x3*w3+x4*w4 +b
    return sigmoid(z)

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_p(x):
    return sigmoid(x)*(1-sigmoid(x))


w1 = np.random.rand()
w2 = np.random.rand()
w3 = np.random.rand()
w4 = np.random.rand()
b = np.random.rand()
learn_rate = 0.2
costs = []
for i in range(100000):
    ri = np.random.randint(len(data))
    #print(ri)
    point = data[ri]
    #print(point[0],point[1],point[2],point[3])
    z = point[0]*w1 +point[1]*w2+point[2]*w3 + point[3]*w4 + b
    #print(z)
    #z1 = np.dot(w.T,point)+b
    #print(z1)
    pred = sigmoid(z) # y^ mean training predict value,Pred = a
    target = point[4] # training set original value,target = y
    #dz = pred - target
    #dw = (1/len(point))*dz.T
    #print(target)
    cost = np.square(pred - target)
    costs.append(cost)
    dcost_pred = 2*(pred - target)
    dpred_dz = sigmoid_p(z)
    
    dz_dw1 = point[0]
    dz_dw2 = point[1]
    dz_dw3 = point[2]
    dz_dw4 = point[3]
    
    dz_db = 10 # bias 
    
    dcose_dz = dcost_pred*dpred_dz
    
    dcost_w1 = dcose_dz*dz_dw1
    dcost_w2 = dcose_dz*dz_dw2
    dcost_w3 = dcose_dz*dz_dw3
    dcost_w4 = dcose_dz*dz_dw4
    dcost_db = dcose_dz*dz_db
    
    
    w1 = w1 - learn_rate*dcost_w1
    w2 = w2 - learn_rate*dcost_w2
    w3 = w3 - learn_rate*dcost_w3
    w4 = w4 - learn_rate*dcost_w4
    b = b - learn_rate*dcost_db
    
plt.plot(costs)

x1 = float(input('Enter sepal length:'))
x2 = float(input('Enter sepal width:'))
x3 = float(input('Enter petal length:'))
x4 = float(input('Enter petal width:'))

mistry = NN(x1,x2,x3,x4,w1,w2,w3,w4,b)
pred = sigmoid(mistry)
print(pred)
