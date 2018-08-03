#!/usr/bin/env python
#coding:utf-8

import os
import fnmatch
import gzip
import bz2
import re

def get_find(filepat,top):
    """
    Find all filenames in a directory tree that match a shell
    wildcard pattern
    :param filepat:
    :param top:
    :return:
    """
    for path,dirlist,filelist in os.walk(top):
        for name in fnmatch.filter(filelist,filepat):
            yield os.path.join(path,name)

def gen_opener(filenames):
    """
    Open a sequence of filnaes one at a time producing a file object
    The file is clolsed immediately when proceeding to the next
    iteration
    :param filename:
    :return:
    """
    for filename in filenames:
        if filename.endswith('.gz'):
            f=gzip.open(filename,'rt')
        elif filename.endswith('.bz2'):
            f=bz2.open(filename,'rt')
        yield f
        f.close()

def gen_concatenate(iteators):
    """
    Chain a sequence of iterators together into a single sequence
    :param iteators:
    :return:
    """
    for it in iteators:
        yield from it

def gen_grep(pattern,lines):
    """
    look for a regex pattern in a sequnce of lines
    """
    pat=re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line
