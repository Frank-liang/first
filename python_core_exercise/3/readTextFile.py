#!/usr/bin/env python
#coding=utf-8
fname = raw_input("Enter filename: ")
print 'You want to open %s' %fname

try:
    fobj = open(fname,'r')
except IOError,e:
    print "*** file open error:",e
else:
    for eachLine in fobj:
        print eachLine.strip(),
    fobj.close()
