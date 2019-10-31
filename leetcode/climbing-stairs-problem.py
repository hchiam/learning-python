"""
To run python linter pylint on this file, run this in the CLI:
pylint pylint_example.py

Or even better, pip3 install rerun and then run this in the CLI:
rerun "pylint pylint_example.py; python3 pylint_example.py"
"""

# pylint: disable = too-few-public-methods, invalid-name

# learn unit testing in python later: https://www.youtube.com/watch?v=6baJ5t83820

class Solution_Number_Pattern_DO_NOT_USE: # really slow (the other solution is better)
    """
    Solution using number pattern for:
    https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/569/
    """
    def __init__(self):
        self.list = set('1')

    def climbStairs(self, number):
        """get answer"""
        if number == 1:
            return 1
        # otherwise
        self.__init__()
        for _ in range(number-1):
            self.list = self.get_next_level()
        options_count = len(self.list)
        return options_count

    def get_next_level(self):
        """get next level up by replacing self.list with new list"""
        new_list = set()
        for i in self.list:
            for index in range(len(i)):
                temporary_string = i[:index] + '1' + i[index:]
                new_list.add(temporary_string)
        new_list_with_2s = new_list.copy()
        for i in new_list:
            for index in range(len(i)):
                if i[index:index+2] == '11':
                    temporary_string = i[:index] + '2' + i[index+2:]
                    new_list_with_2s.add(temporary_string)
        return new_list_with_2s


class Solution_previous_2_steps: # faster solution
    """
    Solution using previous 2 numbers of steps for:
    https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/569/
    """
    def __init__(self):
        self.memo = {0:0, 1:1, 2:2}

    def climbStairs(self, number):
        """example method docstring"""
        if number in self.memo:
            return self.memo[number]
        # otherwise
        self.memo[number] = self.climbStairs(number - 1) + self.climbStairs(number - 2)
        return self.memo[number]


s1 = Solution_Number_Pattern_DO_NOT_USE()
s2 = Solution_previous_2_steps()
print(1)
print('method 1 works: ', s1.climbStairs(1) == 1)
print('method 2 works: ', s2.climbStairs(1) == 1)
print(2)
print('method 1 works: ', s1.climbStairs(2) == 2)
print('method 2 works: ', s2.climbStairs(2) == 2)
print(3)
print('method 1 works: ', s1.climbStairs(3) == 3)
print('method 2 works: ', s2.climbStairs(3) == 3)
print(4)
print('method 1 works: ', s1.climbStairs(4) == 5)
print('method 2 works: ', s2.climbStairs(4) == 5)
print(5)
print('method 1 works: ', s1.climbStairs(5) == 8)
print('method 2 works: ', s2.climbStairs(5) == 8)
