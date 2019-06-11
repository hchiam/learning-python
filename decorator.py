# https://realpython.com/inner-functions-what-are-they-good-for/#conclusion
# https://realpython.com/primer-on-python-decorators

import functools
import time

def is_being_called_directly():
    return __name__ == "__main__"

def generate_power(exponent):
    def decorator(callback): # note the callback function!
        @functools.wraps(callback) # preserve info of original function
        def inner(*args, **kwargs):
            result = callback(*args, **kwargs) # insert callback function call here!
            return result ** exponent
        return inner # end of inner function
    return decorator # end of decorator function that returns inner function

@generate_power(exponent=2)
def raise_to_2(n):
    return n

if is_being_called_directly():
    print(raise_to_2(2))

@generate_power(exponent=3)
def raise_to_3(n):
    return n

if is_being_called_directly():
    print(raise_to_3(2))


def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func) # preserve info of original function
    def wrapper_timer(*args, **kwargs): # decorator wrapper around the func
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Using @timer decorator: Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer # return the decorator wrapper around the func

@timer
def run_process(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

if is_being_called_directly():
    run_process(num_times=1)
    run_process(num_times=2)
    run_process(num_times=3)
    run_process(num_times=4)
    run_process(num_times=4)
