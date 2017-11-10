#!/usr/bin/evn python

# Project: RabbitMQ Demonstration
# Purpose Details: Use RabbitMQ to send/receive messages from a queue
# Course: IST411
# Author: Kevin Mikus
# Date Developed: 2017-11-10
# Last Date Changed: 2017-11-10
# Rev: 0.1

import pika, json

try:
	# setup json
	fh = open("payloadMikus.json", "r")
	json_data = json.loads(fh.read())
	payload = json.dumps(json_data)

	# connecting
	print("Connecting to Localhost Queue")
	connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
	channel = connection.channel()

	# sending
	channel.queue_declare(queue="hello")
	channel.basic_publish(exchange="", routing_key="hello", body=payload)
	print(" [x] Sent json data")

	connection.close()
except Exception as e:
	print(e)
