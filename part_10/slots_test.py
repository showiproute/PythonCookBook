#!/usr/bin/env python
#coding:utf-8

class Date(object):
    __slots__ = ['year','month','day']
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day

class A(object):
    def __init__(self):
        self._internal=0
        self.public=1

    def public_method(self):
        """
        A public method
        :return:
        """

    def _internal_method(self):
        pass

class B(object):
    def __init__(self):
        self.__private=0

    def __private_method(self):
        pass

    def public_method(self):
        pass
        self.__private_method()

class C(B):
    def __init__(self):
        super().__init__()
        self.__private=1

    def __private_method(self):
        pass

print(dir(A))

print(dir(B))

print(dir(C))