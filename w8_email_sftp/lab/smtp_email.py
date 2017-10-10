# Project: Send and receive e-mail with python
# Purpose Details: Demonstrate ability to send e-mail using smtp protocols
# Course: IST411
# Author: Kevin Mikus
# Date Developed: 2017-10-09
# Last Date Changed: 2017-10-09
# Rev: 0.1

# import necessary libraries
import smtplib
from email.mime.text import MIMEText

# setup email parameters
fromAdd = 'kzm5599@psu.edu'
toAdd = 'kzm5599@psu.edu'
subject = 'This is the subject line'
msg = MIMEText('This is the body of the email')
msg['Subject'] = subject
msg['From'] = fromAdd
msg['To'] = toAdd

# send message to smtp server
try:
	s = smtplib.SMTP_SSL('authsmtp.psu.edu', 465)
	s.sendmail(fromAdd, toAdd, msg.as_string())
except Exception as e:
	print("Error {}".format(e.args[0]))
finally:
	try:
		s.quit()
	except:
		exit()
