import unittest

def doit(s,L):
    if L == 1:
        return s
    lst = s[len(s)-1]
    rst = doit(s[:L-1], L-1)
    output = []
    for r in rst:
        for i in range(len(r)+1):
            output.append(r[:i] + lst + r[i:])
    return output

def getAllPerms(s):
    return doit(s,len(s))

class Test(unittest.TestCase):
    def test(self):
        s = 'abc'
        self.assertEqual(getAllPerms(s),['cba','bca','bac','cab','acb','abc'])

if __name__ == '__main__':
    unittest.main()
