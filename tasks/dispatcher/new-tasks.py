#!/usr/bin/env python
import pika
import sys
from socket import gethostname;

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare queue 
channel.queue_declare(queue='task_queue', durable=True)

# Message to send
message = ' '.join(sys.argv[1:]) or 'Hello World!'

# Exchanging the task
channel.basic_publish(exchange='',
		      routing_key='task_queue',
	  	      body=message,
		      properties=pika.BasicProperties(
			 delivery_mode = 2, # make message persistent
		      ))

print ' [%s] Sent %r' % (gethostname(), message,)

# Close connection
connection.close()
