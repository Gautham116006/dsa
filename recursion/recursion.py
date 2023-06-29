def subst_count(n, s):
    # write for condition when all elements are same
    repeat_str_len = 1
    result = n

    for i in range(1, n):
        if s[i - 1] == s[i]:
            repeat_str_len += 1
        else:
            if repeat_str_len > 1:
                result += repeat_str_len * (repeat_str_len + 1) // 2 - repeat_str_len
                repeat_str_len = 1
            # end if
        # end if
    # end for
    if repeat_str_len > 1:
        result += repeat_str_len * (repeat_str_len + 1) // 2 - repeat_str_len

    # condition for different element in the middle

    index = 1
    pointer = 1
    count = 0
    while index < n:
        while 0 <= index - pointer and index + pointer < n:
            if s[index - pointer] == s[index + pointer] == s[index - 1] != s[index]:
                count += 1
                pointer += 1
            else:
                break
        # end while
        index += 1
        pointer = 1
    # end while

    return result + count


# end def subst_count

print(subst_count(7, "abcbaba"))
