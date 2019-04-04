import matplotlib.pyplot as plt 
import numpy as np
from sklearn import datasets, linear_model, metrics
import pandas as pd
from sklearn.model_selection import train_test_split

data=pd.read_csv("multiple_reg.csv")
X=[]
l=len(data["Funds"])
for i in range(l):
    X.append([data["Funds"][i],data["Rating"][i]])

y=np.array(data["Result"])

xtrain,ytrain,xtest,ytest=train_test_split(X,y,test_size=0.4,random_state=1)

reg=linear_model.LinearRegression()
reg.fit(xtrain,ytrain)
print(reg.coef_)

print(reg.score(xtest,ytest))

