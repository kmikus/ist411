#!/usr/bin/env python

# Project: RabbitMQ Demonstration
# Purpose Details: Use RabbitMQ to send/receive messages from a queue
# Course: IST411
# Author: Kevin Mikus
# Date Developed: 2017-11-10
# Last Date Changed: 2017-11-10
# Rev: 0.1

import pika

try:
	connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
	channel = connection.channel()

	channel.queue_declare(queue="hello")

	def callback(ch, method, properties, body):
		print(" [x] Received %r" % body)

	channel.basic_consume(callback, queue="hello", no_ack=True)

	print(" [*] Waiting for messages. To exit press CTRL+C")
	channel.start_consuming()
except Exception as e:
	print(e)
