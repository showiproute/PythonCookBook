#!/usr/bin/env python
#coding:utf-8

import gzip
#with gzip.open(r'F:\Linux source\bind-9.7.3-P1.tar.gz','rt',errors='ignore') as f:
#    text=f.read()
#    print(text)

import bz2
with bz2.open(r'F:\Linux source\busybox-1.20.2.tar.bz2','rt',encoding='utf-8',errors='replace') as f:
    text=f.read()
    print(f.encoding)


