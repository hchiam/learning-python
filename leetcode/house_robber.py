"""
Note to self:
rerun "pylint house_robber.py; python3 house_robber.py"

I use pyright to do static type checking in VSCode
"""

# pylint: disable=invalid-name, too-few-public-methods, no-self-use
from typing import List # so you can do List[int]

# https://leetcode.com/problems/house-robber/discuss/156523/From-good-to-great.-How-to-approach-most-of-DP-problems.
# my take-away:
# 1) recursive
# 2) recursive memo
# 3) iterative memo
# 4) iterative N variables

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
        if len(houses) == 1:
            return houses[0]
        if len(houses) == 2:
            return max(houses[0], houses[1])
        # return self.rob_recursively(houses, 0)
        return self.rob_iteratively(houses)

    def rob_recursively(self, houses: List[int], i: int) -> int:
        """
        TO FIND A RECURSIVE SOLUTION: THINK OF THE BASE CASES!!!
        Either (1) loot this house (and then must skip next one),
        or (2) don't loot this house (and loot the next one).
        If you don't loot this house and not the next one either,
        then you're being silly and are better off with case (1) above anyways.
        """
        if i >= len(houses):
            return 0
        if i in self.memo:
            return self.memo[i]
        loot_this_house_and_next_house = houses[i] + self.rob_recursively(houses, i + 2)
        loot_next_house = self.rob_recursively(houses, i + 1)
        max_loot = max(loot_this_house_and_next_house, loot_next_house)
        self.memo[i] = max_loot
        return max_loot

    def rob_iteratively(self, houses: List[int]) -> int:
        """
        iterative solution: loot up to the NEXT house =
        either (1) loot from this house,
        or (2) loot 
        """
        self.memo[0] = houses[0]
        # loop starting at the 2nd house:
        for i in range(1, len(houses)):
            if i - 2 < 0: # as if only getting 2nd house
                loot_this_house_and_2_ago = houses[i]
            else: # otherwise i - 2 is a valid index
                loot_this_house_and_2_ago = houses[i] + self.memo[i - 2]
            loot_previous_house = self.memo[i - 1]
            self.memo[i] = max(loot_this_house_and_2_ago, loot_previous_house)
        return self.memo[len(houses) - 1]

if __name__ == "__main__":
    def check_answer(houses, correct):
        """helper function"""
        answer = Solution().rob(houses)
        assert answer == correct, f'{answer} should be {correct}'
        print(answer, 'ok' if answer == correct else 'error')
    check_answer(houses=[], correct=0) # empty
    check_answer(houses=None, correct=0) # invalid
    check_answer(houses=[1], correct=1) # simple
    check_answer(houses=[111], correct=111) # simple
    check_answer(houses=[1, 2], correct=2)
    check_answer(houses=[1, 2, 3], correct=4)
    check_answer(houses=[1, 2, 3, 1], correct=4)
    check_answer(houses=[2, 7, 9, 3, 1], correct=12)
    check_answer(houses=[9, 1, 1, 9], correct=18)
    check_answer(houses=[0], correct=0)
    check_answer(houses=[1, 0, 0, 0], correct=1)
    check_answer(houses=[0, 1, 0, 0, 0], correct=1)
    check_answer(houses=[0, 1, 0, 0, 0], correct=1)
    check_answer(houses=[1, 0, 1, 0, 0, 1], correct=3)
    check_answer(houses=[0, 1, 0, 1, 0, 0, 1], correct=3)
    check_answer(houses=[155, 44, 52, 58, 250, 225, 109, 118, 211, \
        73, 137, 96, 137, 89, 174, 66, 134, 26, 25, 205, 239, 85, 146, \
        73, 55, 6, 122, 196, 128, 50, 61, 230, 94, 208, 46, 243, 105, \
        81, 157, 89, 205, 78, 249, 203, 238, 239, 217, 212, 241, 242, \
        157, 79, 133, 66, 36, 165], correct=4517) # requires fast algorithm
    check_answer(houses=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], correct=30)
    check_answer(houses=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], correct=30)
