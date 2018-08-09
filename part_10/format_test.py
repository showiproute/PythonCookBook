#!/usr/bin/env python
#coding:utf-8

_formats={
    'ymd':'{0.year}-{0.month}-{0.day}',
    'mdy':'{0.month}/{0.day}/{0.year}',
    'dmy':'{0.day}/{0.month}/{0.year}'
}

class Date(object):
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day

    def __format__(self, code):
        if code=='':
            code='ymd'
        fmt=_formats[code]
        return fmt.format(self)

d=Date(2012,12,21)
print(format(d))
print(format(d,'mdy'))
print('The date is {:ymd}'.format(d))

from datetime import date
d=date(2012,12,21)
print(format(d))
print(format(d,'%A,%B %d,%Y'))
