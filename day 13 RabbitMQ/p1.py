#!/usr/bin/env python
# -*-coding:utf-8 -*-
# 工作模式：简单队列
import pika
import sys

# ######################### 生产者 #########################

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='192.168.1.110'))                   # 封装了socket逻辑部分，不需要自己写socket
channel = connection.channel()           # 拿到操作rabbitmq的句柄

channel.queue_declare(queue='hello')     # 在RabbitMQ中创建队列并命名

message = ' '.join(sys.argv[1:]) or "Hello World!"
print(message)

channel.basic_publish(exchange='',          # exchange交换机，提供路由功能，简单（单一）队列不需要，多个队列场景会用到
                      routing_key='hello',  # 把数据body='Hello World!'放到名字为hello的队列中,没有用到exchange交换机，需要指定队列名即：routing_key
                      body=message)

# print(" [x] Sent 'Hello World!'")
print(" [x] Sent %r" % message)
connection.close()
