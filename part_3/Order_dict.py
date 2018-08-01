#!/usr/bin/env python
#coding:utf-8

from collections import OrderedDict
def order_dict():
    d=OrderedDict()
    d['foo']=1
    d['bar']=2
    d['spam']=3
    d['grok']=4
    for key in d:
        print(key,d[key])

order_dict()