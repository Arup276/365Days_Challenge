def quicksort(arr):
    quick(arr,0,len(arr)-1)

def quick(arr,start,end):
    if start < end:
        pindex = partition(arr,start,end)
        quick(arr,start,pindex-1)
        quick(arr,pindex+1,end)

def partition(arr,start,end):
    pinde = end
    pivot = arr[pinde]
    index = start
    for i in range(start,end):
        if arr[i] < pivot:
            arr[i],arr[index] = arr[index],arr[i]
            index = index+1
    arr[index],arr[pinde] = arr[pinde],arr[index]
    return index  





###Not in place 
##def quick(a):
##    if len(a) <=1:
##        return a
##    smaller,equal,larger = [],[],[]
##    pivot = a[len(a) - 1]
##    for i in a:
##        if i < pivot:
##            smaller.append(i)
##        elif i > pivot:
##            larger.append(i)
##        else:
##            equal.append(i)
##    return quick(smaller)+equal+quick(larger)




##            temp = arr[i]
##            arr[i] = arr[index]
##            arr[index] = temp
        



            
##    temp = arr[index]
##    print("arr[index]:",arr[index])
##    print("Pivot",pivot)
##    arr[index] = pivot
##    arr[pinde] = arr[index]
##    print("index",index)
##    print(arr)
##    return index
##

##
##
##
##
####def quick_sort(arr):
####    end = len(arr)-1
####    if end > 1:
####        pivot = arr[0]
####        i = 0
####        for j in range(end):
####            if arr[j+1] < pivot:
####                arr[j+1] ,arr[i+1] = arr[i+1],arr[j+1]
####                i +=1
####        arr[0], arr[i] = arr[i],arr[0]
####        first_part = quick_sort(arr[:i])
####        print(first_part)
####        second_part = quick_sort(arr[i+1:])
####        first_part.append(arr[i])
####        return first_part+second_part
####def quicksort(x):
####    if len(x) == 1 or len(x) == 0:
####        return x
####    else:
####        pivot = x[0]
####        i = 0
####        for j in range(len(x)-1):
####            if x[j+1] < pivot:
####                x[j+1],x[i+1] = x[i+1], x[j+1]
####                i += 1
####        x[0],x[i] = x[i],x[0]
####        first_part = quicksort(x[:i])
####        second_part = quicksort(x[i+1:])
####        first_part.append(x[i])
####        
