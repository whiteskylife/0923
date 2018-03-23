#!/usr/bin/env python
# -*-coding:utf-8 -*-

#  工作模式：发布订阅
#  注意：exchange可以由生产者创建也可由消费者创建，队列由消费者创建，然后在消费者端把交换机和队列进行绑定，
#       此后生产者发布消息，订阅者（绑定了交换机的消费者，可以存在多个订阅者）绑定了交换机都能收到数据


import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='192.168.1.110'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',         # 创建一个交换机并命名（消费者通过名字来绑定队列），把信息放入交换机，（注意：生产者无需创建队列，只需创建一个交换机，把信息放入即可）
                         exchange_type='fanout')    # #订阅发布模式 ，由路由器名称logs来选择队列分发消息

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs',          # 指定交换机名字，放到哪个交换机里面
                      routing_key='',           # 有了交换机，不再需要简单队列中指定队列名字的参数routing_key,设置为空
                      body=message)             # body里面的信息不再放到队列，而是放到交换机中

print(" [x] Sent %r" % message)
connection.close()

