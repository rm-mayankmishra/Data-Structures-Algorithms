arr = [1, 3, 5, 14, 20, 99, 34, 5, 7]

# find largest element in arr :



def largestElement(arr):               # index approach
    n = len(arr)
    maximum = arr[0]
  
    for i in range(1, n):
        if arr[i] > maximum:
            maximum = arr[i]
    return maximum


# ------------------------------------

def largestElement2(arr):              #element approach
    maximum = arr[0]
    for num in arr:
        if num > maximum:
            maximum = num

    return maximum
    
