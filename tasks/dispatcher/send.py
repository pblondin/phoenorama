#!/usr/bin/env python
import pika
from socket import gethostname;

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare queue 
channel.queue_declare(queue='hello')

# Exchanging the message
channel.basic_publish(exchange='', 
		      routing_key='hello', 
		      body='Hello World!')

print " [%s] Sent 'Hello World!'" % (gethostname(),)

# Close connection
connection.close()
