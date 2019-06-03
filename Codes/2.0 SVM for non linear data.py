from sklearn.datasets.samples_generator import make_circles

data,target=make_circles(100,factor=0.1,noise=0.1)

print(data.shape)
print(target.shape)

print(data[0])
print(target[0])

from sklearn.model_selection import train_test_split

train_data,test_data,train_target,test_target=train_test_split(data,target,test_size=0.2)

from sklearn.svm import SVC
#from sklearn.neighbors import KNeighborsClassifier

#clsfr=KNeighborsClassifier()
#clsfr=SVC(kernel='poly',degree=2) #support vector classifier
clsfr=SVC(kernel='linear') #radial bais function

clsfr.fit(train_data,train_target)
results=clsfr.predict(test_data)

from sklearn.metrics import accuracy_score

accuracy=accuracy_score(test_target,results)
print('accuracy:',accuracy)


from matplotlib import pyplot as plt

for i in range(len(target)):

    if target[i]==0:
        plt.scatter(data[i,0],data[i,1],c='r')
    elif target[i]==1:
        plt.scatter(data[i,0],data[i,1],c='b')

plt.show()
