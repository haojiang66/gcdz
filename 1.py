from sklearn import datasets
digits = datasets.load_digits()
dir(digits)
import matplotlib.pyplot as plt
plt.imshow(digits['images'][1])
plt.savefig("out.png")
# DESCR
# data 64-vector
# images 8*8
# target 0-9
# target_names all 0-9

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

X_train, X_test, y_train, y_test = train_test_split(digits['data'], digits['target'])
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
knn.score(X_test, y_test)
