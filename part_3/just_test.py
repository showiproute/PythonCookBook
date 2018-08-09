#!/usr/bin/env python
#coding:utf-8

text='Hello world'
print(text.ljust(20,'-'))
print(text.rjust(20,'='))
print(text.center(20,'*'))
print(format(text,'=>20'))
print(format(text,'=<20'))
print(format(text,'*^20'))
