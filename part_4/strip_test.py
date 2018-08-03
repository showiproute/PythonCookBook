#!/usr/bin/env python
#coding:utf-8

s='   Hello world \n'
print(s.strip())
print(s.lstrip())
print(s.rstrip())
t='--------hello====='
print(t.lstrip('-'))
print(t.rstrip('='))
s=' hello     world  '
print(s.replace(' ',''))
import re
print(re.sub('\s+','',s))
