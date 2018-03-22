#!/usr/bin/env python
# -*-coding:utf-8 -*-
# 工作模式：简单队列
import pika

# ########################## 消费者 ##########################

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')  # 当队列存在时，不会重复创建，没有则创建；目的：防止生产者没有启动，队列不存在报错


def callback(ch, method, properties, body):         # 必须要自定义一个这样的回调函数，处理从队列中获取的数据
    """
    :param ch:         操作句柄
    :param method:     很少用，但要列出
    :param properties: 属性，封装了关于传递过来的数据的信息
    :param body:       队列中的内容、数据
    :return:
    """
    print(" [x] Received %r" % body)


channel.basic_consume(callback,          # 取队列中的数据，并在内部执行回调函数callback
                      queue='hello',
                      no_ack=True)       # no_ack=false消费者拿到数据后如果宕机，队列中的数据不会删除，对安全性要求很高的业务可以设置为false，意思即有应答，但效率低

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()           # 运行消费者程序，监听是否有数据，通过basic_consume去队列中取数据

