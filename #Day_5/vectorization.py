#Vectorization is use for Increase th eexcution time by use of parallisum of CPU or GP

import numpy as np
ar = np.random.rand(10000000)
br = np.random.rand(10000000)
import time
tic = time.time()
c = 0
for i in range(10000000):
    c +=ar[i]*br[i]
    
toc = time.time()
print("Using For loops")
print("Answar is:{}  and time taken is: {} ns".format(c,1000*(toc-tic)))

tic = time.time()
c = 0
c = np.dot(ar,br)
toc = time.time()
print("Using Vectorization")

print("Answar is:{}  and time taken is: {} ns".format(c,1000*(toc-tic)))

