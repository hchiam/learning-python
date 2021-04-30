# https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/815/

# key insight: when the sum of the squares of the digits cycles, it always eventually repeats a sum
"""
Example:
4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4 (repeat)
"""


class Solution(object):
    def isHappy(self, n: int) -> bool:
        ht = {}
        new_number = n
        while new_number not in ht:
            # print(new_number)
            if new_number is 1:
                return True
            ht[new_number] = True
            digits = [int(x) for x in str(new_number)]
            new_number = self.get_new_number(digits)
        # print(new_number)
        return False

    def get_new_number(self, digits_array: int) -> int:
        output = 0
        for digit in digits_array:
            output += digit ** 2
        return output


s = Solution()
assert s.isHappy(1) is True
assert s.isHappy(2) is False
assert s.isHappy(19) is True
assert s.isHappy(4) is False
