#!/usr/bin/env python
#coding:utf-8


def apply_async(func,args,*,callback):
    #Compute the result
    result=func(*args)

    #Invoke the callback with the result
    callback(result)

def print_result(result):
    print("Got:",result)

def add(x,y):
    return x+y

apply_async(add,(2,3),callback=print_result)

class ResultHandler(object):
    def __init__(self):
        self.sequence=0

    def handler(self,result):
        self.sequence+=1
        print("[{}] Got : {}".format(self.sequence,result))

#r=ResultHandler()
#apply_async(add,(2,3),callback=r.handler)



