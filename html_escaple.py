#!/usr/bin/env python
#coding:utf-8

s='Elements are written as "<tag>text</tag>".'
import html
print(s)
print(html.escape(s))
print(html.escape(s,quote=False))

s='Spicy Jalapeno'
print(s.encode('ascii',errors='xmlcharrefreplace'))

s='Elements are written as &quot;&lt;tag&gt;text&lt;/tag&gt;&quot;.'

print(html.unescape(s))