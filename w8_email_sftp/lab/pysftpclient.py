# Project: Send and receive e-mail with python
# Purpose Details: Demonstrate ability to send e-mail using smtp protocols
# Course: IST411
# Author: Kevin Mikus
# Date Developed: 2017-10-09
# Last Date Changed: 2017-10-09
# Rev: 0.1

import pysftp, sys
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
# Windows Subsystem for Linux has trouble resolving using DNS, using IP address instead
cinfo = {'cnopts':cnopts,'host':'128.118.251.244','username':'ftpuser','password':'test1234','port': 101}

try:
	with pysftp.Connection(**cinfo) as sftp:
		print("Connection successful")
		try:
			r = ""
			while(r != "x"):
				r = input("parameters = [list | get | put]: ")
				if (r == "get"):
					sftp.get('payloadReceiveMikus.json')
					print("Received payload")
				elif (r == "list"):
					for file in (sftp.listdir(remotepath='/home/ftpuser/')):
						print(file)
				elif (r == "put"): 
					sftp.put('payloadSendMikus.json', remotepath='/home/ftpuser/payloadSendMikus.json')
					print("Sent payload")
				else:
					print("Invalid command, try again")
				r = input("Press any key to continue or x to exit: ")
		except:
			print("Log exception 1: ", sys.exc_info())
except:
	print("Log exception 2: ", sys.exc_info()[0])
