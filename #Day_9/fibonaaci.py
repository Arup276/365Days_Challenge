def fibo(num):
    x,y = 0,1
    print(x,y,'',end = '')
    for i in range(0,num-1):
        z = x+y
        x = y
        y = z
        print(z,'',end = '')
