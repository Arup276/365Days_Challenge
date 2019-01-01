def insertion(arr):
    for i in range(1,len(arr)):
        value = arr[i]  
        hole = i
        while hole and arr[hole-1] > value: #Check while hole > 0 and previous value of hole is > current value
            arr[hole] = arr[hole-1] # then take the value from prev hole and sift the hole
            hole -=1
     arr[hole] = value # At the end of while loop put the smallest elemnt in hole
    return arr
            

# Time complexcity: Worst case : O(n^2)    
