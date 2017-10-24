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
outputs = []
message_dict = {}

while True:
    '''
    读信息和写信息分离
    '''
    r_list, w_list, e_list = select.select(inputs, outputs, inputs, 1)  # select内部自动监听sk1,sk2,sk3等对象，一旦某个句柄发生变化，写入r_list中)
    # 每当有一个用户来连接时，sk1都会发生变化，select将会监听到sk1的变化, 放入r_list中，而用户的conn对象只有在有数据传输时才会发生变化。
    print('listening obj %d' % len(inputs))
    print(r_list)
    for sk_or_conn in r_list:           # r_list 用于读取信息
        # 每有一个新的连接对象时，sk发生变化，放入r_list中
        if sk_or_conn == sk1:
            conn, ip = sk_or_conn.accept()
            inputs.append(conn)     # 把新的连接对象放入r_list中
            message_dict[conn] = []
        else:
            # 有老用户发消息了
            try:
                data_bytes = sk_or_conn.recv(1024)
            except Exception as ex:
                # 如果用户终止连接
                print(ex)
                inputs.remove(sk_or_conn)
            else:
                # 用户正常发送消息
                data_str = str(data_bytes, encoding='utf-8')
                # sk_or_conn.sendall(bytes(data_str + 'ok', encoding='utf-8'))
                message_dict[sk_or_conn].append(data_str)
                outputs.append(sk_or_conn)

    for conn in w_list:                 # w_list 保存了谁给我发过信息，用于回复信息
        # conn.sendall(bytes('hello', encoding='utf-8'))
        # outputs.remove(conn)
        recv_str = message_dict[conn][0]
        del message_dict[conn][0]
        conn.sendall(bytes(recv_str + 'good', encoding='utf-8'))
        outputs.remove(conn)

    for sk in e_list:
        inputs.remove(sk)


# 小结： IO多路复用的实现，通过select监听多个文件描述符来实现一个伪并发。