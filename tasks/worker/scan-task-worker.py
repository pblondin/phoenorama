#!/usr/bin/env python
import pika
import shlex, subprocess, threading, time
from socket import gethostname;

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

def execTask(body):
   task, host = body.split(':')
   cmd = shlex.split(task + ' ' +  host)
   print "Thread started"
   retcode = subprocess.call(cmd)
   print "Thread finished with retcode: %s" % (str(retcode))

def callback(ch, method, properties, body):
   print ' [%s] Received %r' % (gethostname(), body,)
   execTask(body) 
   print ' [%s] Done' % (gethostname(),)
   ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
		      queue='task_queue')

print ' [*] Waiting for messages. To exit press CTRL+C'
channel.start_consuming()

