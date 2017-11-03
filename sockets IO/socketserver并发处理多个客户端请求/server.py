# -*- coding: utf-8 -*-

import socketserver
'''
socket只能同时处理一个请求
import socket

obj = socket.socket()
ip_port = ('127.0.0.1', 9999)
obj.bind(ip_port)
obj.listen(5)

while True:
    conn, ip = obj.accept()
    while True:
        ret = str(conn.recv(1024), encoding='utf-8')
        if ret == 'q':
            break
        conn.sendall(bytes(ret + 'server reply...', encoding='utf-8'))
'''


class MyServer(socketserver.BaseRequestHandler):

    def handle(self):        # 必须叫这个方法名称，ThreadingTCPServer内写死了要调这个方法
        # self 封装了属性如下，可以生成多个服务端响应请求
        # self.request(客户端请求), self.client_address（客户端地址）,self.servers（服务器对象）
        conn = self.request
        conn.sendall(bytes('welcome login whiskys python world', encoding='utf-8'))
        while True:
            ret_bytes = conn.recv(1024)
            ret_str = str(ret_bytes, encoding='utf-8')
            if ret_str == 'q':
                break
            conn.sendall(bytes(ret_str + 'OK', encoding='utf-8'))


if __name__ == '__main__':

    """
    server对象封装了：
            self.server_address ==> ('127.0.0.1', 9999)
            self.RequestHandlerClass ==> MyServer
            self.socket             ==>  创建服务器端的socket对象
    """

    server = socketserver.ThreadingTCPServer(('127.0.0.1', 9999), MyServer)
    server.
    server.serve_forever()

# 类的参数，初始化 __init__ 只能通过传值？ 其他方式?

"""
class ThreadingMixIn:
    def process_request_thread(self, request, client_address):
        try:
            self.finish_request(request, client_address)
            self.shutdown_request(request)
        except:
            self.handle_error(request, client_address)
            self.shutdown_request(request)

    def process_request(self, request, client_address):
        t = threading.Thread(target = self.process_request_thread,
                             args = (request, client_address))
        t.daemon = self.daemon_threads
        t.start()





class TCPServer(BaseServer):
	def __init__(self, server_address, RequestHandlerClass, bind_and_activate=True):
	BaseServer.__init__(self, server_address, RequestHandlerClass)
	self.socket = socket.socket(self.address_family,
								self.socket_type)
	if bind_and_activate:
		try:
			self.server_bind()
			self.server_activate()
		except:
			self.server_close()
			raise

    def get_request(self):
        return self.socket.accept()

    def server_bind(self):
        if self.allow_reuse_address:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.server_address)
        self.server_address = self.socket.getsockname()

    def server_activate(self):
        self.socket.listen(self.request_queue_size)

    def server_close(self):
        self.socket.close()

    def shutdown_request(self, request):
        """Called to shutdown and close an individual request."""
        try:
            #explicitly shutdown.  socket.close() merely releases
            #the socket and waits for GC to perform the actual close.
            request.shutdown(socket.SHUT_WR)
        except OSError:
            pass #some platforms may raise ENOTCONN here
        self.close_request(request)

    def close_request(self, request):
        """Called to clean up an individual request."""
        request.close()




class BaseServer:

    def __init__(self, server_address, RequestHandlerClass):
        self.server_address = server_address
        self.RequestHandlerClass = RequestHandlerClass
        self.__is_shut_down = threading.Event()
        self.__shutdown_request = False

    def server_activate(self):
		pass


    def serve_forever(self, poll_interval=0.5):
        self.__is_shut_down.clear()
        try:
            with _ServerSelector() as selector:
                selector.register(self, selectors.EVENT_READ)

                while not self.__shutdown_request:
                    ready = selector.select(poll_interval)
                    if ready:
                        self._handle_request_noblock()

                    self.service_actions()
        finally:
            self.__shutdown_request = False
            self.__is_shut_down.set()


    def shutdown(self):
        self.__shutdown_request = True
        self.__is_shut_down.wait()


    def _handle_request_noblock(self):
        try:
            request, client_address = self.get_request()
        except OSError:
            return
        if self.verify_request(request, client_address):
            try:
                self.process_request(request, client_address)
            except:
                self.handle_error(request, client_address)
                self.shutdown_request(request)

    def process_request(self, request, client_address):
        """Call finish_request.

        Overridden by ForkingMixIn and ThreadingMixIn.

        """
        self.finish_request(request, client_address)
        self.shutdown_request(request)

    def finish_request(self, request, client_address):
        """Finish one request by instantiating RequestHandlerClass."""
        self.RequestHandlerClass(request, client_address, self)

    def shutdown_request(self, request):
        """Called to shutdown and close an individual request."""
        self.close_request(request)


class ThreadingTCPServer(ThreadingMixIn, TCPServer): pass



import socketserver

class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        conn = self.request
        conn.sendall(bytes('welcome login whiskys python world', encoding='utf-8'))
        while True:
            ret_bytes = conn.recv(1024)
            ret_str = str(ret_bytes, encoding='utf-8')
            if ret_str == 'q':
                break
            conn.sendall(bytes(ret_str + 'OK', encoding='utf-8'))


if __name__ == '__main__':

    server = socketserver.ThreadingTCPServer(('127.0.0.1', 9999), MyServer)
    server.serve_forever()

"""