# -*- coding: utf-8 -*-

import socket
import select

ip1 = ('127.0.0.1', 8001)
ip2 = ('127.0.0.1', 8002)
ip3 = ('127.0.0.1', 8003)

sk1 = socket.socket()
sk1.bind(ip1)
sk1.listen()

sk2 = socket.socket()
sk2.bind(ip2)
sk2.listen()

sk3 = socket.socket()
sk3.bind(ip3)
sk3.listen()

inputs = [sk1, sk2, sk3, ]

while True:
    # [sk1, sk2, ], select内部自动监听sk1,sk2,sk3等对象，一旦某个句柄发生变化，写入r_list中
    r_list, w_list, e_list = select.select(inputs, [], [], 1)
    # r_list: 第一个位置参数的传参，发生变化的对象放到r_list中
    # w_list: 第二个位置参数列表中只要有值，就放入w_list中，没有值，则w_list为空
    # e_list: 第三个位置参数列表中出错的socket放入e_list, 并从r_list中去掉出错的对象
    # 最后一个参数1表示最多延迟1秒用于select检测，如果超时了，此次循环跳过

    for sk in r_list:
        conn, ip = sk.accept()
        conn.sendall(bytes('hello', encoding='utf-8'))
        conn.close()



    # conn, ip = sk.accept()
    # conntent_bytes = conn.recv(1024)
    # conntent_str = bytes(conntent_bytes, encoding='utf-8')
    # conn.sendall(bytes('server send content:....', encoding='utf-8'))
    #
    #
