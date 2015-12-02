#!/usr/bin/env python
#coding=utf-8
stack = []

def pushit():
    stack.append(raw_input('Enter new string: ').strip())

def popit():
    if len(stack) == 0:
        print 'Cnnot pop from an empty stack!'
    else:
        stack.pop()
        print 'Removed [','stack.pop()',']'

def viewstack():
    print stack

CMDs = {'u': pushit, 'o':popit, 'v': viewstack}

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
            if choice not in 'uovq':
                print 'Invalid option, try again'
            else:
                break
            
        if choice == 'q':
            break
        CMDs[choice]()

if __name__ == '__main__':
    showmenu()

