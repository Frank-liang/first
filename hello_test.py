#!/usr/bin/env python
###
def power(x,n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

def add_end(L=[]):
    L.append('END')
    return L

def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)
