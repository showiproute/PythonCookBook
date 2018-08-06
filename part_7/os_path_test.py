#!/usr/bin/env python
#coding:utf-8

import os
path='/User/beazley/Data/data.csv'

print(os.path.basename(path))

print(os.path.dirname(path))

print(os.path.join('tmp','data',os.path.basename(path)))

path='~/Data/data.csv'
print(os.path.expanduser(path))

print(os.path.splitext(path))

print(os.path.exists('/etc/passwd'))

print(os.path.isfile('/etc/passwd'))
print(os.path.isdir('/tmp'))

names=os.listdir('somedir')

names=[name for name in os.listdir('somedir')
        if os.path.isfile(os.path.join('somedir',name))]

dirnames=[name for name in os.listdir('somedir')
        if os.path.isdir(os.path.join('somedir',name))]

pyfiles=[name for name in os.listdir('somedir')
         if name.endswith('.py')]

import os
import os.path
import glob

pyfiles=glob.glob('*.py')

name_sz_date=[(name,os.path.getsize(name),os.path.getmtime(name))
              for name in pyfiles]

for name,size,mtime in name_sz_date:
    print(name,size,mtime)

file_metadata=[(name,os.stat(name)) for name in pyfiles]
for name,meta in file_metadata:
    print(name,meta.st_size,meta.st_mtime)
