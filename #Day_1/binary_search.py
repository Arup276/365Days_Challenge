def binary(arr,num):
    start = 0 # Giving the start position
    end = len(arr)- 1 # last posotion
    while start <= end: # last check for 1 element in the array
        mid = (start+end)//2 # taking int value
        if arr[mid] == num: # check The middle element is search element
            return "Found at position: {}".format(arr.index(arr[mid]))
        if num < arr[mid]:
            end = mid-1 # If searching number less than mid then update end to mid
        elif num > arr[mid]:
            start = mid+1 # id=f src elm is > mid then update str .
    return "Not found"
