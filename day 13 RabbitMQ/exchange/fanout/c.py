#!/usr/bin/env python
# -*-coding:utf-8 -*-

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',       # 如果生产者还未启动，建立exchange交换机，确保exchange存在，生产者启动后，直接放入数据即可
                         exchange_type='fanout')

result = channel.queue_declare(exclusive=True)  # 消费者创建一个队列
queue_name = result.method.queue                # 随机给队列命名

channel.queue_bind(exchange='logs',             # 把队列绑定到交换机上（queue_name绑定到logs上），实际就是订阅的动作
                   queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r" % body)


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()   # 阻塞监听，等待生产者把数据放到交换机中
