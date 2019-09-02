from collections import Counter
words = "if there was there was but if \
    there was not there was not".split()
counts = Counter(words)
print(counts) # Counter({'there': 4, 'was': 4, 'if': 2, 'not': 2, 'but': 1})
print(counts.most_common(2)) # [('there', 4), ('was', 4)]
