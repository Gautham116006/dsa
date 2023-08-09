memo = [-1] * 4


def compute_fib(n):
    if memo[n] == -1:
        if n == 1 or n == 0:
            memo[n] = n
            return n
        else:
            x = compute_fib(n - 1) + compute_fib(n - 2)
            memo[n] = x
            return x
        # end if
    # end if
    return memo[n]
# end def compute_fib


print(compute_fib(3))
