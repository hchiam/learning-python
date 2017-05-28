# reference: https://realpython.com/blog/python/primer-on-python-decorators/

import time

def timePerfWrapper(function):
    def wrapper():
        start = time.time()
        function()
        end = time.time()
        print('Time to run function: ' + str(end - start))
    return wrapper


# this if statement is so that the following code only runs if this .py file is not being imported
if __name__ == '__main__':
    
    # # example use of this .py file:
    # from timeperfdecorator import timePerfWrapper
    
    @timePerfWrapper
    def myFunction():
        print('test print time')
    # test myFunction (now modified by decorator)
    myFunction()
