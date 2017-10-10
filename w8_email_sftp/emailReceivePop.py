# Project: Send and receive e-mail with python
# Purpose Details: Demonstrate ability to send e-mail using smtp protocols
# Course: IST411
# Author: Kevin Mikus
# Date Developed: 2017-10-09
# Last Date Changed: 2017-10-09
# Rev: 0.1

import getpass, poplib

try:
	# create pob object with connection to server
	m = poplib.POP3_SSL('mail.psu.edu')
	# send username
	m.user('kzm5599')
	# prompt for password
	m.pass_(getpass.getpass())
	# get num of messages
	print(m.stat())
	# get all messages
	numMessages = m.stat()[0]
	for i in range(numMessages):
		for j in m.retr(i+1)[1]:
			print(j)

	# retrieve messages by id
	m.retr(1)
except Exception as e:
	print("Error {}".format(e.args[0]))
finally:
	# m will not be definied if exception is caught
	try: m.quit()
	except: exit()
