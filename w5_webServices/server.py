import socket
try:
	serverSocket = socket.socket()
	print("Create an INET, STREAMING socket")
	serverSocket.bind((socket.gethostname(), 8080))
	print("Bind the socket to public host, and a well-known port 8080")
	serverSocket.listen(5)
	print("Become a server socket")
	while True:
		print("Accepts connections from outside")
		(clientSocket, address) = serverSocket.accept()
		# PRINT CLIENT SIDE CODE HERE
except Exception as e:
	print(e)
