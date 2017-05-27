# adapted from orignal code found in May 2017: https://en.wikipedia.org/wiki/XOR_cipher

from __future__ import print_function, unicode_literals
from os import urandom


def generate_key(length):
    return urandom(length)

def xor_strings_together(string1, string2):
    # zip "pairs" each element (character) from both lists (strings), up to the shorter length
    # bytes() --> returns byte sequence of integers in range 0-255
    return bytes(a^b for a,b in zip(string1, string2))


message = 'This is the original message.'
print('\nMESSAGE:', message)

key = generate_key(len(message))
print('\nKEY:', key)

cipherText = xor_strings_together(message.encode('utf8'), key)
print ('\nCIPHER TEXT:', cipherText)

decrypted_message = xor_strings_together(cipherText, key).decode('utf8')
print ('\nDECRYPTED:', decrypted_message)

# verify
if decrypted_message == message:
    print('\nUnit test PASSED :)')
else:
    print('\nUnit test FAILED :(')
