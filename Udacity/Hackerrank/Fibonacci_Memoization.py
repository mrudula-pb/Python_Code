
def fib_memo(n, memo):
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n == 2:
        return 1
    else:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

n = 6
memo = [0] * n
value = fib_memo(n, memo)
print(value)