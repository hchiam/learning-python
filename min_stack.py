# MinStack and BetterMinStack:


import math


class MinStack():
    def __init__(self):
        self.s = []

    def push(self, n):
        if len(self.s) == 0:
            self.s.append({'value': n, 'min': n})
        else:
            prev = self.s[-1]
            self.s.append({'value': n, 'min': min(prev['min'], n)})

    def pop(self):
        return self.s.pop()['value']

    def min(self):
        if len(self.s) == 0:
            return math.inf
        return self.s[-1]['min']


s = MinStack()

s.push(3)
s.push(2)
s.push(4)
s.push(1)
print(s.min(), s.pop())
print(s.min(), s.pop())
print(s.min(), s.pop())
print(s.min(), s.pop())
print(s.min())


class BetterMinStack():
    def __init__(self):
        self.s = []
        self.min_stack = []

    def push(self, n):
        length = len(self.min_stack)
        if length == 0 or n < self.min_stack[length-1]:
            self.min_stack.append(n)
        self.s.append(n)

    def pop(self):
        output = self.s.pop()
        if output == self.min_stack[-1]:
            self.min_stack.pop()
        return output

    def min(self):
        if len(self.min_stack) == 0:
            return math.inf
        return self.min_stack[-1]


s = BetterMinStack()

s.push(3)
s.push(2)
s.push(4)
s.push(1)
print(s.min(), s.pop())
print(s.min(), s.pop())
print(s.min(), s.pop())
print(s.min(), s.pop())
print(s.min())
