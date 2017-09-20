import sys, datetime
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.test_database
collection = db.test_collection
doc= collection.find()
for post in doc:
	print(post)
client.close()

