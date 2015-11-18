#!/usr/bin/env python
#coding=utf-8
import os
ls = os.linesep
while True:
    fname = raw_input("Input the file name you are build: ")
    if os.path.exists(fname):
        print "ERROR: '%s' already exists" %fname
    else:
        break
all = []
print "\nEnter lines('.' by inself to quit).\n"
while True:
    entry = raw_input('Input the content: ')
    if entry == '.':
        break
    else:
        all.append(entry)
fobj = open(fname,'w')
fobj.writelines(['%s%s' %(x,ls) for x in all])
fobj.close()
print 'DONE!'
