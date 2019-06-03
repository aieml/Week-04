from sklearn.datasets.samples_generator import make_circles
import numpy as np

data,target=make_circles(100,factor=0.1,noise=0.2)

x=data[:,0]
y=data[:,1]

z=np.exp(-(x*x+y*y))

print(z.shape)

from matplotlib import pyplot as plt

for i in range(len(target)):

    if target[i]==0:
        plt.scatter(x[i],z[i],c='r')
    elif target[i]==1:
        plt.scatter(x[i],z[i],c='b')

plt.show()
