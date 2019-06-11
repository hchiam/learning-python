import decorator as d
print(f'imported module: {d.raise_to_2(2)}')

from decorator import raise_to_2
print(f'imported function: {raise_to_2(2)}')

@d.generate_power(exponent=7)
def raise_to_7(n):
    return n

print(f'imported decorator: {raise_to_7(2)}')

@d.timer
def do_something_slow():
    for _ in range(100):
        sum([i**2 for i in range(10000)])

do_something_slow()
