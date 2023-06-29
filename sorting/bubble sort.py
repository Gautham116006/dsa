def bubble_sort(arr):
    LAST_ELE_IDX = len(arr) - 1
    FIRST_ELE_IDX = 0
    REVERSE_TRAVERSE = -1

    for end_index in range(LAST_ELE_IDX, FIRST_ELE_IDX, REVERSE_TRAVERSE):
        for index in range(FIRST_ELE_IDX + 1, end_index + 1):
            if arr[index] < arr[index - 1]:
                arr[index], arr[index - 1] = arr[index - 1], arr[index]
            # end if
        # end for
    # end for

    return arr
# end def bubble_sort


print(bubble_sort([5, 4, 3, 2, 1]))
