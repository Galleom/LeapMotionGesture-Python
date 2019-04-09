import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import seaborn as sb
# %matplotlib inline
#


df = pd.read_csv('TWO_TREE_HAND.csv')
X = np.array(df.drop('target',1))
Y = np.array(df.target)
knn = KNeighborsClassifier(11)
knn.fit(X,Y)





def predict( ):
   file = open('input.txt')
   cont = 0
   contTwo =0
   contThree =0
   while True:
    line = file.readline()
    if not line:
        break


    cont = cont+1
    line = line.rstrip('\n')

    if(cont==24):
        print("_____________")

    # print(line)
    mylist = [float(x) for x in line.split(',')]



    result = knn.predict([mylist])



    if(cont<25 and result!="TWO"):
        contTwo = contTwo+1
    elif(cont>=25 and result!="TREE"):
        contThree=contThree+1


    print(result)

   file.close()
   print("Erro: " , (contTwo/24)*100 , "%")
   print("Erro: " , (contThree/24)*100 , "%")





# input("Press Enter to continue...")
predict();

