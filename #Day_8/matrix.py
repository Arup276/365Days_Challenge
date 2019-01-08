
import numpy as np

while True:
    i1 = int(input("Enter the dimention of 1st mastrix Row: "))
    j1 = int(input('Col:'))
    i2 = int(input("Enter the dimention of 2nd mastrix Row: "))
    j2 =int(input('Col:'))
    if j1 != i2: # rule of matrix multiplication 1st matrix colunm == 2nd matrix row     
        print("Dimensions are wrong") # if dos;t match try again else break the loop

    else:
        break
shape1 = (i1,i2)
shape2 = (i2,j2)
mat1 = np.zeros(shape1) # creating matrises ,initialize with zero
mat2 = np.zeros(shape2)
res = np.zeros((i1,j2))

#Taking 1st matrix inputs
print("'''''''''''''''''''''''''''''''''''1st Matrix'''''''''''''''''''''''''''''''''")

for i in range(i1):
    for j in range(j1):
        #num = int(input("Enter Elements: "))
        mat1[i][j] = int(input("Enter 1st matrix Elements: "))

#Taking 2nd matrix input
print("'''''''''''''''''''''''''''''''''''2nd Matrix'''''''''''''''''''''''''''''''''")
for i in range(i2):
    for j in range(j2):
        num = int(input("Enter 2nd matrix Elements: ")) 
        mat2[i][j] = num

# Doing multiplication 
res = np.dot(mat1,mat2)

print(res)
