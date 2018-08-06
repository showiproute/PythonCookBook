#!/usr/bin/env python
#coding:utf-8

import json

data={
    'name':'ACME',
    'shares':100,
    'price':542.23
}

json_str=json.dumps(data)
print(json_str,type(json_str))
data=json.loads(json_str)
print(data,type(data))

print(json.dumps(False))

d={'a':True,
   'b':'Hello',
    'c':None
   }

print(json.dumps(d))

'''
from urllib.request import urlopen
import json
u=urlopen('http://search.twitter.com/search.json?q=python&rpp=5')
resp=json.loads(u.read().decode('utf-8'))
from pprint import pprint
#pprint(resp)
'''

s='{"name":"ACME","shares":50,"price":490.1}'
from collections import OrderedDict
data=json.loads(s,object_pairs_hook=OrderedDict)
print(data)

class JSONObject(object):
    def __init__(self,d):
        self.__dict__=d

#data=json.loads(s,object_hook=JSONObject)
#print(data.name,data.shares)
print(json.dumps(data))
print(json.dumps(data,indent=4))

class Point(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y

def serialize_instance(obj):
    d={'__classname__':type(obj).__name__}
    d.update(vars(obj))
    return d
p=Point(2,3)
print(json.dumps(serialize_instance(p)))

classes={
    'Point':Point
}

def unseraizlie_object(d):
    clsname=d.pop('__classname__',None)
    if clsname:
        cls=classes[clsname]
        obj=cls.__new__(cls)
        for key,value in d.items():
            setattr(obj,key,value)
            return obj
    else:
        return d

p=Point(2,3)
s=json.dumps(p,default=serialize_instance)

print(s)

a=json.loads(s,object_hook=unseraizlie_object)

