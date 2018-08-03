#!/usr/bin/env python
#coding:utf-8

xpts=[1,5,4]
ypts=[101,78,37,15,62,98]

for x,y in zip(xpts,ypts):
    print(x,y)


from itertools import  zip_longest
for i in zip_longest(xpts,ypts):
    print(i)

headers=['name','shares','price']
values=['ACME','100','490.1']
s=dict(zip(headers,values))
print(s)

a=[1,2,3]
b=[10,11,12]
c=['x','y','z']
for i in zip(a,b,c):
    print(i)


