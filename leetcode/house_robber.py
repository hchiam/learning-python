"""
Note to self:
rerun "pylint house_robber.py; python3 house_robber.py"

I use pyright to do static type checking in VSCode
"""

# pylint: disable=invalid-name, too-few-public-methods, no-self-use
from typing import List # so you can do List[int]

# helpful reading: https://leetcode.com/problems/house-robber/discuss/156523/From-good-to-great.-How-to-approach-most-of-DP-problems.

class Solution:
    """solution for 'House Robber' on leetcode"""

    def __init__(self):
        self.memo = {}

    def rob(self, houses: List[int]) -> int:
        """
        Gets the max loot from non-adjacent houses.
        Stores data in the given list of houses.
        """
        if not houses:
            return 0
        return self.rob_recursively(houses, 0)

    def rob_recursively(self, numbers: List[int], i: int) -> int:
        if i >= len(numbers):
            return 0
        if i in self.memo:
            return self.memo[i]
        loot_this_house = numbers[i]
        loot_next_house = self.rob_recursively(numbers, i + 1)
        gap_of_1 = loot_this_house + self.rob_recursively(numbers, i + 2)
        gap_of_2 = loot_next_house
        max_loot = max(gap_of_1, gap_of_2)
        self.memo[i] = max_loot
        return max_loot

if __name__ == "__main__":
    def check_answer(numbers, correct):
        """helper function"""
        answer = Solution().rob(numbers)
        assert answer == correct, f'{answer} should be {correct}'
        print(answer, 'ok' if answer == correct else 'error')
    check_answer(numbers=[], correct=0) # empty
    check_answer(numbers=None, correct=0) # invalid
    check_answer(numbers=[1], correct=1) # simple
    check_answer(numbers=[111], correct=111) # simple
    check_answer(numbers=[1, 2], correct=2)
    check_answer(numbers=[1, 2, 3], correct=4)
    check_answer(numbers=[1, 2, 3, 1], correct=4)
    check_answer(numbers=[2, 7, 9, 3, 1], correct=12)
    check_answer(numbers=[9, 1, 1, 9], correct=18)
    check_answer(numbers=[0], correct=0)
    check_answer(numbers=[1, 0, 0, 0], correct=1)
    check_answer(numbers=[0, 1, 0, 0, 0], correct=1)
    check_answer(numbers=[0, 1, 0, 0, 0], correct=1)
    check_answer(numbers=[1, 0, 1, 0, 0, 1], correct=3)
    check_answer(numbers=[0, 1, 0, 1, 0, 0, 1], correct=3)
    check_answer(numbers=[155, 44, 52, 58, 250, 225, 109, 118, 211, \
        73, 137, 96, 137, 89, 174, 66, 134, 26, 25, 205, 239, 85, 146, \
        73, 55, 6, 122, 196, 128, 50, 61, 230, 94, 208, 46, 243, 105, \
        81, 157, 89, 205, 78, 249, 203, 238, 239, 217, 212, 241, 242, \
        157, 79, 133, 66, 36, 165], correct=4517) # requires fast algorithm
    check_answer(numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], correct=30)
    check_answer(numbers=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], correct=30)
