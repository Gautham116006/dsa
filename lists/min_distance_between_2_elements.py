def min_distance(arr, x, y):
    min_distance = len(arr) + 1
    prev_index = 0
    elements = [x, y]

    for i in range(1, len(arr)):
        if arr[i] in elements:
            if arr[i] != arr[prev_index]:
                pass




