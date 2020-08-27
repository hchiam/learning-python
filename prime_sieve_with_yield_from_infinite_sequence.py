# https://www.youtube.com/watch?v=5jwV3zxXc8E

def naturals(n):
  yield n
  yield from naturals(n+1)

def sieve(s):
  n = next(s)
  yield n
  yield from sieve(i for i in s if i%n!=0)

primes = sieve(naturals(2))

next(primes) # 2
next(primes) # 3
next(primes) # 5
next(primes) # 7
next(primes) # 11
# ...
