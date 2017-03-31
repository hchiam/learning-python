# this .py file runs on python 3 (NOT python 2)

from statistics import mean, stdev
from math import sqrt

# example data:
group1 = [3, 15, 8, 5, 14, 19, 4]
group2 = [3, 14, 15, 9, 2, 6, 5]

# to get Cohen's d effect size, we need differenceInMeans_grp1vs2 and pooledStdDev:

# differenceInMeans_grp1vs2:
differenceInMeans_grp1vs2 = mean(group1) - mean(group2)

# pooledStdDev:
sd1 = stdev(group1)
sd2 = stdev(group2)
n1 = len(group1)
n2 = len(group2)
pooledStdDev = sqrt( ((n1-1)*sd1**2 + (n2-1)*sd2**2) / (n1+n2-2) )
# or pooledStdDev = sqrt( (sd1**2 + sd2**2) / 2 )

# Cohen's d effect size:
cohens_d = differenceInMeans_grp1vs2 / pooledStdDev
print("Cohen's d effect size for Group 1 vs. Group 2: \n\t" + str(cohens_d))
print('0.2=small 0.5=medium 0.8=large')

# evaluate effect size:
def evalEffectSize(effectSize):
    if effectSize >= 0.8:
        return 'large'
    elif effectSize >= 0.5:
        return 'medium'
    elif effectSize >= 0.2:
        return 'small'
    elif effectSize < 0.2:
        return 'very small'

print('Effect size: \n\t' + evalEffectSize(cohens_d))
