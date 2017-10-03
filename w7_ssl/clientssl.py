# Project: Using an SSL Certificate for security
# Purpose Details: Demonstrate client-server connection with security via an SSL Certificate
# Course: IST411
# Author: Kevin Mikus
# Date Developed: 10/02/17
# Last Date Changed: 10/02/17
# Rev: 0.1

import socket, ssl
try:
	clientSocket = socket.socket()
	sslSock = ssl.wrap_socket(clientSocket,
		ca_certs="server.crt",
		cert_reqs=ssl.CERT_REQUIRED)
	sslSock.connect((socket.gethostname(), 8080))
	with open("input.json", "rb") as fh:
		print("Sending...")
		data = fh.read(1024)
		while data:
			print("Sending...")
			sslSock.send(data)
			data = fh.read(1024)
	print("Transmission complete")
	sslSock.shutdown(socket.SHUT_RDWR)
except Exception as e:
	print(e)
