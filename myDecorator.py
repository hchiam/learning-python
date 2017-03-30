# reference: https://realpython.com/blog/python/primer-on-python-decorators/

def myDecoratorFun(function):
    def wrapper():
        print('As a decorator function, I can change your myFunction to do something BEFORE')
        function()
        print('Also, I can do something different AFTER running the original myFunction')
    return wrapper


# this if statement is so that the following code only runs if this .py file is not being imported
if __name__ == '__main__':
    myDecoratorFun()