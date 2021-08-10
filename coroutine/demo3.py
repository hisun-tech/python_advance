# !/usr/bin/env python
# encoding: utf-8


"""
  @author: gaogao
  @file: demo3.py
  @time: 2021/7/21 15:02
  @desc:
"""

import asyncio
import time
import threading


def tn(func):
    '''定义一个程序运行时间计算函数'''

    def wrapper(*args, **kwargs):
        start = time.time()  # 起始时间
        func(*args, **kwargs)  # 要执行的函数
        end = time.time()  # 结束时间
        print('程序运行时间:{:.2f}ms'.format((end - start)))

    return wrapper


def loop1(tname):
    print(tname + "循环loop1打印时间======" + time.ctime())
    time.sleep(1)


# @asyncio.coroutine
async def loop2(tname):  # async等同于@asyncio.coroutine
    print(tname + "循环loop1打印时间======" + time.ctime())
    # yield from asyncio.sleep(1)
    await asyncio.sleep(1)  # 等同于yield from


@asyncio.coroutine
def loop3(tname):  # async等同于@asyncio.coroutine
    print(tname + "循环loop1打印时间======" + time.ctime())
    yield from asyncio.sleep(1)
    # await asyncio.sleep(1)  # 等同于yield from


@tn
def main():
    print('多线程任务开始执行=====')
    threads = []  # 定义一个线程队列
    for i in range(5):
        t = threading.Thread(target=loop1, args=("thread" + str(i),))
        threads.append(t)
    for i in range(5):
        threads[i].start()
    for i in range(5):
        threads[i].join()

    # 协程并发测试
    print('协程并发测试开始======')
    loop = asyncio.get_event_loop()  # 获取一个event_loop
    # 任务列表
    tasks = [
        asyncio.ensure_future(loop2('11111')),
        asyncio.ensure_future(loop2('22222')),
        asyncio.ensure_future(loop2('33333')),
        asyncio.ensure_future(loop3('44444')),  # loop3
        asyncio.ensure_future(loop3('55555'))]  # loop3
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


if __name__ == '__main__':
    main()
