#!/usr/bin/env python
#coding:utf-8

import numpy as np
ax=np.array([1,2,3,4])
ay=np.array([5,6,7,8])
print(ax*2)
print(ax+10)
print(ax+ay)
print(ax*ay)

grid=np.zeros(shape=(10000,10000),dtype=float)
print(grid)
grid+=10
print(grid)

a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a)
print(a[1])
print(a[:,1])