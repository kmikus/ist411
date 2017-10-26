# Project: HMAC demonstration
# Purpose Details: Use HMAC to verify integrity of payload message
# Course: IST411
# Author: Kevin Mikus
# Date Developed: 2017-10-20
# Last Date Changed: 2017-10-20
# Rev: 0.1

import pysftp, sys, json, hmac, os

# setting up connection ftp server
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
# Windows Subsystem for Linux has trouble resolving using DNS, using IP address instead
cinfo = {'cnopts':cnopts,'host':'oz-ist-linux-fa17-411','username':'ftpuser','password':'test1234','port': 101}

# creating json payload
payload_dict = {'message': 'I am a message'}
md5_sig = hmac.new(payload_dict['message'].encode(), digestmod='md5').hexdigest()
sha1_sig = hmac.new(payload_dict['message'].encode(), digestmod='sha1').hexdigest()
payload_dict['md5'], payload_dict['sha1'] = md5_sig, sha1_sig
with open('payload_mikus_hmac.json', 'w') as outFile:
	outFile.write(json.dumps(payload_dict, indent=4))

# Modified to show signature before and after
print("MD5 digest: ", md5_sig)
print("SHA1 digest: ", sha1_sig)

# establish connection
try:
	with pysftp.Connection(**cinfo) as sftp:
		print("Connection successful")
		try:
			r = ""
			while(r != "x"):
				r = input("parameters = [get | put | list]: ")
				if (r == "get"):
					sftp.get('payload_mikus_hmac.json')
					with open('payload_mikus_hmac.json', 'r') as fh:
						decoded_json = json.load(fh)
						message = decoded_json['message']
						md5_rec, sha1_rec = decoded_json['md5'], decoded_json['sha1']
						print("MD5 digest received: ", md5_rec)
						print("SHA1 digest received: ", sha1_rec)
						if(md5_sig == md5_rec and sha1_sig == sha1_rec):
							print('Message verified')
							print("Received payload")
							print('Message: ', message)
						else:
							os.remove('payload_mikus_hmac.json')
							print('Invalid signature, file removed, exiting')
							break
				elif (r == "put"):
					sftp.put('payload_mikus_hmac.json', remotepath='/home/ftpuser/payload_mikus_hmac.json')
					print("Sent payload")
				elif (r == "list"):
					for file in (sftp.listdir(remotepath='/home/ftpuser/')):
						print(file)
				else:
					print("Invalid command, try again")
				r = input("Press any key to continue or x to exit: ")
		except:
			print("Log exception 1: ", sys.exc_info())
except:
	print("Log exception 2: ", sys.exc_info()[0])
