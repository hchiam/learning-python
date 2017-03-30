def testEqual(a, b):
    try:
        assert a == b
        print('PASSED assertion test a==b')
    except AssertionError:
        print('FAILED assertion test a==b')


# this if statement is so that the following code only runs if this .py file is not being imported
if __name__ == '__main__':
    
    a = 1
    b = 24
    
    print('a = ' + str(a) + ', b = ' + str(b))
    testEqual(a, b)
    
    b = 1
    
    print('a = ' + str(a) + ', b = ' + str(b))
    testEqual(a, b)