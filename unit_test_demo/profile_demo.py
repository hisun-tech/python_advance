# !/usr/bin/env python
# encoding: utf-8


"""
  @author: gaogao
  @file: profile_demo.py
  @time: 2021/7/29 17:02
  @desc:
"""
import cProfile


def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]

    return helper


@memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib2(n):
    # 定义初始条件
    a, b, count = 0, 1, 0
    while True:
        if count > n:  # 设置终止条件
            return
        print("a", a)
        yield a
        a, b = b, a + b
        print("a", a)
        print("b", b)
        count += 1


# def fib_seq(n):
#     res = []
#     if n > 0:
#         res.extend(fib_seq(n - 1))
#     res.append(fib(n))
#     return res
def fib_seq(n):
    return list(fib2(n))


# cProfile.run('fib_seq(10000)')
print(fib_seq(10))
