#!/usr/bin/env python
#coding:

'''
import sys
print(sys.getdefaultencoding())

row=('ACME',50,91.5)
print(','.join(str(item) for item in row))

t='Hello world'
print(t[0])
for c in t:
    print(c)

b=b'aHello world'
print(b[0])


import array
import os
nums=array.array('i',[1,2,3,4])

from io import StringIO
f=StringIO()
print(f.write('hello'))
print(f.write(' '))
print(f.write('world'))
print(f.getvalue())

f=StringIO('Hello!\nHi!\nGoodbye')
while True:
    s=f.readline()
    if s=='':
        break
    print(s.strip())

from io import BytesIO
f=BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue().decode('utf-8'))
'''

import sys
print(sys.getfilesystemencoding())










