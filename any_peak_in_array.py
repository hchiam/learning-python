# https://leetcode.com/problems/find-peak-element

import math


class Solution:
    def findPeakElement(self, nums: [int]) -> int:
        if not nums or len(nums) < 1:
            return -1
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums)-1
        for i in range(1, len(nums)-1):
            left = nums[i-1]
            right = nums[i+1]
            if nums[i] > left and nums[i] > right:
                return i
        return -1

    def findPeakElement_1_liner(self, nums: [int]) -> int:
        if len(nums) == 0:
            return -1
        return nums.index(max(nums)) if nums and len(nums) > 0 else 0

    def findPeakElement_binary(self, nums: [int]) -> int:
        if not nums or len(nums) < 1:
            return -1
        if len(nums) == 1:
            return 0
        left = 0
        right = len(nums) - 1
        mid = math.floor((left + right)/2)
        while left < right:
            mid = math.floor((left + right)/2)
            if nums[mid] <= nums[mid+1]:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def findPeakElement_log(self, nums: [int]) -> int:
        if not nums or len(nums) < 1:
            return -1
        if len(nums) == 1:
            return 0

        i = 0
        skip = len(nums)

        def ok(index):
            return index < len(nums) and nums[index-1] <= nums[index]

        while skip >= 1:
            while ok(i+skip):
                i += skip
            skip = math.floor(skip/2)

        return i


solution = Solution()
print(solution.findPeakElement([1, 2, 3, 2, 4, 5, 6, 1]) in [2, 6])
print(solution.findPeakElement([1, 2, 3, 3, 4, 5, 6, 1]) in [6])
print(solution.findPeakElement([100, 2, 3, 3, 4, 5, 6, 1]) in [0, 6])
print(solution.findPeakElement([1, 2, 3, 4, 4, 5, 6, 777]) in [7])
print(solution.findPeakElement([1]) == 0)
print(solution.findPeakElement([]) == -1)
print('-------')
print(solution.findPeakElement_1_liner([1, 2, 3, 2, 4, 5, 6, 1]) in [2, 6])
print(solution.findPeakElement_1_liner([1, 2, 3, 3, 4, 5, 6, 1]) in [6])
print(solution.findPeakElement_1_liner([100, 2, 3, 3, 4, 5, 6, 1]) in [0, 6])
print(solution.findPeakElement_1_liner([1, 2, 3, 4, 4, 5, 6, 777]) in [7])
print(solution.findPeakElement_1_liner([1]) == 0)
print(solution.findPeakElement_1_liner([]) == -1)
print('-------')
print(solution.findPeakElement_binary([1, 2, 3, 2, 4, 5, 6, 1]) in [2, 6])
print(solution.findPeakElement_binary([1, 2, 3, 3, 4, 5, 6, 1]) in [6])
print(solution.findPeakElement_binary([100, 2, 3, 3, 4, 5, 6, 1]) in [0, 6])
print(solution.findPeakElement_binary([1, 2, 3, 4, 4, 5, 6, 777]) in [7])
print(solution.findPeakElement_binary([1]) == 0)
print(solution.findPeakElement_binary([]) == -1)
print('-------')
print(solution.findPeakElement_log([1, 2, 3, 2, 4, 5, 6, 1]) in [2, 6])
print(solution.findPeakElement_log([1, 2, 3, 3, 4, 5, 6, 1]) in [6])
print(solution.findPeakElement_log([100, 2, 3, 3, 4, 5, 6, 1]) in [0, 6])
print(solution.findPeakElement_log([1, 2, 3, 4, 4, 5, 6, 777]) in [7])
print(solution.findPeakElement_log([1]) == 0)
print(solution.findPeakElement_log([]) == -1)
