from dictAsFile_wrapper import *

myDict =  {'a':1,'b':2,'c':3,'d':5}
fileName = 'wer.pkl'
writeDictToFile(myDict,fileName)
dictBack = readFileToDict(fileName)
print(dictBack)