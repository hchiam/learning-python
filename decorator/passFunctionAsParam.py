# reference: https://realpython.com/blog/python/primer-on-python-decorators/

def myDecorator(function):
    def wrapper():
        print('you can do something BEFORE run myFunction')
        function()
        print('you can do something different AFTER run myFunction')
    return wrapper


# this if statement is so that the following code only runs if this .py file is not being imported
if __name__ == '__main__':
    def myFunction(): # define function
        print('run the ORIGINAL myFunction')
    myFunction = myDecorator(myFunction) # change my function (you can use a function itself as an argument!)
    myFunction() # run the "wrapped"/updated function
