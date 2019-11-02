"""
Note to self:
rerun "pylint house_robber.py; python3 house_robber.py"

I use pyright to do static type checking in VSCode
"""

# pylint: disable=invalid-name, too-few-public-methods, no-self-use
from typing import List # so you can do List[int]

# This solution is a rework of:
# https://leetcode.com/problems/house-robber/discuss/416524/Python-O(n)-iterative-with-explanation
class Solution:
    """solution for 'House Robber' on leetcode"""

    def rob(self, numbers: List[int]) -> int:
        """
        Gets the max loot from non-adjacent houses.
        Stores data in the given list of houses.
        """

        if not numbers: # empty or invalid input
            return 0

        houses = list(numbers) # edit a copy instead of the original

        # handle trivial cases:
        if len(houses) == 1:
            return houses[0]
        if len(houses) == 2:
            return max(houses[0], houses[1])

        """
        Intuition: To maximize loot, you can only have gaps of 1 or 2.
        You can run in O(n) time instead of O(2^n) time if you track
        running totals inside the array itself.
        """
        max_3_back = houses[0]
        for i in range(2, len(houses)):
            if houses[i-2] > max_3_back:
                houses[i] += houses[i-2]
                # in the next step, this will be the value 3 back:
                max_3_back = houses[i-2]
            else:
                houses[i] += max_3_back

        return max(houses[-1], houses[-2])

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

# helpful reading: https://leetcode.com/problems/house-robber/discuss/156523/From-good-to-great.-How-to-approach-most-of-DP-problems.
