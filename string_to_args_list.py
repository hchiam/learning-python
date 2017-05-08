# http://stackoverflow.com/questions/20263839/python-convert-a-string-to-arguments-list
# http://www.python-course.eu/passing_arguments.php
def f(a,b):
    print(a)
    print(b)
x='argument-one argument-two'
args = x.split(' ')
print (args)
f(*args)