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
    r_list, w_list, e_list = select.select(inputs, [], inputs, 1)
    print('listening obj %d' % len(inputs))
    print(r_list)
    for sk in r_list:
        if sk == sk1:
            conn, ip = sk.accept()
            inputs.append(conn)
        else:
            data_bytes = sk.recv(1024)
            data_str = str(data_bytes, encoding='utf-8')
            sk.sendall(bytes(data_str + 'ok', encoding='utf-8'))



