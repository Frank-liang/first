#!/usr/bin/env python
while True:
    numb = int(raw_input("Input a number: "))
    if 1 < numb < 100:
        print "You get it"
        break
    else:
        print "Input the right number"
        continue
