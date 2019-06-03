from sklearn import datasets

digits=datasets.load_digits()

data=digits.data
target=digits.target

img=digits.images

print(data.shape)

print(data[0])

from matplotlib import pyplot as plt

plt.imshow(img[0])
plt.show()

#print(data[0])
#print(target[0])
