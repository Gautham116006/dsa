def rotate_arr(arr, k):
    k = k % len(arr)
    arr = arr[k:] + arr[:k]
    return arr


print(rotate_arr([1, 2, 3, 4, 5], 2))

