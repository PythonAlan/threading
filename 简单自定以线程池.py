#!/usr/bin/env python3
#antuor:Alan

#!/usr/bin/env python
# -*- coding:utf-8 -*-
import queue
import threading
import multiprocessing

#pool = multiprocessing.Pool(10)

class ThreadPool(object):

    def __init__(self, max_num=20):
        # 创建一个队列，队列里最多只能有10个数据
        self.queue = queue.Queue(max_num)
        # 在队列里填充线程类
        # 【线程类、线程类、线程类、线程类、线程类、线程类、线程类】
        for i in range(max_num):
            self.queue.put(threading.Thread)

    def get_thread(self):
        # 去队列里去数据，
        # queue特性，如果有，对列里那一个出来
        #            如果没有，阻塞，
        return self.queue.get()

    def add_thread(self):
        # 往队列里再添加一个线程类
        self.queue.put(threading.Thread)

# pool = ThreadPool(10)


pool = ThreadPool(10)

def func(arg, p):
    # 函数内容
    print(arg)
    import time
    time.sleep(2)

    # 在线程池里重新添加一个线程（将线程归还给线程池）
    p.add_thread()

for i in range(30):
    # 去线程池里那一个线程，如果有，则池子里拿，如果没有，等直到有人归还线程到线程池
    thread = pool.get_thread()
    # thread = threading.Thread
    t = thread(target=func, args=(i, pool))
    t.start()