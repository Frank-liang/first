#!/usr/bin/env python
#conding=utf-8
import threading
import time
class Th(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.t_name = name
    def run(self):
        print "This is "+ self.t_name
if __name__ == '__main__':
    thread1 = Th("Thread_1")
    thread1.start()
