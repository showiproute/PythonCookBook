#!/usr/bin/env python
#coding:utf-8

import csv
headers=['Symbol','Price','Date','Time','Change','Volume']
rows=[('AA',39.48,'6/11/2007','9:36am',-0.18,181800),
('AA',39.48,'6/11/2007','9:36am',-0.18,181800),
('AA',39.48,'6/11/2007','9:36am',-0.18,181800),
      ]

headers=['Symbol','Price','Date','Time','Change','Volume']
rows=[{'Symbol':'AA','Price':39.48,'Date':'6/11/2007',
       'Time':'9:36am','Change':-0.18,'Volume':181800}]

with open('stocks2.csv','w+') as f:
    f_csv=csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)


with open('stocks.csv2','w') as f:
    f_csv=csv.DictWriter(f,headers)
    f_csv.writeheader()
    f_csv.writerows(rows)
