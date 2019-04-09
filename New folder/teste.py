import socket 
import time
host,port = "127.0.0.1" , 10000


data = "1,5,2"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:

	sock.connect((host,port))
	
	while True:
		sock.sendall(data.encode("utf-8"))
		out = sock.recv(1024).decode("utf-8")
		print(out+"\n")
		time.sleep(.02)

finally:
	sock.close()