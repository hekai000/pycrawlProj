# -*- coding: utf-8 -*-
import os, time, random
from multiprocessing import Pool


def run_task(name):

    print 'Task %s （%s）Runing' % (name, os.getpid())
    time.sleep(random.random()*3)
    print "Task %s end" % name


if __name__ == "__main__":
    print "Current process %s." % os.getpid()
    p = Pool(processes=3)
    for i in range(5):
        p.apply_async(run_task, args=(i,))
    print "Waiting for all subprocessing done"
    p.close()
    p.join()
    print "All Process end"
    print "add new line"
