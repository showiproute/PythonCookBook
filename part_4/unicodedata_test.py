#!/usr/bin/env python
#coding:utf-8

s1='Spicy Jalape\u00f1o'
s2='Spicy Jalapen\u0303o'

import unicodedata
t1=unicodedata.normalize('NFC',s1)
t2=unicodedata.normalize('NFC',s2)
print(t1==t2,ascii(t1))