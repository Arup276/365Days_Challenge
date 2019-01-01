def linear(a,num):
    for i in range(len(a)):
        if a[i] == num:
            return "Element Found at position: {}".format(a.index(a[i]))
    return "Not Found"
