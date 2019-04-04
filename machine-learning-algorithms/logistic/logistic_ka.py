import csv 
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd


dataset=[]
file=pd.read_csv('multiple_reg.csv')
print(file.Funds)
for i in range(len(file.Funds)):
    dataset.append([file.Funds[i],file.Rating[i]])
dataset=np.array(dataset)

