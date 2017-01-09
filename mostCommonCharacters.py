import collections

filename = raw_input('Enter name of file to analyse most common characters:\n')

numOfMostCommonLetters = int(raw_input('Enter number of most common characters to track:\n'))

with open(filename,'r') as f:
    data = f.read() # .replace('\n', '').replace(',', '')
    s = "helloworld"
    print(collections.Counter(data).most_common(numOfMostCommonLetters))