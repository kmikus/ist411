import socket
try:
	clientSocket = socket.socket()
	clientSocket.connect((socket.gethostname(), 8080))
	clientSocket.sendall(bytes("This is a message"))	
except Exception as e:
	print(e)
