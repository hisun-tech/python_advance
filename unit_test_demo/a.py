# !/usr/bin/env python
# encoding: utf-8


"""
  @author: gaogao
  @file: a.py
  @time: 2021/7/29 15:48
  @desc:
"""
import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
import pdb


def side_effect(arg):
    if arg < 0:
        return 1
    else:
        return 2


class A(unittest.TestCase):
    def m1(self):
        val = self.m2()
        self.m3(val)

    def m2(self):
        pass

    def m3(self, val):
        pass

    def test_m1(self):
        a = A()
        a.m2 = MagicMock(return_value="custom_val")
        a.m3 = MagicMock()
        a.m1()
        self.assertTrue(a.m2.called)
        a.m3.assert_called_with("custom_val")


if __name__ == "__main__":
    # unittest.main()
    # mock = MagicMock()
    # mock.side_effect = side_effect
    # print(mock(-1))
    # print(mock(1))
    a  = 1
    b =2
    pdb.set_trace()
    c = 3
    print(a+b+c)
