def merge(l_arr, r_arr):
    result = []
    i = 0
    j = 0

    while i < len(l_arr) and j < len(r_arr):
        if l_arr[i] < r_arr[j]:
            result.append(l_arr[i])
            i += 1
        else:
            result.append(r_arr[j])
            j += 1
        # end if
    # end while

    return result + l_arr[i:] + r_arr[j:]
# end def merge


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    # end if

    mid_idx = len(arr) // 2
    l_arr = merge_sort(arr[:mid_idx])
    r_arr = merge_sort(arr[mid_idx:])

    return merge(l_arr, r_arr)
# end def merge_sort



