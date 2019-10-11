# You can loop over 2 iterables at the same time

a = [1, 2, 3]
b = ['a', 'b', 'c']
for number, letter in zip(a, b):
  print(number, letter)
# 1 a
# 2 b
# 3 c
