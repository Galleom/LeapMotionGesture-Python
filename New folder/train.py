import numpy as np
import pandas as pd
import time,os
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
from sklearn import svm
# import matplotlib.pyplot as plt
import seaborn as sb
# %matplotlib inline
#
fileUnity = r".\communication\unity.txt";
filePython = r".\communication\python.txt";





resultadoAnterior = "";

lastTimeUnity  = "";


df = pd.read_csv(r".\gestures\gesture.csv")
X = np.array(df.drop('target',1))
Y = np.array(df.target)
# knn = svm.SVC(kernel = 'linear' , C=2**5)

# knn = svm.SVC(kernel = 'linear' , C=2**5)
# knn = svm.SVC(kernel = 'linear' ,decision_function_shape = 'cvr')

knn = svm.SVC()
# knn = KNeighborsClassifier(5)
# knn = tree.DecisionTreeClassifier()
knn.fit(X,Y)
file = open(fileUnity)


def predict( ):
   file = open(fileUnity)

   while True:
    line = file.readline()
    if not line:
        break

    line = line.rstrip('\n')
    # print(line)
    mylist = [float(x) for x in line.split(',')]

    # print(mylist)
    result = knn.predict([mylist])


    return result[0]

   # file.close()



while(1):
    # tempTime = time.ctime(os.stat(fileUnity).st_atime)
    # if (lastTimeUnity != tempTime):
    #     lastTimeUnity = tempTime


    resultado = predict()
    if(resultado != None):
        if(resultadoAnterior != resultado ):
            resultadoAnterior = resultado

            try:
            	print(resultado)
            	with open(filePython, 'w') as file_python:
	                file_python.write(resultado + '\n')
	                file_python.close()
            except Exception:
	            print("Erro ao ler arquivo filePython")


    time.sleep(.02)


#
# input("Press Enter to continue...")
# predict();
