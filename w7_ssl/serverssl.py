# Project: Using an SSL Certificate for security
# Purpose Details: Demonstrate client-server connection with security via an SSL Certificate
# Course: IST411
# Author: Kevin Mikus
# Date Developed: 10/02/17
# Last Date Changed: 10/02/17
# Rev: 0.1

import socket, ssl
try:
	serverSocket = socket.socket()
	sslSock = ssl.wrap_socket(serverSocket,
		server_side=True,
		certfile="server.crt",
		keyfile="server.key")
	print("Create an INET, STREAMING socket")
	sslSock.bind((socket.gethostname(), 8080))
	print("Bind the socket to public host, and a well-known port 8080")
	sslSock.listen(5)
	print("Become a server socket")
	while True:
		with open("output.json", "wb+") as fh:
			print("Accepting connections from outside...")
			clientSocket, address = sslSock.accept()
			print("Received connection from {}".format(address))
			data = clientSocket.recv(1024)
			while data:
				print("Receiving data...")
				fh.write(data)
				data = clientSocket.recv(1024)
			print("Done receiving")
		with open("output.json", "r") as fh:
			print(fh.read())
		answer = input("Use x to exit, any key to keep listening: ")
		if answer == "x":
			exit()
except Exception as e:
	print(e)
