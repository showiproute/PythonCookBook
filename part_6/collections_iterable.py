#!/usr/bin/env python
#coding:utf-8

from collections import Iterable

def flatten(items,ignore_types=(str,bytes)):
    for x in items:
        if isinstance(x,Iterable) and not isinstance(x,ignore_types):
            yield from flatten(x)
        else:
            yield x

#Flatten not use yield from

def flatten2(items,ignore_types=(str,bytes)):
    for x in items:
        if isinstance(x,Iterable) and not isinstance(x,ignore_types):
            for i in flatten2(x):
                yield i
        else:
            yield x

items=[1,2,[3,4,[5,6],7],8]
for x in flatten(items):
    print(x)

items2=['Dave','Paula',['Thomas','Lewis']]
for x in flatten(items2):
    print(x)

for x in flatten2(items2):
    print(x)
