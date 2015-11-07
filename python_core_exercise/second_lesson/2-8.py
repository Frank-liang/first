#!/usr/bin/env python
#coding=utf-8
def fir():
    l = [1,2,3,4,5]
    i = 0
    sum = 0
    while i < len(l):
        sum += l[i]
        i += 1
    print sum    

def sec():
    l = [1,2,3,4,5]
    for i in xrange(len(l)):
        sum += l[i]
    print sum    

fir()
sec()





    

