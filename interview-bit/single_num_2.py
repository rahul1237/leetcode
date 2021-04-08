A = [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]

def leastFrequent(arr, n) :
 
    # Sort the array
    arr.sort()
  
    # find the min frequency using
    # linear traversal
    min_count = n + 1
    res = -1
    curr_count = 1
    for i in range(1, n) :
        if (arr[i] == arr[i - 1]) :
            curr_count = curr_count + 1
        else :
            if (curr_count < min_count) :
                min_count = curr_count
                res = arr[i - 1]
             
            curr_count = 1
             
   
    # If last element is least frequent
    if (curr_count < min_count) :
        min_count = curr_count
        res = arr[n - 1]
     
    return res

print(leastFrequent(A,len(A)))

