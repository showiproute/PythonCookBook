#!/usr/bin/env python
#coding:utf-8

from socket import socket,AF_INET,SOCK_STREAM

class LazyConnection(object):
    def __init__(self,address,familty=AF_INET,type=SOCK_STREAM):
        self.address=address
        self.family=familty
        self.type=type
        self.sock=None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock=socket(self.family,self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock.close()
        self.sock=None

from functools import partial

conn=LazyConnection(('www.python.org',80))

with conn as s:
    s.send(b'GET/index.html HTTP/1.0\r\n')
    s.send(b'Host: www.python.org\r\n')
    s.send(b'\r\n')
    resp=b''.join(iter(partial(s.recv,8192),b''))