#!/usr/bin/env python
#coding:utf-8

filename="spam.txt"
print(filename.endswith(".txt"))
print(filename.startswith("spam"))

url="http://www.python.org"

url.startswith("http:")

import os
filenames=os.listdir('.')
print(filenames)
result=[name for name in filenames if name.endswith(('.py','txt'))]
print(result)

from urllib.request import urlopen

def read_data(name):
    if name.startwith(('http:','https:','ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

choices=['https:','ftp:']
url="https://www.python.org"

result=url.startswith(tuple(choices))
print(result)