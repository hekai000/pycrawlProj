# -*- coding: utf-8 -*-
import random
import time, threading

mylock = threading.RLock()
num = 0
class myThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)

    def run(self):
        global num
        while True:
            mylock.acquire()
            print "Current %s Locked, num is %s " % (threading.current_thread().name, num)
            if num >= 4:
                mylock.release()
                print "Current %s release, num is %s" % (threading.current_thread().name, num)
                break
            num += 1
            print "Current %s release, num is %s" % (threading.current_thread().name, num)
            mylock.release()

if __name__ == "__main__":
    t1 = myThread(name="Thread_1")
    t2 = myThread(name="Thread_2")
    t1.start()
    t2.start()