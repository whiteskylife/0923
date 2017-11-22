#!/usr/bin/env python
# -*- coding utf-8 -*-

import socket


def handle_request(client):
    client.recv(1024)
    client.sendall(bytes('HTTP/1.1 301 OK\r\n\r\n', 'utf8'))
    client.sendall(bytes('hello, world', 'utf8'))


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
