# example of making the same function have different names

def lowercase(string):
    return string.lower()

downcase = makeLowerCase = lowercase # lowercase has to be the last one

print(lowercase('HELLO WORLD'), ' <- using lowercase()')
print(lowercase('HELLO WORLD'), ' <- using downcase()')
print(lowercase('HELLO WORLD'), ' <- using makeLowerCase()')
