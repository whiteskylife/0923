#!/usr/bin/env python
# -*-coding:utf-8 -*-

import pika

# ######################### 生产者 #########################

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))                               # 封装了socket逻辑部分，不需要自己写socket

channel = connection.channel()                      # 拿到操作rabbitmq的句柄

channel.queue_declare(queue='hello')                # 在RabbitMQ中创建队列并命名

channel.basic_publish(exchange='',                  # exchange交换机，提供路由功能，简单（单一）队列不需要，多个队列场景会用到
                      routing_key='hello',          # 把数据body='Hello World!'放到名字为hello的队列中
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()
