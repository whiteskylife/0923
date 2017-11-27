#!/usr/bin/env python
# -*- coding utf-8 -*-

import socket
import abc
# http://www.cnblogs.com/yuanchenqi/articles/5603871.html


def handle_request(client):
    client.recv(1024)
    client.sendall(bytes('HTTP/1.1 301 OK\r\n\r\n', 'utf8'))
    f = open("abc")
    data = f.read()
    f.close()
    client.sendall(bytes(data, 'utf8'))


def main():
    sock = socket.socket()
    sock.bind(('127.0.0.1', 8082))
    sock.listen(5)

    while True:
        conn, ip = sock.accept()
        handle_request(conn)
        conn.close()

if __name__ == '__main__':
    main()


