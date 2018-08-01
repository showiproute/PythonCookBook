#!/usr/bin/env python
#coding:utf-8

from collections import namedtuple
Subscriber=namedtuple('Subscriber',['addr','joined'])
sub=Subscriber('jonesy@example.com','2012-10-19')
print(sub,type(sub))
print(sub.addr,sub.joined)

def compute_cost(records):
    total=0.0
    for rec in records:
        total+=rec[1]*rec[2]
    return total

Stock=namedtuple('Stock',['name','shares','price'])
def compute_cost(records):
    total=0.0
    for rec in records:
        s=Stock(*rec)
    total+=s.shares*s.price
    return total

Stock=namedtuple('Stock',['name','shares','price','date','time'])

#Create a prototype instance
stock_prototype=Stock('',0,0.0,None,None)

#Functon to convert a dictionary to a Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)

a={'name':'ACME','shares':100,'price':'123.45'}
result=dict_to_stock(a)
print(result)

b={'name':'ACME','shares':100,'price':123.45,'date':'1111'}
result2=dict_to_stock(b)
print(result2)