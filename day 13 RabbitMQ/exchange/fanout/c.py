#!/usr/bin/env python
# -*-coding:utf-8 -*-
#  工作模式：发布订阅
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='192.168.1.110'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',       # 如果生产者还未启动，建立exchange交换机，确保exchange存在，生产者启动后，直接放入数据即可
                         exchange_type='fanout')

result = channel.queue_declare(exclusive=True)  # 消费者创建一个队列 ,once the consumer connection is closed, the queue should be deleted. There's an exclusive flag for that
queue_name = result.method.queue                # 随机给队列命名 For example it may look like amq.gen-JzTY20BRgKO-HjmUJj0wLg

channel.queue_bind(exchange='logs',             # 把队列绑定到发布者或订阅者创建的交换机上（queue_name绑定到logs上），实际就是订阅的动作
                   queue=queue_name)            # 将队列名称与路由器绑定

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r" % body)


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()   # 阻塞监听，等待生产者把数据放到交换机中
