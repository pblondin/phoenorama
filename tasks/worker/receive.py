#!/usr/bin/env python
import pika
from socket import gethostname;

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

def callback(ch, method, properties, body):
  print " [%s] Received %r" % (gethostname(), body,)

channel.basic_consume(callback,
		      queue='hello',
		      no_ack=True)

print ' [*] Waiting for messages. To exit press CTRL+C'
channel.start_consuming()

