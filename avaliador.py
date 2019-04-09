import pandas as pd
import numpy as np
import os
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
# from sklearn.datasets import make_classification
import sys

from sklearn import tree
from sklearn import svm
from numpy import * 
# import numpy as np


import pickle
training_percentage = 0.3 # float entre 0 e 1
bestResult= [0,0,0,0,0,0,0,0,0,0]


n = 10
m = 10
confusionMatrix = [0] * n
for i in range(n):
	for j in range(n):
		confusionMatrix[i] = [0.0] * m


winner = 0 
# pegar input
df = pd.read_csv(r"gestures\gesture.csv")
# pegar tamanho de t e f
# T se refere a "Teste"
# F se refere a "Fim" (por é o fim)
t_rows = int(round(df.shape[0]*training_percentage))
f_rows = df.shape[0] - t_rows

# Randomizar entrada
D = df.sample(frac=1,random_state=2).reset_index(drop=True);

# Pegar primeiros para treinamento
DT = D.iloc[:t_rows]
XT = np.array(DT.drop('target',1))
YT = np.array(DT.target)
# XT.tofile("TESTE", format="%s")
# __________________DECISION TREE_______________________

# Fazer treinamento de acordo com algoritmo

classifiers = {} 

# classifierNames = ["KNN(3)","KNN(5)","KNN(7)","TREE(2)","TREE(3)","TREE(5)","TREE(7)","TREE(2)","TREE(3)","TREE(5)","TREE(7)","SVM(1)","SVM(2)","SVM(3)","SVM(1)","SVM(2)","SVM(3)"];
classifierNames = ["KNN(3)","KNN(5)","SVM(3)","SVM(5)","SVM(7)","TREE(2)","TREE(3)","TREE(5)"];

classifiers[0] = KNeighborsClassifier(3)
classifiers[1] = KNeighborsClassifier(5)
# classifiers[2] = KNeighborsClassifier(7
classifiers[2] = svm.SVC(degree=3)
classifiers[3] = svm.SVC(degree=5)
classifiers[4] = svm.SVC(degree=7)
classifiers[5] = tree.DecisionTreeClassifier(min_samples_split=2,splitter="best")
classifiers[6] = tree.DecisionTreeClassifier(min_samples_split=3,splitter="best")
classifiers[7] = tree.DecisionTreeClassifier(min_samples_split=5,splitter="best")
# classifiers[6] = tree.DecisionTreeClassifier(min_samples_split=7,splitter="best")
# classifiers[7] = tree.DecisionTreeClassifier(min_samples_split=2,splitter="random")
# classifiers[8] = tree.DecisionTreeClassifier(min_samples_split=3,splitter="random")
# classifiers[9] = tree.DecisionTreeClassifier(min_samples_split=5,splitter="random")
# classifiers[10] = tree.DecisionTreeClassifier(min_samples_split=7,splitter="random")

# classifiers[14] = svm.SVC(kernel='poly' , degree=1)
# classifiers[15] = svm.SVC(kernel='poly' , degree=2)
# classifiers[16] = svm.SVC(kernel='poly' , degree=3)#default


for c in classifiers:

	classifiers[c].fit(XT,YT)

	# Pegar últimos % para testes
	D2 = D.iloc[-f_rows:]
	XF = np.array((D2).drop('target',1))
	YF = np.array(D2[D2.columns[-1]])


	print("\nClassifier:"+classifierNames[c] )
	textfile = open('RESULTADOS.txt', 'a')
	textfile.write('\n' +classifierNames[c])

	acertos = [0,0,0,0,0,0,0,0,0,0]
	erros   = [0,0,0,0,0,0,0,0,0,0]
	total   = [0,0,0,0,0,0,0,0,0,0]
	temp = 0 

	for i in range(0, f_rows) :
		result = classifiers[c].predict([XF[i]]);
		if YF[i] == "OPEN":
			temp=0
		elif YF[i] ==  "CLOSE":
			temp=1
		elif YF[i] ==  "THUMB":
			temp=2
		elif YF[i] == "TWO":
			temp=3
		elif YF[i] == "THREE":
			temp=4
		elif YF[i] ==  "FOUR":
			temp=5
		elif YF[i] ==  "LOVE":
			temp=6
		elif YF[i] ==  "COOL":
			temp=7
		elif YF[i] ==  "FIRE":
			temp=8
		elif YF[i] ==  "HANG_LOOSE":
			temp=9

		total[temp] +=1;
		index =0
		if (result == YF[i]):
			acertos[temp] += 1
		
		# CONFUSION MATRIX
		if result == "OPEN":
			index=0
		elif result ==  "CLOSE":
			index=1
		elif result ==  "THUMB":
			index=2
		elif result == "TWO":
			index=3
		elif result == "THREE":
			index=4
		elif result ==  "FOUR":
			index=5
		elif result ==  "LOVE":
			index=6
		elif result ==  "COOL":
			index=7
		elif result ==  "FIRE":
			index=8
		elif result ==  "HANG_LOOSE":
			index=9
		confusionMatrix[temp][index] += 1.0


	
	print("confusionMatrix")
	print(confusionMatrix)
	resultArray = []
	for x in range(0,10): 
		result = round((100*(acertos[x]/total[x])),2)
		resultArray.append(result) 

	for u in range (0,10):
		for v in range (0,10):
			confusionMatrix[u][v] = round(100* (confusionMatrix[u][v]/total[v]),2)
	

	print('\n',confusionMatrix)


	textfile = open('RESULTADOS.txt', 'a')
	textfile.write('\n confusionMatrix')
	textfile.write(str(confusionMatrix))



	pointA=0
	pointB=0
	for x in range(0,10):
		if(resultArray[x]>bestResult[x]):
			pointA+=1
		else:
			pointB+=1
	if(pointA>pointB):
		bestResult = resultArray[:]
		winner = c
			



	textfile = open('RESULTADOS.txt', 'a')
	textfile.write('\n')
	for z in range(0,10):
		textfile.write(str(resultArray[z]) +'\t')
		# sys.stdout.write(str(resultArray[z]) +'\t')
		# print(resultArray[z],'\t', end='')
	textfile.write('\n')
	textfile.close()

	for u in range (0,10):
		for v in range (0,10):
			confusionMatrix[u][v] = 0

print('\n',bestResult , '\n' ,winner, classifierNames[winner])