#!/usr/bin/env python
#coding=utf-8
import sys
l = [2,3,4,5,6]
Input = raw_input("Input and devide or exit: ")

if Input == "and":
    sum = 0
    for i in l:
        sum += i
    print sum    
if Input == "devide":
    sum = 0
    for i in l:
        sum += i
        end = sum / 5
    print end
if Input == "exit":
    sys.exit(0)

