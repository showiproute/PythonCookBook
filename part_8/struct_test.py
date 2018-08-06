#!/usr/bin/env python
#coding:utf-8

from struct import Struct

def write_records(records,format,f):
    """
    write a sequence of tuples to a binary file of structures
    :param records:
    :param format:
    :param f:
    :return:
    """
    record_struct=Struct(format)
    for r in records:
        f.write(record_struct.pack(*r))

if __name__=='__main__':
    records=[(1,2.3,4.5),
             (6,7.8,9.0),
             (12,13.4,56.7)
             ]
    with open('data.b','wb') as f:
        write_records(records,'<idd',f)

