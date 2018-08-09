#!/usr/bin/env python
#coding:utf-8

class Pair(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __repr__(self):
        return 'Pari({0.x!r},{0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s},{0.y!s})'.format(self)

p=Pair(3,4)
print(p)
print('p is {0!r}'.format(p))
print('p is {0}'.format(p))


#重写repr
def __repr__(self):
    return 'Pari(%r,%r)' % (self.x,self.y)

