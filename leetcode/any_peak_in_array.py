# https://leetcode.com/problems/find-peak-element

import math


class Solution:
    def findPeakElement(self, numbers: [int]) -> int:
        if not numbers or len(numbers) < 1:
            return -1
        if len(numbers) == 1:
            return 0
        if numbers[0] > numbers[1]:
            return 0
        if numbers[-1] > numbers[-2]:
            return len(numbers)-1
        for i in range(1, len(numbers)-1):
            left = numbers[i-1]
            right = numbers[i+1]
            if numbers[i] > left and numbers[i] > right:
                return i
        return -1

    def findPeakElement_1_liner(self, numbers: [int]) -> int:
        if len(numbers) == 0:
            return -1
        return numbers.index(max(numbers)) if numbers and len(numbers) > 0 else 0

    def findPeakElement_binary(self, numbers: [int]) -> int:
        if not numbers or len(numbers) < 1:
            return -1
        if len(numbers) == 1:
            return 0
        left = 0
        right = len(numbers) - 1
        mid = math.floor((left + right)/2)
        while left < right:
            mid = math.floor((left + right)/2)
            if numbers[mid] <= numbers[mid+1]:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def findPeakElement_log(self, numbers: [int]) -> int:
        if not numbers or len(numbers) < 1:
            return -1
        if len(numbers) == 1:
            return 0

        i = 0
        skip = len(numbers)

        def ok(index):
            return index < len(numbers) and numbers[index-1] <= numbers[index]

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
