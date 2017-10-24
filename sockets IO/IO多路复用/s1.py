# -*- coding: utf-8 -*-

import socket
import select

ip1 = ('127.0.0.1', 8001)
ip2 = ('127.0.0.1', 8002)
ip3 = ('127.0.0.1', 8003)

sk1 = socket.socket()
sk1.bind(ip1)
sk1.listen()

inputs = [sk1, ]

while True:
    r_list, w_list, e_list = select.select(inputs, [], inputs, 1)  # select内部自动监听sk1,sk2,sk3等对象，一旦某个句柄发生变化，写入r_list中)
    # 每当有一个用户来连接时，sk1都会发生变化，select将会监听到sk1的变化, 放入r_list中，而用户的conn对象只有在有数据传输时才会发生变化。
    print('listening obj %d' % len(inputs))
    print(r_list)
    for sk_or_conn in r_list:
        # 每有一个新的连接对象时，sk发生变化，放入r_list中
        if sk_or_conn == sk1:
            conn, ip = sk_or_conn.accept()
            inputs.append(conn)     # 把新的连接对象放入r_list中
        else:
            # 有用户发消息了
            try:
                data_bytes = sk_or_conn.recv(1024)
                data_str = str(data_bytes, encoding='utf-8')
                sk_or_conn.sendall(bytes(data_str + 'ok', encoding='utf-8'))
            except Exception as ex:
                inputs.remove(sk_or_conn)




'''
基于select实现的多路复用
inputs中放了两类数据，一类是服务器端的socket，一类是客户端的socket。相比于用socket实现的多路复用，可以实现多个人同时连接，无需等待

当c1来连接s1：
inputs中的元素为：sk1对象   							r_list中的元素：sk1对象			inputs添加的元素为：c1的conn
当c2来连接s1：
inputs中的元素为：sk1对象，c1的conn   				r_list中的元素：sk1对象 			inputs添加的元素为：c2的conn
当c3来连接s1：
inputs中的元素为：sk1对象，c1的conn, c2的conn    		r_list中的元素：sk1对象 			inputs添加的元素为：c3的conn

当c1和s1通信时：
inputs中的元素为：sk1对象，c1的conn, c2的conn, c3的conn   r_list中的元素：c1的conn（存在sk1对象?)

'''


