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
	print(m.list())
	# show greeting from pop3 server
	print(m.getwelcome())
	# get mailbox status tuple of 2 ints, message count and mailbox size
	print(m.stat())
except Exception as e:
	print("Error {}".format(e.args[0]))
finally:
	# m will not be definied if exception is caught
	try: m.quit()
	except: exit()
