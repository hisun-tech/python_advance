# !/usr/bin/env python
# encoding: utf-8


"""
  @author: gaogao
  @file: foo.py
  @time: 2021/7/29 12:36
  @desc:
"""


class Foo:
    def __init__(self):
        print("__init__ called")

    def __enter__(self):
        print("__ernter__ called")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__  called")
        if exc_type:
            print(f"exc_type:{exc_type}")
            print(f"exc_val:{exc_val}")
            print(f"exc_tb:{exc_tb}")
            print("exception handled")
        return True


with Foo() as obj:
    raise Exception("exception raised").with_traceback(None)
