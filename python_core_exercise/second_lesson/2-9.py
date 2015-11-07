#!/usr/bin/env python
#coding=utf-8

l = [1,2,3,4,5,6,7]
sum = 0
for i in xrange(len(l)):
    sum += float(l[i])
    i += 1
    aver = sum / i
print aver
