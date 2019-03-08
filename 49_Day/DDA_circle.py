# dependencies
import matplotlib.pyplot as plt
# %matplotlib inline

# taking the radius
r = int(input('Enter thre radius: '))
x,y = 0,r # initialize the point 
x1,y1 = x,y

# function to calculating epsilon
def find_e(r):
    for i in range(20):
        if 2**(i-1) <= r < 2**i:
            return 2**(-i)

e = find_e(r)
point_x = []
point_y = []
while True:
    # calculating the next points
    x2 = x1 + e*y1
    y2 = y1 - e*x2
    point_x.append(int(x2))
    point_y.append(int(y2))
    # reinitialize the current points
    x1 = x2
    y1 = y2
    if ((int(y1) == r) and (int(x1) == 0)): # when we back to the initial point then break the loop 
        break

        # ploting
plt.plot(point_x,point_y) # plot the points 
plt.plot([-r,r],[0,0],color = 'black') # for the under straight lines
plt.plot([0,0],[-r,r],color = 'black')
plt.show()
