#!/usr/bin/env python
#coding:utf-8

from tempfile import TemporaryFile

with TemporaryFile('w+t') as f:
    # Read/write to the file
    f.write('Hello World\n')
    f.write('Testing!\n')

    #Seek back to begging and read the data
    f.seek(0)
    data=f.read()

with TemporaryFile('w+t',encoding='utf-8',errors='ignore') as f:
    ##
    pass

from tempfile import NamedTemporaryFile

with NamedTemporaryFile('w+t') as f:
    print('filename is:',f.name)
    pass

with NamedTemporaryFile('w+t',delete=False) as f:
    print('Filename is:',f.name)
    
from tempfile import TemporaryDirectory

with TemporaryDirectory() as dirname:
    print('Dirname is:',dirname)
    #Use the director
    pass

