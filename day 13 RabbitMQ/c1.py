#!/usr/bin/env python
# -*-coding:utf-8 -*-

import pika

# ########################## 消费者 ##########################

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')  # 当队列存在时，不会重复创建，没有则创建；目的：防止队列不存在报错


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_qos(prefetch_count=1)


channel.basic_consume(callback,          # 取队列中的数据执行回调函数callback
                      queue='hello',
                      no_ack=True)       # no_ack=false消费者拿到数据后如果宕机，队列中的数据不会删除，对安全性要求很高的业务可以设置为false，意思即有应答，但效率低

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

