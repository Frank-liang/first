#!/usr/bin/env python
#coding=utf-8

import threading
import time
class Th(threading.Thread):
    def __init__(self, thread_name):
        threading.Thread.__init__(self)
        self.setName(thread_name)
    
    def run(self):
        threadLock.acquire()
        print "This is thread" + self.getName()
        for i in range(3):
            time.sleep(0.5)
            print str(i)
        print self.getName() + "is over"
        threadLock.release()
if __name__ == "__main__":
    threadLock = threading.Lock()
    thread1 = Th('Thread_1')
    thread2 = Th("Thread_2")
    thread1.start()
    thread2.start()
