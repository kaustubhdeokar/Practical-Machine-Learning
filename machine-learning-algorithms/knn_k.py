import pandas as pd
import numpy as np
import math
import operator

def eucdis(a,b,l):
    dis=0
    for i in range(l):
        dis+=np.square(a[i]-b[i])
    return np.sqrt(dis)

data = pd.read_csv("a.txt",sep=",",header=None)

testSet = [[7.2, 3.6, 5.1, 2.5]]
test = pd.DataFrame(testSet)

distances = {}
sort = {}
 
length=test.shape[1]

for i in range(len(data)):
    dist=eucdis(data.iloc[i],test,length)
    distances[i]=dist[0]

sorted_d=sorted(distances.items(), key=operator.itemgetter(1))
neighbours=[]

for i in range(2):
    neighbours.append(sorted_d[i][0])

