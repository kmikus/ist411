# Project: HMAC demonstration
# Purpose Details: Use HMAC to verify integrity of payload message
# Course: IST411
# Author: Kevin Mikus
# Date Developed: 2017-10-20
# Last Date Changed: 2017-10-20
# Rev: 0.1

import pysftp, sys, json

# setting up connection ftp server
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
# Windows Subsystem for Linux has trouble resolving using DNS, using IP address instead
cinfo = {'cnopts':cnopts,'host':'128.118.251.244','username':'ftpuser','password':'test1234','port': 101}

# creating json payload
payload_dict = {'message': 'I am a message'}
md5_sig = hmac.new(payload_dict['message'].encode(), digestmod='md5').hexdigest()
sha1_sig = hmac.new(payload_dict['message'].encode(), digestmod='sha1').hexdigest()
payload_dict['md5'], payload_dict['sha1'] = md5_sig, sha1_sig
with open('hmac_payload_mikus.json', 'w') as outFile:
	outFile.write(json.dumps(payload_dict, indent=4))

# establish connection
try:
	with pysftp.Connection(**cinfo) as sftp:
		print("Connection successful")
		try:
			r = ""
			while(r != "x"):
				r = input("parameters = [get | put | list]: ")
				if (r == "get"):
					sftp.get('hmac_payload_mikus.json')
					print("Received payload")
				elif (r == "put"):
					sftp.put('hmac_payload_mikus.json', remotepath='/home/ftpuser/hmac_payload_mikus.json')
					print("Sent payload")
				elif (r == "list"):
					for file in (sftp.listdir(remotepath='home/ftpuser/')):
						print(file)
				else:
					print("Invalid command, try again")
				r = input("Press any key to continue or x to exit: ")
		except:
			print("Log exception 1: ", sys.exc_info())
except:
	print("Log exception 2: ", sys.exc_info()[0])
