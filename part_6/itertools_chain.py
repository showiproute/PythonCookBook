#!/usr/bin/env python
#coding:utf-8

from itertools import chain

a=[1,2,3,45]
b=['x','y','z']
for x in chain(a,b):
    print(x)

