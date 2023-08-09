def compute_fib(n):
    fib_arr = [0] * (n + 1)
    fib_arr[0], fib_arr[1] = 0, 1

    for i in range(2, n + 1):
        fib_arr[i] = fib_arr[i - 1] + fib_arr[i - 2]
    # end for

    return fib_arr[-1]
# end def compute_fib


print(compute_fib(10))
