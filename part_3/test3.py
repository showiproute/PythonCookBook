#!/usr/bin/env python
#coding:utf-8
'''
mylist=[1,4,-5,10,-7,2,3,-1]
list1=[n for n in mylist if n >0]

list2=[n for n in mylist if n<0 ]

print(list1,list2)

pos=(n for n in mylist if n>0 )
print(type(pos))
for item in pos:
    print(item)

values=['1','2','-3','-','4','N/A','5']
def is_int(val):
    try:
        x=int(val)
        return True
    except ValueError:
        return False
ivals=list(filter(is_int,values))
print(ivals)

import math
result=[math.sqrt(n) for n in mylist if n>0]
print(result)

result=[math.sqrt(n) if n >0 else 0 for n in mylist]
print(result)

result=[n if n<0 else 0 for n in mylist]
print(result)
'''

