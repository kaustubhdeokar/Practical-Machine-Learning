import numpy as np
from numpy import linalg
import operator
from sklearn import datasets
import matplotlib.pyplot as plt
import pandas as pd

def cov(x,y):
    xmean=np.mean(x)
    ymean=np.mean(y)
    s=np.sum((x-xmean)*(y-ymean))
    return s/(len(x)-1)

x=[2.5,0.5,2.2,1.9,3.1,2.3,2,1,1.5,1.1]
y=[2.4,0.7,2.9,2.2,3,2.7,1.6,1.1,1.6,0.9]

xmean=np.mean(x)
ymean=np.mean(y)


x=x-xmean
##print(x)
y=y-ymean
##print(y)

mat=[[cov(x,x),cov(x,y)],[cov(y,x),cov(y,y)]]
w,v=linalg.eig(mat)
print(w)
print(v)
