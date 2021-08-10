# !/usr/bin/env python
# encoding: utf-8


"""
  @author: gaogao
  @file: my_decorator.py
  @time: 2021/7/19 14:20
  @desc:装饰器
"""
import functools


def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("wrapper of decorator")
        print("wrapper of decorator", args)
        print("wrapper of decorator", kwargs)
        return func(*args, **kwargs)

    return wrapper


@my_decorator
def greet(*args, **kwargs):
    print("args", args)
    print("kwargs", kwargs)
    return "1"


# greet = my_decorator(greet)
print(greet.__name__)
help(greet)
print(greet(("Hello world", "Hello python"), key=1))
