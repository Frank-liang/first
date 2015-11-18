#!/usr/bin/env python
#coding=utf-8
score = int(raw_input("Input you score,between 1 and 100: "))
if score <= 100 and score >=90:
    print "A"
elif score >=80 and score <=89:
    print 'B'
elif score >=70 and score <=79:
    print 'C'
elif score >=60 and score <=69:
    print 'D'
elif score < 60:
    print 'F'
