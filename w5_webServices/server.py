import socket
try:
	serverSocket = socket.socket()
	print("Create an INET, STREAMING socket")
	serverSocket.bind((socket.gethostname(), 8080))
	print("Bind the socket to public host, and a well-known port 8080")
	serverSocket.listen(5)
	print("Become a server socket")
	with open("output.json", "wb") as fh:
		while True:
			print("Accepts connections from outside")
			clientSocket, address = serverSocket.accept()
			print("Received connection from {}".format(address))
			data = clientSocket.recv(1024)
			while data:
				print("Receiving data...")
				fh.write(data)
				data = clientSocket.recv(1024)
			print("Done receiving")
except Exception as e:
	print(e)
