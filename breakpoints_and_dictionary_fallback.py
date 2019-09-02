# https://realpython.com/python-coding-interview-tips/
# breakpoints and accessing/setting dictionary values for keys you don't know exist:

test = {'a':1,'b':2,'c':3}
breakpoint() # see value in Pdb with: locals()['test']

# safely get value even if key does not exist:
output = test.get('key_to_check', 'fallback value')
breakpoint() # see value in Pdb with: locals()['output']
output = test.get('a', 'fallback value')
breakpoint() # see value in Pdb with: locals()['output']

# safely set value even if key does not exist:
output = test['asdfas'] = ".setdefault('a', 'set fallback value')"
breakpoint() # see value in Pdb with: locals()['output']
