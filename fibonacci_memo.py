memo = {0:0,1:1}

def fib(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

for n in range(0,9):
    print(fib(n))
