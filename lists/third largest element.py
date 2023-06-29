def third_largest(arr):
    l1 = arr[0]
    l2 = -1
    l3 = -1
    for num in arr[1:]:
        if num > l1:
            l1, l2, l3 = num, l1, l2
        elif num > l2:
            l2, l3 = num, l2
        elif num > l3:
            l3 = num
    print(l3)
    print(l1)


third_largest(list(x for x in range(2)))


