#!/usr/bin/env python
#coding:utf-8

class A(object):
    def spam(self):
        print("A.SPAM")

class B(A):
    def spam(self):
        print("B.SPAM")
        super().spam()

bb=B()
bb.spam()


class A(object):
    def __init__(self):
        self._x=0

class B(A):
    def __init__(self):
        super().__init__()
        self.y=1

bb=B()

class Proxy(object):
    def __init__(self,obj):
        self._obj=obj

    def __getattr__(self, name):
        return getattr(self._obj,name)

    def __setattr__(self, name, value):
        if name.startwith('_'):
            super().__setattr__(name,value)
        else:
            setattr(self._obj,name,value)

class Base(object):
    def __init__(self):
        print('Base.__init__')

class A(Base):
    def __init__(self):
        Base.__init__(self)
        print('A.__init__')

#aa=A()
#aa

class Base(object):
    def __init__(self):
        print("Base.__init__")

class A(Base):
    def __init__(self):
        super().__init__()
        print('A.__init__')

class B(Base):
    def __init__(self):
        super().__init__()
        print('B.__init__')

class C(A,B):
    def __init__(self):
        super().__init__()
        print('C.__init__')

c=C()
print(C.__mro__)

class A(object):
    def spam(self):
        print('A.spam')
        super().spam()

class B(object):
    def spam(self):
        print('B.spam')

class C(A,B):
    pass

c=C()
c.spam()
print(C.__mro__)