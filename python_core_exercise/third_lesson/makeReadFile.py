#!/usr/bin/env python
#coding=utf-8                                                                      
import os
ls = os.linesep                                                                    
def writeFile():
    while True:
        fname = raw_input("Input the file name you are build: ")                       
        if os.path.exists(fname):                                                      
            print "ERROR: '%s' already exists" %fname                                  
        else:
            break                                                                      
    all = []
    print "\nEnter lines('.' by inself to quit).\n"                                    
    while True:  
        entry = raw_input('Input the content: ')                                       
        if entry == '.':
            break                                                                      
        else:    
            all.append(entry)                                                          
    fobj = open(fname,'w')                                                             
    fobj.writelines(['%s%s' %(x,ls) for x in all])                                     
    fobj.close()
    print 'DONE!'

def readFile():
    fname = raw_input("Enter filename: ")
    print 'You want to open %s' %fname
    
    try:
        fobj = open(fname,'r')
    except IOError,e:
        print "*** file open error:",e
    else:
        for eachLine in fobj:
            print eachLine.strip(),
        fobj.close()
if __name__ == "__main__":
    while 1:
        print """please select target:
        1) read txtfile
        2)create testfile
        3)quit
        """
        getcode = raw_input("which one:")
        if getcode == '1':
            readFile()
        elif getcode == '2':
            writeFile()
        elif getcode == '3':
            break
        else:
            print ("check you choice, repeat")
