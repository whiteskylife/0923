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





