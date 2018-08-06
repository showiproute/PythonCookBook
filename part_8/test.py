#!/usr/bin/env python
#coding:utf-8

'''
import csv
with open('stocks.csv') as f:
    f_csv=csv.reader(f)
    headers=next(f_csv)
    print(headers)
    for row in f_csv:
        print(row)
'''

import struct
result=struct.pack('>I',10240099)
print(result,type(result))



