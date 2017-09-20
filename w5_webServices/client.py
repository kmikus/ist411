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
