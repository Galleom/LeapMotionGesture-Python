import numpy as np
import pandas as pd
import time,os
import socket
# from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
from sklearn import svm
import pickle
# import matplotlib.pyplot as plt
# import seaborn as sb
# %matplotlib inline
#



##############   SAVE MODEL TO DISK ##########
df = pd.read_csv(r".\gestures\gesture.csv")
X = np.array(df.drop('target',1))
Y = np.array(df.target)

# classifier = svm.SVC(kernel = 'linear' , C=2**5)
# classifier = svm.SVC(kernel = 'linear' , C=2**5)
# classifier = svm.SVC(kernel = 'linear' ,decision_function_shape = 'cvr')
# classifier = svm.SVC()
# classifier = KNeighborsClassifier(5)
# classifier = tree.DecisionTreeClassifier()
# classifier= tree.DecisionTreeClassifier(min_samples_split=2,splitter="best")
# classifier = svm.SVC()

# classifier = svm.SVC(kernel='linear',degree=3)
# classifier = svm.SVC(degree=3)
classifier= tree.DecisionTreeClassifier(min_samples_split=2,splitter="best")
classifier.fit(X,Y)
filename = 'model.sav'
pickle.dump(classifier, open(filename, 'wb'))
print("model saved!")


