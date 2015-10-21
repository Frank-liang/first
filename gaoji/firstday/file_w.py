#!/usr/bin/env python

f = open('f.txt','w')
for i in range(0,10):
    f.write(str(i)+'\n')
f.close()    
