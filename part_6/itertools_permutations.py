#!/usr/bin/env python
#coding:utf-8

items=['a','b','c']
from itertools import permutations,combinations,combinations_with_replacement

for p in permutations(items):
#    print(p)
    pass

for p in permutations(items,2):
#    print(p)
    pass

for c in combinations(items,2):
    #print(c)
    pass

for c in combinations(items,1):
    #print(c)
    pass

for c in combinations_with_replacement(items,3):
    print(c)

    