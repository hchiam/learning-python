"""
Note to self:
rerun "pylint max_subarray_sum.py; python3 max_subarray_sum.py"

I use pyright to do static type checking in VSCode
"""

# pylint: disable=invalid-name, too-few-public-methods, no-self-use
from typing import List, Optional # so you can do List[int]

class Solution:
    """solution for 'Maximum Subarray' on leetcode"""

    def maxSubArray(self, nums: List[int]) -> Optional[int]:
        """max sum of contiguous non-empty subarray"""
        max_sum = nums[0] # fallback to first element
        temporary_sum = nums[0]
        for i in range(1, len(nums)): # go through the rest of the array
            n = nums[i]
            adding_helps = (temporary_sum + n > n)
            if adding_helps:
                temporary_sum += n
            else: # restarting is better
                temporary_sum = n
            # update max
            max_sum = max(max_sum, temporary_sum)
        return max_sum

if __name__ == "__main__":
    def check_answer(numbers, correct):
        """helper function"""
        answer = Solution().maxSubArray(numbers)
        assert answer == correct, f'{answer} should be {correct}'
        print(answer, 'ok' if answer == correct else 'error')
    check_answer(numbers=[1], correct=1)
    check_answer(numbers=[1, 2], correct=3)
    check_answer(numbers=[1, 2, 3], correct=6)
    check_answer(numbers=[1, 2, 3, 4, 5], correct=15)
    check_answer(numbers=[-1, -2, -3], correct=-1)
    check_answer(numbers=[-3, -1, -2, -3], correct=-1)
    check_answer(numbers=[-2, 1, -3, 4, -1, 2, 1, -5, 4], correct=6)
    check_answer(numbers=[-2, -1, -3, 7, -5, 2, 1, -1, 10], correct=14)
    check_answer(numbers=[0, 0, 0], correct=0)
    check_answer(numbers=[0, 0, 0, -1], correct=0)
    check_answer(numbers=[0, 0, 0, 1], correct=1)
