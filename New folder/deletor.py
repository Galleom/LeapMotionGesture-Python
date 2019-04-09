import os
from random import randint


f1 = open("gestureOPEN.txt","r")
f2 = open("gestureCLOSE.txt","r")
f3 = open("gestureCOOL.txt","r")
f4 = open("gestureTHUMB.txt","r")
f5 = open("gestureTWO.txt","r")
f6 = open("gestureFOUR.txt","r")
f7 = open("gestureLOVE.txt","r")
lines1 = f1.readlines()
lines2 = f2.readlines()
lines3 = f3.readlines()
lines4 = f4.readlines()
lines5 = f5.readlines()
lines6 = f6.readlines()
lines7 = f7.readlines()
f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()
f7.close()

f1 = open("gestureOPEN.txt","w")
f2 = open("gestureCLOSE.txt","w")
f3 = open("gestureCOOL.txt","w")
f4 = open("gestureTHUMB.txt","w")
f5 = open("gestureTWO.txt","w")
f6 = open("gestureFOUR.txt","w")
f7 = open("gestureLOVE.txt","w")

porcent = 2;

for line in lines1:
  r = randint(0, porcent)
  if r != 0:
    f1.write(line)

for line in lines2:
  r = randint(0,porcent)
  if r != 0:
    f2.write(line)


for line in lines3:
  r = randint(0, porcent)
  if r != 0:
    f3.write(line)


for line in lines4:
  r = randint(0, porcent)
  if r != 0:
    f4.write(line)

for line in lines5:
  r = randint(0, porcent)
  if r != 0:
    f5.write(line)

for line in lines6:
  r = randint(0, porcent)
  if r != 0:
    f6.write(line)

for line in lines7:
  r = randint(0, porcent)
  if r != 0:
    f7.write(line)

f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()
f7.close()
