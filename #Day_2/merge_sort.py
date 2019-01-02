def merge_sort(arr):
    n = len(arr)
    if n > 1 :
        mid = n//2
        la = arr[:mid] # taking the elements in la till mid -1
        ra = arr[mid:] # taking the element after nid
       
        merge_sort(la) # recursive call to left array
        merge_sort(ra) # recersive call to right array
        i,j,k = 0,0,0
        while i < len(la) and j < len(ra): # Taking element from both left and right array untill they become empty
            if la[i] < ra[j]:
                arr[k] = la[i]
                i +=1
            else:
                arr[k] = ra[j]
                j +=1
            k +=1 # for both of thid condition the k value will update
        while i < len(la): # if right array is empty first
                arr[k] = la[i]
                i +=1
                k +=1
        while j < len(ra): # if left array is empty first
                arr[k] = ra[j]
                j +=1
                k +=1

    return arr
    
# Time complexcity : Worst case: O(nlogn)
