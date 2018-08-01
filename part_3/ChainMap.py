#!/usr/bin/env python
#coding:utf-8

from collections import ChainMap
a={'x':1,'z':3}
b={'y':2,'z':4}

c=ChainMap(a,b)
print(c['x'])
print(c['y'])
print(c['z'])
print(len(c),c.keys(),c.values())

c['z']=10
c['w']=40
del c['x']
print(a)
