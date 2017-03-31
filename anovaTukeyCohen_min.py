# this .py file runs on python 3
# using python 2.7? download statsmodels: http://statsmodels.sourceforge.net/devel/install.html

# reference: http://cleverowl.uk/2015/07/01/using-one-way-anova-and-tukeys-test-to-compare-data-sets/



# for ANOVA
import numpy as np
from scipy import stats
# for Tukey test
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.multicomp import MultiComparison
# for Cohen's d effect size
from cohensd import getCohensD, evalEffectSize
# for better terminal/commandline usability
import sys
# import time



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
            if any(c.isalpha() for c in line): # check if any characters in line are letters
                currGroup = line + ' ' # account for possibly similar group names
                groupNames.append(currGroup)
            else:
                mytuple = tuple([currGroup,line])
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

def formatDataForCohenCalc(fileData):
    data = {}
    for name in groupNames:
        data[name] = []
    for entry in fileData:
        grpNm = entry[0]
        dtPt = float(entry[1])
        data[grpNm].append(dtPt)
    return data

def printAndSaveCohensD(group1, group2):
    cohens_d = getCohensD(fileData[group1], fileData[group2])
    output_cohend = "Cohen's d: " + group1 + " vs. " + group2 + ": \n\t\t" + str(cohens_d) + '\n'
    output_effectsize = '\t\t' + evalEffectSize(cohens_d) + '\n'
    with open(outputFileName,'a') as f:
        f.write(output_cohend)
        f.write(output_effectsize)



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
anovaPrintout = 'One-way ANOVA\n=============\nF-value: ' + str(f) + '\np-value: ' + str(p) + '\n'
anovaConclusion = 'CONCLUSION:\n-> Significant DIFFERENCE found!' if p < 0.05 else 'CONCLUSION:\n-> NO significant difference found...'

# append to output file
outputFileName = 'output_cohendadded.txt'
with open(outputFileName,'a') as fl:
    fl.write('\nData File: ' + fileName + '\n===========================\n' + anovaPrintout + anovaConclusion + '\n')

if p < 0.05:
    mc = MultiComparison(data['Score'], data['Game'])
    result = mc.tukeyhsd()
    with open(outputFileName,'a') as f:
        f.write(str(result)+'\n')
        f.write('\t\tmeandiff = mean(group2) - mean(group1)\n')
        # f.write('Unique groups:\n')
        # f.write(str(mc.groupsunique)+'\n')
        f.write('Significantly higher:\n')
        f.write(checkWhichSigHigher(str(result),groupNames))


with open(outputFileName,'a') as f:
    f.write('Cohen\'s d effect sizes\n======================\n')

# now get Cohen's d effect sizes:
fileData = formatDataForCohenCalc(fileData)
for i in range(len(groupNames)):
    for j in range(i+1,len(groupNames)):
        group1 = groupNames[i]
        group2 = groupNames[j]
        printAndSaveCohensD(group1, group2)

print('Done analysis. Refresh view of the output txt file to see data.')