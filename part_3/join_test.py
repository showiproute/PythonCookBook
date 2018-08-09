#!/usr/bin/env python
#coding:utf-8

parts=['Is','Chicago','Not','Chicago?']
print('，'.join(parts))

data=['ACME',50,91.1]
print(','.join(str(d) for d in data))

def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'

text=''.join(sample())
print(text)

#Option 1
for part in sample():
    f.write(part)

#Option 2

def combine(source,maxsize):
    parts=[]
    size=0
    for part in source:
        parts.append(part)
        size+=len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts=[]
            size=0
        yield ''.join(parts)

#结合文件操作
with open('filename','w') as file:
    for prt in combine(sample(),32768):
        f.write(part)
