#!/usr/bin/env python
#coding=utf-8

def is_leap_year(year):
    if (year % 4 == 0 or year % 4 != 100) and (year % 400 == 0):
        return True
    else:
        return False

guess = int(raw_input("Input the year: "))
if is_leap_year(guess):
    print "Leap"
else:
    print "Not Leap"
