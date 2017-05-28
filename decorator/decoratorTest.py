# reference: https://realpython.com/blog/python/primer-on-python-decorators/

from myDecorator import myDecoratorFun
from timeperfdecorator import timePerfWrapper

def fun1():
    print('<<< fun1() >>>')

@myDecoratorFun
def fun2():
    print('<<< fun2() >>>')

@myDecoratorFun
@timePerfWrapper
def fun3():
    print('<<< fun3() >>>')

@timePerfWrapper
@myDecoratorFun
def fun4():
    print('<<< fun4() >>>')


# this if statement is so that the following code only runs if this .py file is not being imported
if __name__ == '__main__':
    print('\n1) NO DECORATOR:\n_____________________')
    fun1()
    
    print('\n2) ONE DECORATOR:\n_____________________')
    fun2()
    
    print('\n3) TWO DECORATORS, myDecoratorFun(timePerfWrapper()):\n__________________________________________')
    fun3()
    
    print('\n4) TWO DECORATORS, timePerfWrapper(myDecoratorFun()):\n__________________________________________')
    fun4()
    
    print('\n')
