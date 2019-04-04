import pandas as pd
import numpy as np
import random



                                                            
file=pd.read_csv('multiple_reg.csv')
dataset=[]
x=file.Funds
y=file.Rating
l=len(x)
for i in range(l):
    dataset.append([x[i],y[i]])
k=int(input('enter k:'))
points=[]
for i in range(k):
    points.append(random.randint(0,l-1))
print(points)
    
    
distance=[]
d=dataset
for i in range(l):
    sub=[]
    for j in range(len(points)):
        ans=(d[i][0]-d[points[j]][0])**2+(d[i][1]-d[points[j]][1])**2
        ans=round(ans,2)
        sub.append(ans)
    distance.append(sub)
print(distance)

#making clusters

num_clusters=[[] for i in range(len(distance[0]))]
for i in range(len(distance)):
    num_clusters[distance[i].index(max(distance[i]))].append(i+1)

a=num_clusters
b=[]
while(a!=b):
    a=



