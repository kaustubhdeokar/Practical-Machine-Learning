import numpy as np
from numpy import linalg
import operator
from sklearn import datasets
import matplotlib.pyplot as plt
import pandas as pd


iris=datasets.load_iris()
X=iris.data[:,:2]
d=pd.DataFrame(X)
plt.scatter(d[0],d[1])
from sklearn.mixture import GaussianMixture

gmm=GaussianMixture(n_components=3)
gmm.fit(d)
labels=gmm.predict(d)
print(labels)

d['labels']=labels
d0=d[d['labels']==0]
d1=d[d['labels']==1]
d2=d[d['labels']==2]

plt.scatter(d0[0],d0[1],color="r")
plt.scatter(d1[0],d1[1],color="m")
plt.scatter(d2[0],d2[1],color="y")

plt.show()

