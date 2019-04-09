###  AUTHOR:IVO STINGHEN ( gamefico@gmail.com)
### Read model from disk and run a RealTime Communication with unity

import numpy as np
import pandas as pd
import time,os
import socket
import pickle

host,port = "localhost" , 10000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

############# LOAD MODEL  ##############
classifier = pickle.load(open('model.sav', 'rb'))
#classifier = pickle.load(open('save.pkcls', 'rb'))
print("model loaded!")
#########################################################



try:
    sock.connect((host,port))
    print("sock connected!")
    while (1):
       
        #recebe input
        inputReceived = sock.recv(1024).decode("utf-8")
        line = inputReceived
        line = line.rstrip('\n')
        mylist = [float(x) for x in line.split(',')]

        #envia resultado
        result = classifier.predict([mylist])
        result = result[0]
        sock.sendall(result.encode("utf-8"))
 
        # print(result)
        time.sleep(.02)


finally:
    sock.close()
