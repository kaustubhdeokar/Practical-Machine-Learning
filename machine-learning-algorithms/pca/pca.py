import numpy as np
from numpy import linalg
import operator

def covar(a,b):
    s=0
    amean=np.mean(a)
    bmean=np.mean(b)
    s=np.sum((a-amean)*(b-bmean))
    s/=(len(a)-1)
    return s


x=[2.5,0.5,2.2,1.9,3.1,2.3,2,1,1.5,1.1]
y=[2.4,0.7,2.9,2.2,3,2.7,1.6,1.1,1.6,0.9]

meanx=np.mean(x)
x=x-meanx
meany=np.mean(y)
y=y-meany

mat=[]
mat.append([covar(x,x),covar(x,y)])
mat.append([covar(y,x),covar(y,y)])
mat=np.reshape(mat,(2,2))

#eigenvectors
w,v=linalg.eig(mat)

print(w)
print(v)

#order by highest to lowest
d={}
for i in range(len(w)):
    d[w[i]]=v[i]

d1=sorted(d.items(),key=operator.itemgetter(0))
    

print('principal components are:{}'.format(d1))
