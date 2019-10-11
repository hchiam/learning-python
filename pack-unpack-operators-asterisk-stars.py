"""
Demonstrating the powers of the prefix operators * and **
to pack and unpack iterables/arguments.

Reference: https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/#Asterisks_in_list_literals
"""

import sys
if sys.version_info[0] < 3:
    raise Exception("Please use Python 3 or later.")


fruits = ['apple', 'banana', 'coconut', 'durian']
numbers = [1, 2, 3, 4, 5]
print(numbers, fruits, '\n') # [1, 2, 3, ...] ['apple', 'banana', ...]
print(*numbers, *fruits, '\n') # 1, 2, 3, ..., 'apple', 'banana', ...
print([*numbers, *fruits], '\n') # [1, 2, 3, ..., 'apple', 'banana', ...]


def sillyPrint(*items): # "packs" parameters; variable number of arguments!
    for item in items:
        print(item)

sillyPrint('hi', '1', 'hello', '\n')
# hi
# 1
# hello


a = { 'a': 1 }
b = { 'b': 2 }
c = { **a, **b }
print(c, '\n') # {'a': 1, 'b': 2}


def tag(tag_name, **attributes): # attributes unpacks values from keys
    attribute_list = [
        f'{name}="{value}"'
        for name, value in attributes.items()
    ]
    return f"<{tag_name} {' '.join(attribute_list)}>"

print(tag('a', href="https://www.google.com"), '\n') # '<a href="https://www.google.com">'
print(tag('img', height=20, width=40, src="face.jpg"), '\n') # '<img height="20" width="40" src="face.jpg">'
