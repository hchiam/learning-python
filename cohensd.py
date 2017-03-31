# this .py file runs on python 3 (NOT python 2)

from statistics import mean, stdev
from math import sqrt


def getCohensD(group1, group2):
    # example: group1 = [3, 15, 8, 5, 14, 19, 4]
    # example: group2 = [3, 14, 15, 9, 2, 6, 5]
    
    # to get Cohen's d effect size, we need differenceInMeans_grp1vs2 and pooledStdDev:
    
    # differenceInMeans_grp1vs2:
    differenceInMeans_grp1vs2 = mean(group1) - mean(group2)
    # pooledStdDev:
    sd1 = stdev(group1)
    sd2 = stdev(group2)
    n1 = len(group1)
    n2 = len(group2)
    pooledStdDev = sqrt( ((n1-1)*sd1**2 + (n2-1)*sd2**2) / (n1+n2-2) ) # or pooledStdDev = sqrt( (sd1**2 + sd2**2) / 2 )
    # Cohen's d effect size:
    cohens_d = differenceInMeans_grp1vs2 / pooledStdDev
    return cohens_d

def evalEffectSize(cohens_d):
    if cohens_d >= 0.8:
        return 'large'
    elif cohens_d >= 0.5:
        return 'medium'
    elif cohens_d >= 0.2:
        return 'small'
    elif cohens_d < 0.2:
        return 'very small'


# this if statement is so that the following code only runs if this .py file is not being imported
if __name__ == '__main__':
    group1 = [3, 15, 8, 5, 14, 19, 4]
    group2 = [3, 14, 15, 9, 2, 6, 5]
    cohens_d = getCohensD(group1, group2)
    print("Cohen's d effect size for Group 1 vs. Group 2: \n\t" + str(cohens_d))
    print('0.2=small 0.5=medium 0.8=large')
    print('Effect size: \n\t' + evalEffectSize(cohens_d))