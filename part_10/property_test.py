#!/usr/bin/env python
#coding:utf-8

class Person(object):
    def __init__(self,first_name):
        self.first_name=first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self,value):
        if not isinstance(value,str):
            raise TypeError('Expected a string')
        self._first_name=value

    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")

a=Person('123')
print(a.first_name)
a.first_name='Tom'
print(a.first_name)

class Person(object):
    def __init__(self,first_name):
        self.set_first_name(first_name)

    #Getter function
    def get_first_name(self):
        return self._first_name

    #Setter function
    def set_first_name(self,value):
        if not isinstance(value,str):
            raise TypeError("Expected a string")
        self._first_name=value

    #Deleter function
    def del_first_name(self):
        raise AttributeError("Can't delete attribute")

    name=property(get_first_name,set_first_name,del_first_name)

p=Person('guido')
print(p.get_first_name())
p.set_first_name('Larry')


class Person(object):
    def __init__(self,name):
        self.name=name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        if not isinstance(value,str):
            raise TypeError("Expected a string")
        self._name=value

    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")

class SubPerson(Person):
    @property
    def name(self):
        print("Getting name")
        return super().name

    @name.setter
    def name(self,value):
        print("Seting name to",value)
        super(SubPerson,SubPerson).name.__set__(self,value)

    @name.deleter
    def name(self):
        print("Deleting name")
        super(SubPerson,SubPerson).name__delete__(self)


s=SubPerson('Guido')
print(s.name)






