#!/usr/bin/env python
# -*-coding:utf-8 -*-
# 工作模式：direct 关键字

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

severities = sys.argv[1:]
if not severities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)

for severity in severities:
    channel.queue_bind(exchange='direct_logs',
                       queue=queue_name,
                       routing_key=severity)
    # routing_key 由生产者确定的字符串，需要绑定routing_key，如果routing_key和生产者一致，则能接收到交换机中的数据，否则无法接收
    # 如果需要绑定多个routing_key，直接channel.queue_bind多个routing_key即可，exchange和queue参数都相同，可以用for循环绑定
print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
