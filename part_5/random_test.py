#!/usr/bin/env python
#coding:utf-8

import random

values=[1,2,3,4,5,6]
print(random.choices(values))

print(random.sample(values,2))
print(random.sample(values,5))

print(random.randint(0,10))

print(random.random())
print(random.getrandbits(200))
