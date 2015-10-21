#!/usr/bin/env python

import random

f=open('f.txt','a')
f.write(str(random.randint(0,9)))
f.write('\n')
f.close()
    
