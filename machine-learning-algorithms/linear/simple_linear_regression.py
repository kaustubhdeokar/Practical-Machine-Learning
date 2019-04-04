import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#y=b0+b1x
def coeff(x,y):
    #for b1
    n=np.size(x)
    x_bar=np.mean(x)
    y_bar=np.mean(y)

    num=np.sum((x-x_bar)*(y-y_bar))
    den=np.sum((x-x_bar)**2)

    b1=num/den

    b0=y_bar-b1*x_bar

    return (b0,b1)

def plot(x,y,b):
    plt.scatter(x,y,marker="o",color="r")
    y_pred=b[0]+b[1]*x
    plt.plot(x,y_pred)

    plt.xlabel('x-label')
    plt.ylabel('y-predictions')

    plt.show()

def main():
    a=pd.read_csv("one.csv")
    x = np.array(a["Hours"]) 
    y = np.array(a["Scores"])    
    b=coeff(x,y)
    print(b[0],b[1])
    plot(x,y,b)

if __name__=="__main__":
    main()
