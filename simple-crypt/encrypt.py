from xor_crypt import *

oldfile = 'message.txt'
newfile = 'encrypted.txt'
keyfile = 'key.txt'

message = ''
with open(oldfile, 'r', encoding='utf-8') as infile:
    message = infile.read()

key = generate_key(len(message))
with open(keyfile, 'wb') as outfile: # wb = write binary
    outfile.write(key)

cipherText = xor_strings_together(message.encode('utf8'), key)
with open(newfile, 'wb') as outfile: # wb = write binary
    outfile.write(cipherText)

print('Done.')