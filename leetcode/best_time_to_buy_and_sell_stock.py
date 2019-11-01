"""
Note to self:
rerun "pylint best_time_to_buy_and_sell_stock.py; python3 best_time_to_buy_and_sell_stock.py"
"""

# pylint: disable=invalid-name, too-few-public-methods, no-self-use

class Solution:
    """solution for 'Best Time to Buy and Sell Stock' on leetcode"""
    def maxProfit(self, prices: list) -> int:
        """max profit"""
        profit = 0
        min_price = None
        max_price = None
        for price in prices:
            if min_price is None or price < min_price:
                min_price = price
                max_price = None
            if max_price is None or price > max_price:
                max_price = price
            if min_price is not None and max_price is not None:
                temp = max_price - min_price
                if temp > profit:
                    profit = temp
        return profit

if __name__ == "__main__":
    def check_answer(numbers, correct):
        """helper function"""
        answer = Solution().maxProfit(numbers)
        assert answer == correct, f'{answer} should be {correct}'
        print(answer, 'ok' if answer == correct else 'error')
    check_answer(numbers=[7, 1, 5, 3, 6, 4], correct=5)
    check_answer(numbers=[7, 6, 4, 3, 1], correct=0)
    check_answer(numbers=[], correct=0)
    check_answer(numbers=[1], correct=0)
    check_answer(numbers=[1, 1], correct=0)
    check_answer(numbers=[1, 1, 1, 1, 1, 1], correct=0)
    check_answer(numbers=[1, 2], correct=1)
    check_answer(numbers=[2, 1], correct=0)
    check_answer(numbers=[1, 2, 1], correct=1)
    check_answer(numbers=[1, 2, 2], correct=1)
    check_answer(numbers=[1, 2, 3], correct=2)
    check_answer(numbers=[1, 3, 2], correct=2)
    check_answer(numbers=[7, 1, 3], correct=2)
    check_answer(numbers=[100, 150, 1, 125], correct=124)
    check_answer(numbers=[100, 150, 1, 125], correct=124)
    check_answer(numbers=[10, 11, 1], correct=1)
    check_answer(numbers=[5, 10, 1, 17], correct=16)
    check_answer(numbers=[1, 5, 10, -100, 17, 1], correct=117)
    check_answer(numbers=[2, 1, 2, 1, 0, 1, 2], correct=2)
