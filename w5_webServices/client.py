# Project: Server and Client Data Transmission using Sockets
# Purpose Details: To send a receive data using a client-server architecture using socket module in python
# Course: IST411
# Author: Kevin Mikus
# Date Developed: 09/20/17
# Last Date Changed: 09/21/17
# Rev: 0.1

import socket
try:
	clientSocket = socket.socket()
	clientSocket.connect((socket.gethostname(), 8080))
	with open("input.json", "rb") as fh:
		print("Sending...")
		data = fh.read(1024)
		while data:
			print("Sending...")
			clientSocket.send(data)
			data = fh.read(1024)
	print("Transmission complete")
	clientSocket.shutdown(socket.SHUT_RDWR)
except Exception as e:
	print(e)
