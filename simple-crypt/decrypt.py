from xor_crypt import *

oldfile = 'encrypted.txt'
newfile = 'decrypted.txt'
keyfile = 'key.txt'

cipherText = ''
with open(oldfile, 'rb') as infile: # rb = read binary
    cipherText = infile.read()

key = ''
with open(keyfile, 'rb') as infile: # rb = read binary
    key = infile.read()

message = xor_strings_together(cipherText, key).decode('utf8')
with open(newfile, 'w') as outfile:
    outfile.write(message)

print('Done.')