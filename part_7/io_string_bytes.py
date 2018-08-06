#!/usr/bin/env python
#coding:utf-8

import io
s=io.StringIO()
s.write('Hello world\n')
print('This is a test',file=s)
print(s.getvalue())

s=io.BytesIO()
s.write(b'binary data')
print(s.getvalue())
