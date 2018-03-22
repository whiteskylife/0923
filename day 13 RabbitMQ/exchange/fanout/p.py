#!/usr/bin/env python
# -*-coding:utf-8 -*-

#  工作模式：发布订阅
#  注意：exchange可以由生产者创建也可由消费者创建，队列由消费者创建，然后在消费者端把交换机和队列进行绑定，
#       此后生产者发布消息，订阅者（绑定了交换机的消费者，可以存在多个订阅者）就能收到数据


import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',               # 创建一个交换机，把信息放入交换机，（注意：生产者无需创建队列，只需创建一个交换机，把信息放入即可）
                         exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs',          # 指定交换机名字，放到哪个交换机里面
                      routing_key='',           # 有了交换机，不再需要简单队列中的routing_key,设置为空
                      body=message)
print(" [x] Sent %r" % message)
connection.close()

