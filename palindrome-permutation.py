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

def unitTest(passed, string=''):
    if passed:
        print('PASSED :) ' + string)
    else:
        print('FAILED :( ' + string)


if __name__ == '__main__': # do the following if running this .py file directly:
    print('Unit Tests:')
    unitTest(isPalindromePermutation('a') == True, "isPalindromePermutation('a') == True")
    unitTest(isPalindromePermutation('ab') == False, "isPalindromePermutation('ab') == False")
    unitTest(isPalindromePermutation('aba') == True, string="isPalindromePermutation('aba') == True")
    unitTest(isPalindromePermutation('abcba') == True, string="isPalindromePermutation('abcba') == True")
    unitTest(isPalindromePermutation('abcab') == True, string="isPalindromePermutation('abcab') == True")
    unitTest(isPalindromePermutation('ababc') == True, string="isPalindromePermutation('ababc') == True")
    unitTest(isPalindromePermutation('aabbc') == True, string="isPalindromePermutation('aabbc') == True")
    unitTest(isPalindromePermutation('abcbaa') == False, string="isPalindromePermutation('abcbaa') == False")