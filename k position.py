def rotate_right(arr, k):
    n = len(arr)
    k %= n
    return arr[-k:] + arr[:-k]


print(rotate_right([1, 2, 3, 4, 5], 2))  
