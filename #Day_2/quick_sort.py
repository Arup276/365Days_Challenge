# This quick sort has O(nlogn) time complexcity in average case and its a in place sorting algoritham 
# thats way this is use to most of programming IDE sort().
def quicksort(arr):
    quick(arr,0,len(arr)-1)# you can also call it but then you have to pass start as well as end point 

def quick(arr,start,end):
    if start < end:
        pindex = partition(arr,start,end)
        quick(arr,start,pindex-1)
        quick(arr,pindex+1,end)

def partition(arr,start,end):
    pindex = end
    pivot = arr[pindex]
    index = start
    for i in range(start,end):
        if arr[i] < pivot:
            arr[i],arr[index] = arr[index],arr[i]
            index = index+1
    arr[index],arr[pindex] = arr[pindex],arr[index] # Here i did a simple mistake hole day pivot = arr[index] ...WTF! was that don't do that
    return index  

# Time complexcity: Worst Case: O(n^2)

#Best Explanation in c++ : https://www.youtube.com/watch?v=COk73cpQbFQ

### Not in place 
def quick(a):
    if len(a) <=1:
        return a
    low,equal,high = [],[],[]
    pivot = a[len(a) - 1]
    for i in a:
        if i < pivot:
            low.append(i)
        elif i > pivot:
            high.append(i)
        else:
            equal.append(i)
    return quick(low)+equal+quick(high)




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
