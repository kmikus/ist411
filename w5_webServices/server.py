# Project: Server and Client Data Transmission using Sockets
# Purpose Details: To send a receive data using a client-server architecture using socket module in python
# Course: IST411
# Author: Kevin Mikus
# Date Developed: 09/20/17
# Last Date Changed: 09/21/17
# Rev: 0.1

import socket
try:
	serverSocket = socket.socket()
	print("Create an INET, STREAMING socket")
	serverSocket.bind((socket.gethostname(), 8080))
	print("Bind the socket to public host, and a well-known port 8080")
	serverSocket.listen(5)
	print("Become a server socket")
	while True:
		with open("output.json", "wb+") as fh:
			while True:
				print("Accepting connections from outside...")
				clientSocket, address = serverSocket.accept()
				print("Received connection from {}".format(address))
				data = clientSocket.recv(1024)
				while data:
					print("Receiving data...")
					fh.write(data)
					data = clientSocket.recv(1024)
				print("Done receiving")
				break
		with open("output.json", "r") as fh:
			print(fh.read())
		answer = input("Use x to exit, any key to keep listening: ")
		if answer == "x":
			exit()
except Exception as e:
	print(e)
