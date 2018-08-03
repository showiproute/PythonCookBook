#!/usr/bin/env python
#coding:utf-8

def parse_data(filename):
    with open(filename,'rt') as f:
        for lineo,line in enumerate(f,1):
            fileds=line.split()
            try:
                count=int(fileds[1])
                '''
                expression
                '''
            except ValueError as e:
                print('Line{}: Parse errpor:{}'.format(lineo,e))

data=[(1,2),(3,4)]

for index,(x,y) in enumerate(data):
    print(index,(x,y))