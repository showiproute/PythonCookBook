#!/usr/bin/env python
#coding:utf-8

'''
from urllib.request import urlopen

class UrlTemplate(object):
    def __init__(self,template):
        self.template=template
    def open(self,**kwargs):
        return urlopen(self.template.format_map(kwargs))

yahoo=UrlTemplate('https://blogoflyt.cn/s={names}&f={fields}')
for line in yahoo.open(names='IBM,AAPL,FB',fields='slic1v'):
    print(line.decode('utf-8'))
#这个单方法的类可以转换成一个函数

def urltemplate(template):
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))
    return opener



def sample():
    n=0
    #Closure Function
    def func():
        print('n=',n)
    #Accessor methods for n
    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n=value
    #Attach as function attributes
    func.get_n=get_n
    func.set_n=set_n
    return func

f=sample()
f()
f.set_n(10)

print(f.get_n())
'''


import sys
class ClosureInstance(object):
    def __init__(self,locals=None):
        if locals is None:
            locals=sys._getframe(1).f_locals

        self.__dict__.update((key,value) for key,value in locals.items()
                                if callable(value))

    def __len__(self):
        return self.__dict__['__len__']()


def Stack():
    items=[]
    def push(item):
        items.append(item)

    def pop():
        return items.pop()

    def __len__():
        return len(items)

    return ClosureInstance()

s=Stack()
s.push(10)
s.push(20)
s.push('Hello')
print(len(s))

print(s.pop())
print(s.pop())