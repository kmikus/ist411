import sys, datetime
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
print("Connected to MongoDb")
db = client.test_database
print("Got the database: test_database")
collection = db.test_collection
print("Got the collection")
post = {"author": "Mike", "text": "My first blog post!", "tags": ["mongodb", "python", "pymongo"], "date": datetime.datetime.utcnow()}
print("Created the document object")
post_id = collection.insert_one(post).inserted_id
print("Post id: ", post_id)
client.close()

