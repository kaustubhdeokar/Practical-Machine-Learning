import numpy as np
from matplotlib import pyplot as plt

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_der(x):
    return sigmoid(x)*(1-sigmoid(x))


feature_set = np.array([[0,1,0],[0,0,1],[1,0,0],[1,1,0],[1,1,1]])  
labels = np.array([[1,0,0,1,1]])
labels=labels.reshape(5,1)
np.random.seed(42)
weights=np.random.rand(3,1)
bias=np.random.rand(1)
lr=0.05


for epochs in range(100):
    inputs=feature_set
    xw=np.dot(feature_set,weights)+bias
    z=sigmoid(xw)

    error=z-labels
    print(error.sum())

    dcost_dpred=error
    dpred_dz=sigmoid_der(z)

    z_delta=error*sigmoid_der(z)
    inputs=feature_set.T
    weights-=lr*np.dot(inputs,z_delta)

    for num in z_delta:
        bias-=lr*num
    
    

