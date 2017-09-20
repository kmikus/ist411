# Project: Mongo, JSON, and cURL integration using PyMongo
# Purpose Details: Retreive a JSON file from the web and write its key-value pairs to MongoDB
# Course: IST411
# Author: Kevin Mikus
# Date Developed: 9/12/17
# Last Date Changed: 9/12/17
# Rev: 0.1

import sys, urllib.parse, urllib.request, json
from pymongo import MongoClient

try:
	# use urllib to grab json
	url = "https://jsonplaceholder.typicode.com/posts/1/comments"
	urlHandle = urllib.parse.urlparse(url)
	response = urllib.request.urlopen(urlHandle.geturl())
	encoding = response.info().get_content_charset("utf-8")
	payload = response.read().decode(encoding)
	jsonStream = json.loads(payload)
except:
	e = sys.exc_info()[0]
	print("error: {}".format(e))

# use pymongo to write json to mongodb on localhost
client = MongoClient()
db = client.module4
collection = db.payload

for element in jsonStream:
	collection.insert_one(element)
	print("Inserted elementID: ", element["id"])

client.close()

