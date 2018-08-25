#!/usr/bin/env python
#coding:utf-8

import time
from threading import Thread

def count_down(n):
    while n>0:
        time.sleep(1)
        print("count:%d"%n)
        n-=5
        time.sleep(1)

#t=Thread(target=count_down,args=(10,),daemon=True)
#t.start()

class CountdownTask(object):
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print('T-minus', n)
            n -= 1
#            time.sleep(5)

#c = CountdownTask()
#t = Thread(target=c.run, args=(10,))
#t.start()
#c.terminate() # Signal termination
#t.join()      # Wait for actual termination (if needed)


class IOTask:
    def terminate(self):
        self._running = False

    def run(self, sock):
        # sock is a socket
        sock.settimeout(5)        # Set timeout period
        while self._running:
            # Perform a blocking I/O operation w/ timeout
            try:
                data = sock.recv(8192)
                break
            except socket.timeout:
                continue
            # Continued processing
            ...
        # Terminated
        return

class CountdownThread(Thread):
    def __init__(self, n):
        super().__init__()
        self.n = n
    def run(self):
        while self.n > 0:

            print('T-minus', self.n)
            self.n -= 1
            time.sleep(5)

c = CountdownThread(5)
c.start()

