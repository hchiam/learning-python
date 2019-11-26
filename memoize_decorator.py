def memoize(f):
    memo = {}

    def inner_function(*args):
        if args not in memo:
            memo[args] = f(*args)
        return memo[args]

    return inner_function

@memoize
def factorial(num):
    if int(num) == 1:
        return 1
    else:
        return num * factorial(int(num)-1)

print(factorial(5))
