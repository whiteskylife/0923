#!/usr/bin/env python
# -*-coding:utf-8 -*-
# 工作模式：direct 关键字， 相当于fanout模式多加了个条件：routing_key，如果消费者绑定的routing_key值和生产者一致，才能取到信息
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,             # routing_key 生产者定义一个字符串，消费者绑定路由时，
                      body=message)
print(" [x] Sent %r:%r" % (severity, message))
connection.close()


