import unittest

a = 1
b = 24

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(a+b, add(a,b))
    def test_not_equal(self):
        self.assertNotEqual(a+b, add(a,b) + 100)


# this if statement is so that the following code only runs if this .py file is not being imported
if __name__ == '__main__':
    unittest.main()
