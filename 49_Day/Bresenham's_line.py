# dependencies
import matplotlib.pyplot as plt
# %matplotlib inline

# taking the initial and ending point
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))
x,y = x1,y1

# calculating dx adn dy 
dx = x2 - x1
dy = y2 - y1

# calculating the initial decision parameter 
p = 2*dy - dx

# to store the the point and [x] and [y] fro taking the initial points
point_x = [x]
point_y = [y]
while(x < x2):
    x += 1
    if p < 0:
        p = p + 2*dy # if p < 0 the only x will change one unit y will remain same
    else:
        y += 1 # else id p > 0 the x and y both get update by one unit
        p = p - dx # update the decision parameter
    point_x.append(x)
    point_y.append(y)

# plot the points 
plt.plot([x1,x2],[y1,y2],color = 'black',marker = 'o') # to plot the straight line
plt.scatter(point_x,point_y,marker="*") # plot the points 
plt.grid()
plt.plot(point_x,point_y,color = 'red')
plt.show()
