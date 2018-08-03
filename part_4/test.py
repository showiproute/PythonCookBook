#!/usr/bin/env python
#coding:utf-8

'''
line="asdf fjdk; afed, fjek,asdf, foo"
import re
result=re.split(r'[;,\s]\s*',line)
print(result)

fields=re.split(r'(;|,|\s)\s*',line)
print(fields)

values=fields[::2]+['']
delimiters=fields[1::2]+['']
print(values)
print(delimiters)

result=''.join(v+d for v,d in zip(values,delimiters))
print(result)


from fnmatch import fnmatch,fnmatchcase
print(fnmatch('foo.txt','*.txt'))
names=['Dat1.csv','Dat2.csv','config.ini','foo.py']
print([name for name in names if fnmatch(name,'Dat*.csv')])

text='yeah, but no ,but yeah,but no,but yeah'

print(text.startswith('yeah'))

print(text.find('no'))

text1='11/27/2012'
text2='Nov 27,2012'

import re
if re.match(r'\d+/\d+/\d+',text1):
    print('yes')
else:
    print('no')

detepat=re.compile(r'\d+/\d+/\d+')
if detepat.match(text1):
    print('yes')
else:
    print('No')

text='Today is 11/27/2012,PyCon starts 3/13/2013'
print(detepat.findall(text))

datepat=re.compile(r'(\d+)/(\d+)/(\d+)')

m=datepat.match('11/27/2012')
print(m.group(0),m.group(1))
print(m.groups())

print(datepat.findall(text))
for month,day,year in datepat.findall(text):
    print('{}{}{}'.format(year,month,day))

for m in datepat.finditer(text):
    print(m.groups())


text='yeah,but no but yeah,but no ,but yea'

result=text.replace('yeah','yep')
print(result)

text='Today is 11/27/2012,PyCon starts 3/13/2013'
import re
print(re.sub(r'(\d+)/(\d+)/(\d+)',r'\3-\1-\2',text))

import re

str_pat=re.compile(r'\"(.*?)\"')
text1='Computer says "no."'
print(str_pat.findall(text1))

text2='Computer says "no." Phone says "yes"'
print(str_pat.findall(text2))

import re
num=re.compile('\d+')
print(num.match('123'))
'''

s=b'Hello world'
print(s)

