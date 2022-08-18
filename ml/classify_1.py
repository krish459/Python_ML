from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

# Loading dataset
iris = datasets.load_iris()

# Printing features and labels
features = iris.data
labels = iris.target
# print(features[0], labels[0])
# print(iris.DESCR)

# Training the classifier
clf = KNeighborsClassifier()
clf.fit(features, labels)

preds = clf.predict([[31, 1, 1, 1]]);#example
print(preds) 