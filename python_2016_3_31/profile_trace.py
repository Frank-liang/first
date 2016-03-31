#!/usr/bin/env/python
import sys

def profiler(event, arg):
    print 'PROFILER: %r %r %r' %(event, arg)

sys.setprofile(profiler)

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
def fib_seq(n):
    seq = [ ]
    if n > 0:
        seq.extend(fib_seq(n-1))
    seq.append(fib(n))
    return seq
print fib_seq(2)
