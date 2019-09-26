# Example using doctest to generate tests from comments:

# import testmod for testing our function 
from doctest import testmod 
  
# define a function to test 
def factorial(n): 
    ''' 
    This function calculates recursively and 
    returns the factorial of a positive number. 
    Define input and expected output: 
    >>> factorial(3) 
    6
    >>> factorial(5) 
    120
    '''
    if n <= 1: 
        return 1
    return n * factorial(n - 1) 
  
# call the testmod function 
if __name__ == '__main__': 
    testmod(name ='factorial', verbose = True) 

# code slightly modified from: https://www.geeksforgeeks.org/testing-in-python-using-doctest-module/
