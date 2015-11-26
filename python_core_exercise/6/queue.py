#!/usr/bin/env python
#coding=utf-8
queue = []
def enQ():
    queue.append(raw_input('Enter new string: ').strip())

def deQ():
    if len(queue) == 0:
        print 'Cannot pop from an empty queue'
    else:
        queue.pop(0)
        print 'Removed [','queue.pop(0)',']'

def viewQ():
    print queue

CMDs = {'e': enQ, 'd': deQ, 'v': viewQ}

def showmenu():
    pr = """ 
    p(U)sh
    p(O)P
    (V)iew
    (Q)uit

    Enter choice: """

    while True:
        while 1:
            try:
                choice = raw_input(pr).strip()[0].lower()
            except:
                choice = 'q' 
    
            print '\nYou picked: [%s]' %choice
            if choice not in 'edvq':
                print 'Invalid option, try again'
            else:
                break
    
        if choice == 'q':
            break
        CMDs[choice]()

if __name__ == '__main__':
    showmenu()
    
