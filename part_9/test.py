#!/usr/bin/env python
#coding:utf-8

'''
class Screen(object):

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self,width):
        self._width=width

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self,height):
        self._height=height

    @property
    def resolution(self):
        return self._width*self._height

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')


from enum import Enum,unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

#for name, member in Month.__members__.items():
#    print(name, '=>', member, ',', member.value)


@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1=Weekday.Mon
print(day1)
print(Weekday['Tue'])
print(Weekday['Tue'].value)

@unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

print(Gender.Male.value)
print(Gender.Male)

# 测试:
bart = Student('Bart', Gender.Male.value)
if bart.gender == Gender.Male.value:
    print('测试通过!')
else:
    print('测试失败!')


class Hello(object):
    def hello(self,name='world'):
        print('Hello,%s'%name)

def fn(self,name='world'):
    print('Hello,%s'%name)

Hello=type('Hello',(object,),dict(hello=fn))
h=Hello()
h.hello()
print(type(Hello),type(h))


class ListMetaclass(type):
    def __new__(cls, name,bases,attrs):
        attrs['add']=lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)

class MyList(list,metaclass=ListMetaclass):
    pass

L=MyList()
L.add(1)
print(L)


class Field(object):
    def __init__(self,name,column_type):
        self.name=name
        self.column_type=column_type

    def __str__(self):
        return "<%s:%s>" % (self.__class__.__name__,self.name)

class StringField(Field):
    def __init__(self,name):
        super(StringField,self).__init__(name,'varchar(100)')

class IntegerField(Field):
    def __init__(self,name):
        super(IntegerField,self).__init__(name,'bigint')


class ModelMetaclass(type):
    def __new__(cls,name,bases,attrs):
        if name=='Model':
            return type.__new__(cls,name,bases,attrs)
        print("Found model:%s" % name)
        mappings=dict()
        print(attrs.items())
        print(bases)
        for k,v in attrs.items():
            if isinstance(v,Field):
                print("Found mapping %s ==> %s" % (k,v))
                mappings[k]=v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__']=mappings
        attrs['__table__']=name
        print(attrs.items())
        return type.__new__(cls,name,bases,attrs)

class Model(dict, metaclass=ModelMetaclass):
    def __init__(self,*args, **kw):
        super(Model, self).__init__(*args,**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)
    def __setattr__(self, key, value):
        self[key] = value
    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

    def print(self):
        for key in self:
            print(key,self[key])

class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()
u.print()

def avg(first,*rest):
    return (first+sum(rest))/(1+len(rest))

print(avg(1,2))
print(avg(1,2,3,4,5))

import html

def make_element(name,value,**attrs):
    keyvals=[' %s="%s"' % item for item in attrs.items()]
    attr_str=''.join(keyvals)
    element='<{name}{attrs}>{value}{/{name}>'.format(
        name=name,
        attrs=attr_str,
        value=html.escape(value)
    )
    return element

result=make_element('item','Albatross',size='large',quantitiy=6)
make_element('p','<spam>')


def add(x:int,y:int):
    return x+y

print(add(1,2),help(add))

add=lambda x,y:x+y
print(add(2,3))
print(add('hello','world'))

def add(x,y):
    return x+y

names=['David Beazley','Brian Jones','Raymond Hettinger','Ned Batchelder']
print(sorted(names,key=lambda name:name.split()[-1].lower()))

funcs=[lambda x,n=n: x+n for n in range(5)]
for func in funcs:
    print(func(1))


class Demo(object):
    def __init__(self):
        print('__init__() called...')

    def __new__(cls, *args, **kwargs):
        print('__new__() - {cls}'.format(cls=cls))
        return object.__new__(cls, *args, **kwargs)


if __name__ == '__main__':
    de = Demo()

class A(object):
    pass

class B(A):
    def __init__(self):
        print("Init")

    def __new__(cls, *args, **kwargs):
        print("New %s"%cls)
        return object.__new__(cls,*args,**kwargs)

test=B()

class C(object):
    @staticmethod
    def f():
        print("Hello")

C.f()
C().f()
'''


def scope_test():
    spam = "test spam"
    def do_local():
        spam = "local spam"  # 此函数定义了另外的一个spam字符串变量，并且生命周期只在此函数内。此处的spam和外层的spam是两个变量，如果写出spam = spam + “local spam” 会报错

    def do_nonlocal():
        nonlocal spam  # 使用外层的spam变量
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"


    do_local()
    print("After local assignmane:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)

