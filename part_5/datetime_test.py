#!/usr/bin/env python
#coding:utf-8

from datetime import timedelta

a=timedelta(days=2,hours=6)
b=timedelta(hours=4.5)
c=a+b
print(c.days,c.seconds,c.total_seconds())

from datetime import datetime
a=datetime(2012,9,23)
print(a+timedelta(days=10))
b=datetime(2012,12,21)
d=b-a
print(d)

now=datetime.today()

result2=now+timedelta(minutes=10)

print(now<result2)

a=datetime(2012,3,1)
b=datetime(2012,2,28)
print(a-b)

a=datetime(2012,9,23)

from dateutil.relativedelta import relativedelta
print(a+relativedelta(months=+1))


"""
Topic:最后的周五
Desc：
"""

from datetime import datetime,timedelta

weekdays=['Monday','Tuesday','Wednesday','Thursday','Friday',
          'Saturday','Sunday']

def get_previous_byday(dayname,start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num=start_date.weekday()
    print('Day_num:',day_num)
    day_num_target=weekdays.index(dayname)
    days_ago=(7+day_num-day_num_target) % 7
    if days_ago == 0:
        days_ago=7
    target_date=start_date-timedelta(days=days_ago)
    return target_date


