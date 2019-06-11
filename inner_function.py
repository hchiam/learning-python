# https://realpython.com/inner-functions-what-are-they-good-for/

import sys

if sys.version_info[0] < 3:
    raise Exception("Use Python 3+ to run this file.")

def outer(x):
    def inner(x):
        return x + 1
    y = inner(x)
    print(str(x) + ' ' + str(y))

def factorial(n):
    def handle_errors(n):
        if not isinstance(n, int):
            raise TypeError('not an int')
        if n < 0:
            raise ValueError('must be positive (or zero)')

    def actual_factorial(n):
        if n <= 1:
            print(1)
            return 1
        print(str(n) + ' *','')
        return n * actual_factorial(n-1)
    
    print(str(n) + '! = ')
    return actual_factorial(n)

def get_a_function(number):
    def function_to_get(power):
        # number gets saved here when function_to_get gets returned
        return number ** power
    return function_to_get

# test out the functions that have inner functions:

outer(1)

print()
print(factorial(4))

print()
base = 2
power = 3
to_the_power_of = get_a_function(base)
value_should_be = to_the_power_of(power)
print(f'{base} ^ {power} = {value_should_be}')

