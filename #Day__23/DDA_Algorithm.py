import matplotlib.pyplot as plt
#%matplotlib inline

x1 = float(input("Enter X1: "))
x2 = float(input("Enter X2: "))
y1 = float(input("Enter Y1: "))
y2 = float(input("Enter Y2: "))

dx = abs(x2-x1)
dy = abs(y2-y1)

if dx >= dy:
    length = dx
else:
    length = dy

dx = (x2-x1)/length
dy = (y2-y1)/length

x = x1 + 0.5
y = y1 + 0.5
print(x,y)

i = 1
arr_x = []
arr_y = []
while i <= length:
    arr_x.append(int(x))
    arr_y.append(int(y))
    #print(int(x),int(y))
    x += dx
    y += dy
    print(x,y)
    i += 1
plt.plot(arr_x,arr_y)
