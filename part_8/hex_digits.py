#!/usr/bin/env python
#coding:utf-8

s=b'Hello'
import binascii
h=binascii.b2a_hex(s)
print(h)
h=binascii.a2b_hex(h)
print(h)

import base64
h=base64.b16encode(s)
print(h)
print(base64.b16decode(h))

h=base64.b16encode(s)
print(h)
print(h.decode('ascii'))

a=b'Hello'
import base64

a=base64.b64encode(s)
print(a)

print(base64.b64decode(a))

print(base64.b64encode(a).decode('utf-8'))








