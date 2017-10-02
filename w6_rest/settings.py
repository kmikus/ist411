# Project: REST API using Eve framework
# Purpose Details: Set up a REST API using Eve and cURL contents to MongoDB
# Course: IST411
# Author: Kevin Mikus
# Date Developed: 09/26/17
# Last Date Changed: 09/28/17
# Rev: 0.2

MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME = 'apitest'

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

schema = {
	'firstname': {
		'type': 'string',
		'minlength': 1,
		'maxlength': 10,
	},
	'lastname': {
		'type': 'string',
		'minlength': 1,
		'maxlength': 15,
		'required': True,
		'unique': True,
	},
	'role': {
		'type': 'list',
		'allowed': ['author', 'contributor', 'copy'],
	},
	'location': {
		'type': 'dict',
		'schema': {
			'address': {'type': 'string'},
			'city': {'type': 'string'},
		},
	},
	'born': {
		'type': 'datetime',
	},
}

people = {
	'item_title': 'person',
	'additional_lookup': {
		'url': 'regex("[\w]+")',
		'field': 'lastname',
	},
	'cache_control': 'max-age=10,must-revalidate',
	'cache_expires': 10,
	'resource_methods': ['GET', 'POST', 'DELETE'],

	'schema': schema
}

DOMAIN = {
	'people': people,
}
