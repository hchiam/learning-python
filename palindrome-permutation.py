import unittest


def isPalindromePermutation(string):
    # bit vector
    alphaCount = 0
    for letter in string:
        if alphaCount & (1 << mapToAlphabet(letter)): # == 1 DOES NOT WORK
            # clr
            alphaCount &= ~ (1 << mapToAlphabet(letter))
        else:
            # set
            alphaCount |= (1 << mapToAlphabet(letter))
    notMirroredCount = 0
    for bit in bits(alphaCount):
        if bit > 0:
            notMirroredCount += 1
        if notMirroredCount > 1:
            return False
    return True

def mapToAlphabet(ordinal):
    return ord(ordinal) - ord('a')

def bits(number):
    output = []
    bit = 1 # initialize to right-most bit
    while number >= bit:
        if number & bit:
            output.append(True)
        else:
            output.append(False)
        bit <<= 1 # so can check next bit
    return output

class TestPalPerm(unittest.TestCase):
    def testOneLetter(self):
        self.assertTrue(isPalindromePermutation('a'))
    def testShortExamples(self):
        self.assertFalse(isPalindromePermutation('ab'))
        self.assertTrue(isPalindromePermutation('aba'))
    def testDifferentPermutations(self):
        self.assertTrue(isPalindromePermutation('abcba'))
        self.assertTrue(isPalindromePermutation('abcab'))
        self.assertTrue(isPalindromePermutation('ababc'))
        self.assertTrue(isPalindromePermutation('aabbc'))
    def testOneMore(self):
        self.assertTrue(isPalindromePermutation('ababc'))

if __name__ == '__main__': # do the following if running this .py file directly:
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPalPerm)
    unittest.TextTestRunner(verbosity=2).run(suite)
