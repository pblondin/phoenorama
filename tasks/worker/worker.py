#!/usr/bin/env python
import pika
import time
from socket import gethostname;

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

def callback(ch, method, properties, body):
   print ' [%s] Received %r' % (gethostname(), body,)
   time.sleep( body.count('.') )
   print ' [%s] Done' % (gethostname(),)
   ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
		      queue='task_queue')

print ' [*] Waiting for messages. To exit press CTRL+C'
channel.start_consuming()

