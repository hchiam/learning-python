# this .py file runs on python 3
# using python 2.7?
# download statsmodels: http://statsmodels.sourceforge.net/devel/install.html

# reference: http://cleverowl.uk/2015/07/01/using-one-way-anova-and-tukeys-test-to-compare-data-sets/



# for ANOVA
import numpy as np
from scipy import stats
# # for Tukey test
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.multicomp import MultiComparison
# for better terminal/commandline usability
import sys
import time



def getFileNameFromUser():
    print ("You're using python " + str(sys.version_info[0]) + '.')
    if sys.version_info[0] < 3:
        # interative text input in terminal/commandline
        whichData = raw_input('Enter name of .txt data file to analyze and hit enter:\n\t')
    else:
        # interative text input in terminal/commandline
        whichData = input('Enter .txt data file to analyze:\n\t')
    # get file name whether or not file extension .txt was input
    fileName = (whichData + '.txt') if whichData[-4:] != '.txt' else (whichData)
    print('\nAnalyzing ' + fileName + '...\n')
    return fileName

def getFileData(fileName):
    groupNames = []
    # initialize for appending a list of tuple( [group, value] )
    fileData = []
    # track current group name for the numbers that follow it
    currGroup = ''
    # read file line by line
    with open(fileName,'r') as f:
        for line in f:
            line = line.replace('\n','')
            if not line.isdigit():
                currGroup = line + ' ' # account for possibly similar group names
                groupNames.append(currGroup)
                print('\ngroup = ' + currGroup)
                time.sleep(0.5)
            else:
                mytuple = tuple([currGroup,line])
                print(mytuple)
                fileData.append(mytuple)
    return [fileData, groupNames]

def leftAndRightNamesInLine(line, groupNames):
    i1 = -1
    i2 = -1
    name1 = ''
    name2 = ''
    left = ''
    right = ''
    for name in groupNames:
        if name in line:
            if name1 == '':
                name1 = name
                i1 = line.find(name)
            else:
                name2 = name
                i2 = line.find(name)
    for i in range(len(line)):
        if i == i1:
            left = name1
            right = name2
            break
        if i == i2:
            left = name2
            right = name1
            break
    return [left, right]

def checkWhichSigHigher(tukeyOutput, groupNames):
    printOut = ''
    for line in tukeyOutput.split('\n'):
        if 'True' in line:
            [bigger,smaller] = leftAndRightNamesInLine(line, groupNames)
            printOut += bigger + ' > ' + smaller + '\n'
    return printOut



fileName = getFileNameFromUser()
[fileData,groupNames] = getFileData(fileName)

# create numpy record array (associated group and value per data point)
data = np.rec.array(
    fileData, # list of groups and values would've been here
    dtype = [('Game','U10'),('Score', 'f')]
    )
    # 'U5' means 5 Unicode characters
    # 'i' means integer
    # 'f' means float
    # reference: https://docs.scipy.org/doc/numpy-1.10.0/reference/arrays.dtypes.html#arrays-dtypes-constructing

# get F-value and p-value for one-way ANOVA between three groups
#groupNames = ['group1','group2','group3']
f, p = stats.f_oneway(data[data['Game'] == groupNames[0]].Score,
                      data[data['Game'] == groupNames[1]].Score,
                      data[data['Game'] == groupNames[2]].Score)

# print output and conclusion of the one-way ANOVA between the groups
time.sleep(0.5)
anovaPrintout = 'One-way ANOVA\n=============\nF-value: ' + str(f) + '\np-value: ' + str(p) + '\n'
print('\n' + anovaPrintout)
time.sleep(1)
anovaConclusion = 'CONCLUSION:\n-> Significant DIFFERENCE found!' if p < 0.05 else 'CONCLUSION:\n-> NO significant difference found...'
print(anovaConclusion + '\n')

# append to output file
outputFileName = 'output.txt'
with open(outputFileName,'a') as fl:
    fl.write('Data File: ' + fileName + '\n===========================\n' + anovaPrintout + anovaConclusion + '\n')
time.sleep(1)
print('\nANOVA data appended to ' + outputFileName + '\n')

if p < 0.05:
    time.sleep(1)
    print('Significant DIFFERENCE found\n')
    time.sleep(1)
    print(' -> Tukey test\n')
    
    mc = MultiComparison(data['Score'], data['Game'])
    result = mc.tukeyhsd()
    
    time.sleep(1)
    print(result)
    time.sleep(1)
    print('\t\tmeandiff = mean(group2) - mean(group1)')
    time.sleep(1)
    print('Unique groups:')
    print(mc.groupsunique)
    print('\nSignificantly higher:')
    print(checkWhichSigHigher(str(result),groupNames))
    print('\n')
    
    with open(outputFileName,'a') as f:
        f.write(str(result)+'\n')
        f.write('\t\tmeandiff = mean(group2) - mean(group1)\n')
        f.write('Unique groups:\n')
        f.write(str(mc.groupsunique)+'\n')
        f.write('Significantly higher:\n')
        f.write(checkWhichSigHigher(str(result),groupNames) + '\n')
    
    time.sleep(0.5)
    print('Tukey test data appended to ' + outputFileName + '\n')
