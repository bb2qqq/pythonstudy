# EXAMPLE 1, FIXED QUEUES

import array
import random

class Queue:
    def __init__(self, size_max):
        assert size_max > 0
        self.max = size_max
        self.head = 0
        self.tail = 0
        self.size = 0
        self.data = array.array('i', range(size_max))

    def empty(self):
        return self.size == 0

    def full(self):
        return self.size == self.max

    def enqueue(self, x):
        if self.size == self.max:
            return False
        self.data[self.tail] = x
        self.size += 1
        self.tail += 1
        if self.tail == self.max:
            self.tail = 0
        return True

    def dequeue(self):
        if self.size == 0:
            return None
        x = self.data[self.head]
        self.size -= 1
        self.head += 1
        if self.head == self.max:
            self.head = 0
        return x

def test1():
    q = Queue(3)
    res = q.empty()
    if not res:
        print "test1 NOT OK"
        return
    res = q.enqueue(10)
    if not res:
        print "test1 NOT OK"
        return
    res = q.enqueue(11)
    if not res:
        print "test1 NOT OK"
        return
    x = q.dequeue()
    if x != 10:
        print "test1 NOT OK"
        return
    x = q.dequeue()
    if x != 11:
        print "test1 NOT OK"
        return
    res = q.empty()
    if not res:
        print "test1 NOT OK"
        return
    print "test1 OK"

def test2():
    q = Queue(2)
    q.enqueue(5)
    q.enqueue(6)
    q.dequeue()
    q.dequeue()
    x = q.dequeue()
    if x != None:
        print 'test2 NOT OK'
    if q.head != 0:
        print 'test2 NOT OK'
    q.enqueue(7)
    x = q.dequeue()
    if x != 7:
        print 'test2 NOT OK'
    q.enqueue(8)
    x = q.full()
    if not x:
        print 'test2 NOT OK'

def test3():
    q = Queue(1)
    x = q.full()
    if not x:
        print 'test2 NOT OK'

test2()
test3()
