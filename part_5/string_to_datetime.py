#!/usr/bin/env python
#coding:utf-8

from datetime import datetime
text='2012-09-20'
y=datetime.strptime(text,'%Y-%m-%d')
print(y)
z=datetime.now()
print(z-y)
nice_z=datetime.strftime(z,'%A %B %d %Y')
print(nice_z)

def parse_ymd(s):
    year_s,mon_s,day_s=s.split('-')
    return datetime(int(year_s),int(mon_s),int(day_s))
