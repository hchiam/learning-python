# https://realpython.com/python-coding-interview-tips/

import itertools

friends = ['Aang', 'Batman', 'Cookie Monster', 'Dory', 'Eeyore']

choose = 2
print('\nPermutations:')
print(list(itertools.permutations(friends, r=choose)))
print('\nCombinations:')
print(list(itertools.combinations(friends, r=choose)))
