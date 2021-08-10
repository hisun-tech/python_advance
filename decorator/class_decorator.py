# !/usr/bin/env python
# encoding: utf-8


"""
  @author: gaogao
  @file: class_decorator.py
  @time: 2021/7/19 15:17
  @desc:
"""


class Count:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"num of calls is:{self.num_calls}")
        return self.func(*args, **kwargs)


@Count
def example():
    print("hello world")


for i in range(10):
    example()
