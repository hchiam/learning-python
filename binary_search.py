import math

targets = [7, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, -1]
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
answers = 0b00111111111101


def exists1(target, array):
    left = 0
    right = len(array) - 1
    while (left <= right):
        # middle = math.floor((left + right) / 2);
        middle = math.floor(left / 2 + right / 2)
        if array[middle] == target:
            return True
        elif array[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return False


def exists2(target, array):
    i = 0
    jump = math.floor(len(array) / 2)
    while jump >= 1:
        while (i + jump < len(array) and array[i + jump] <= target):
            i += jump
        jump = math.floor(jump/2)
    return array[i] == target


for i, target in enumerate(targets):
    solution1 = exists1(target, array)
    solution2 = exists2(target, array)
    answer = True if (answers & (1 << i)) else False
    print('OK' if (solution1 == answer and solution2 == answer) else 'ERROR')
