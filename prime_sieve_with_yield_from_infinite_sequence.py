# https://www.youtube.com/watch?v=5jwV3zxXc8E

def naturals(n):
    yield n
    yield from naturals(n+1)


def sieve(iterable):
    n = next(iterable)
    yield n
    yield from sieve(i for i in iterable if i % n != 0)


first_prime = 2
primes = sieve(naturals(first_prime))

print(next(primes))  # 2
print(next(primes))  # 3
print(next(primes))  # 5
print(next(primes))  # 7
print(next(primes))  # 11
# ...
