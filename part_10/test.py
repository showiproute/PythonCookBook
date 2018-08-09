#!/usr/bin/env python
#coding:utf-8

'''
import os

print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))


from multiprocessing import Process
import os

def run_proc(name):
    print("Run child process %s (%s).." % (name,os.getpid()))
    print("Parent:%s"%(os.getppid()))

if __name__=='__main__':
    print(os.getpid(),os.getppid())
    print("Paretn process %s "% os.getpid())
    p=Process(target=run_proc,args=('test',))
    print("Child proces will start")
    p.start()
    p.join()
    print("Child process end.")


from multiprocessing import Pool

import os,time,random

def long_time_task(name):
    print("Run task %s (%s) ..." % (name,os.getpid()))
    start=time.time()
    time.sleep(random.random()*3)
    end=time.time()
    print("Task %s run %0.2f seconds " % (name,(end-start)))

if __name__=='__main__':
    print("Parent process %s"% os.getpid())
    p=Pool(4)
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print("Waing for all subprocesses done..")
    p.close()
    p.join()
    print("All subprocesses done.")

import subprocess

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)


from multiprocessing import Process,Queue
import os,time,random

def write(q):
    print("Process to write:%s"%os.getpid())
    for value in ['A','B','C']:
        print("Put %s to queue..."% value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    print("Process to read:%s"%os.getpid())
    while True:
        value=q.get(True)
        print("Get %s from queue."% value)

if __name__=='__main__':
    q=Queue()
    pw=Process(target=write,args=(q,))
    pr=Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()


import time,threading

def loop():
    print("Thread %s is running..."%threading.current_thread().name)
    n=0
    while n<5:
        n=n+1
        print("Thread %s >>> %s "%(threading.current_thread().name,n))
        time.sleep(1)
    print("Thread %s ended" % threading.current_thread().name)

print("Thread %s is running" % threading.current_thread().name)

t=threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print("Thread %s ended"%threading.current_thread().name)

from multiprocessing import Process
import time


def f(name):
    time.sleep(1)
    print('hello', name, time.ctime())


if __name__ == '__main__':
    p_list = []
    for i in range(3):
        p = Process(target=f, args=('alvin',))
        p_list.append(p)
        p.start()
    for i in p_list:
        p.join()
    print('end')
from multiprocessing import Process
import time
import os

def f(name):
    print("Doing process: %s pid: %s parentid:%s" % (name,os.getpid(),os.getppid()))
    time.sleep(1)

if __name__=='__main__':
    p_list=[]
    for i in range(4):
        p=Process(target=f,args=('hello',))
        p_list.append(p)
        p.start()

    for i in p_list:
        p.join()

    print("END")


from multiprocessing import Process
import time

class MyProcess(Process):
    def __init__(self):
        super().__init__()

    def run(self):
        time.sleep(1)
        print("Hello",self.name,time.ctime(),self.pid)

if __name__=='__main__':
    p_list=[]
    for i in range(3):
        p=MyProcess()
        p.start()
        p_list.append(p)

    for p in p_list:
        p.join()

    print("END")

import time
from multiprocessing import Process


def foo(i):
    time.sleep(1)
    print(p.is_alive(), i, p.pid)
    time.sleep(1)


if __name__ == '__main__':
    p_list = []
    for i in range(10):
        p = Process(target=foo, args=(i,))
        # p.daemon=True
        p_list.append(p)

    for p in p_list:
        p.start()
    # for p in p_list:
    #     p.join()

    print('main process end')

from multiprocessing import Process,Queue

def f(q,n):
    q.put([42,n,'hello'])

if __name__=="__main__":
    q=Queue()
    p_list=[]
    for i in range(3):
        p=Process(target=f,args=(q,i))
        p_list.append(p)
        p.start()
    print(q.get())
    print(q.get())
    print(q.get())
    for i in p_list:
            i.join()

from multiprocessing import Process,Pipe

def f(conn):
    conn.send([42,None,'Hello'])
    conn.close()

if __name__=='__main__':
    parent_conn,child_conn=Pipe()
    p=Process(target=f,args=(parent_conn,))
    p.start()
    print(child_conn.recv())
    p.join()


from multiprocessing import Pipe,Process

def son_process(x,pipe):
    _out_pipe,_in_pipe=pipe
    #关闭fork过来的输入端
    _in_pipe.close()
    while True:
        try:
            msg=_out_pipe.recv()
            print(msg)
        except EOFError:
            break

if __name__ == '__main__':
    out_pipe, in_pipe = Pipe(True)  #r,w
    son_p = Process(target=son_process, args=(100, (out_pipe, in_pipe)))
    son_p.start()

    # 等pipe被fork 后，关闭主进程的输出端
    # 这样，创建的Pipe一端连接着主进程的输入，一端连接着子进程的输出口
    out_pipe.close()
    for x in range(1000):
        in_pipe.send(x)
    in_pipe.close()
    son_p.join()
    print("END")


import time, threading

# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)



import time, threading

# 假定这是你的银行存款:
balance = 0
lock=threading.Lock()

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        lock.acquire()
        change_it(n)
        lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

import threading, multiprocessing

def loop():
    x = 0
    while True:
        x = x ^ 1

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()


import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()


from multiprocessing import Process,Manager

def f(d,l,n):
    d[n]='1'
    d['2']=2
    d[0.25]=None
    l.append(n)
    print(l)

if __name__=='__main__':
    with Manager() as manager:
        d=manager.dict()
        l=manager.list(range(5))

        p_list=[]
        for i in range(10):
            p=Process(target=f,args=(d,l,i))
            p.start()
            p_list.append(p)
        for res in p_list:
            res.join()

def consumer():
    r=''
    while True:
        n=yield r
#        yield r
#        n=r
        if not n:
            return
        print("[CONSUMER] Consuming %s ..." % n)
        r="200 OK"

def produce(c):
    c.send(None)
    n=0
    while n<5:
        n+=1
        print("[PRODUCER]Producing %s..." % n)
        r=c.send(n)
        print("[PRODUCER]Producing return %s" % r)
    c.close()

c=consumer()
produce(c)


import asyncio
@asyncio.coroutine
def hello():
    print("Hello world")
    #异步调用asyncio.sleep(1)
    r = yield from asyncio.sleep(1)
    print("Hello again")
#获取EventLoop
loop=asyncio.get_event_loop()
#执行coroutine
loop.run_until_complete(hello())
loop.close()
print(type(hello()))

import threading
import asyncio

@asyncio.coroutine
def hello():
    print("Hello world! (%s)" % threading.currentThread())
    yield from asyncio.sleep(1)
    print("Hello again!(%s)" % threading.currentThread())

loop=asyncio.get_event_loop()
tasks=[hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()


import asyncio

@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()



import asyncio

async def hello():
    print("Hello world!")
    r=await asyncio.sleep(1)
    print("Hello again")

loop=asyncio.get_event_loop()
tasks=[hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

import asyncio

from aiohttp import web

async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>')

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'))

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    print('Server started at http://127.0.0.1:8000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

class lazyproperty(object):
    def __init__(self,func):
        self.func=func

    def __get__(self,instance,cls):
        if instance is None:
            return self
        else:
            value=self.func(instance)
            setattr(instance,self.func.__name__,value)
            return value

import math
class Circle(object):
    def __init__(self,radius):
        self.radius=radius

    @lazyproperty
    def area(self):
        print("Computing area")
        return math.pi * self.radius **2

    @lazyproperty
    def perimeter(self):
        print("Computing perimeter")
        return 2*math.pi*self.radius

c=Circle(4.0)
print(c.radius)
print(c.area)
print(c.area)
'''


















