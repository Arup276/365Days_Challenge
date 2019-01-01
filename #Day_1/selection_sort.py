def selection(arr):
    limit = len(arr)
    for i in range(limit):
        for j in range(i,limit):
            if arr[j] < arr[i]:
                arr[j],arr[i] = arr[i],arr[j]
    return arr

#Time complexcityb is: O(n)
