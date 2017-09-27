#Project: REST API using Eve framework
# Purpose Details: Set up a REST API using Eve and cURL contents to MongoDB
# Course: IST411
# Author: Kevin Mikus
# Date Developed: 09/26/17
# Last Date Changed: 09/26/17
# Rev: 0.1

from eve import Eve
app = Eve()

if __name__ == '__main__':
	app.run()
