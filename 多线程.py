#!/usr/bin/env python3
#antuor:Alan


import threading
import time

def sayhi(num): #定义每个线程要运行的函数

    print("running on number:%s" %num)

    time.sleep(3)

if __name__ == '__main__':

    t1 = threading.Thread(target=sayhi,args=(1,)) #生成一个线程实例
    t2 = threading.Thread(target=sayhi,args=('Alan',)) #生成另一个线程实例
    t3 = threading.Thread(target=sayhi,args=(3,))   #args必须传入一个元祖，逗号不能少
    t1.setName('first thread')   #给线程设置名字
    t1.setDaemon(True)
    t1.start() #启动线程
    t2.start() #启动另一个线程
    t3.start()

    print(t1.getName()) #获取线程名
    print(t2.getName())