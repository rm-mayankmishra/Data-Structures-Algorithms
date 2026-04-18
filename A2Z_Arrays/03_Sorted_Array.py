arr = [2, 3, 4, 5, 7, 8, 9]

def sorted_array(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return False
    return True

# TC : O(n)
# SC : O(1)
