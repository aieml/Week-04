import numpy as np

array=[[10,50,40],[90,53,12],[21,342,21]]

array=np.array(array)

#array=array.ravel()
array=np.reshape(array,(9,1))

print(array)

print(array.shape)

from sklearn import datasets

digits=datasets.load_digits()

data=digits.data
target=digits.target

print(data.shape)

