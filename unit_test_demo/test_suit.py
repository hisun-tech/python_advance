# !/usr/bin/env python
# encoding: utf-8


"""
  @author: gaogao
  @file: test_suit.py
  @time: 2021/7/20 9:48
  @desc:
"""
import unittest
from myunittest import Test3
from unittest import TestLoader

if __name__ == "__main__":
    # 实例化一个TestSuite类
    suite = unittest.TestSuite()

    loader = TestLoader()
    test_case1 = loader.loadTestsFromTestCase(Test3)
    suite.addTest(test_case1)
    runner = unittest.TextTestRunner(verbosity=2)
    #
    #     # 测试执行类的实例执行测试套件
    runner.run(suite)

    # # 把需要执行的案例放在一个list中
    # tests = [Test3("test_add"), Test3("test_minus"), Test3("test_multi"), Test3("test_divide")]
    # t2 = [Test3("test_add"), Test3("test_minus"), Test3("test_multi"), Test3("test_divide")]
    #
    # # 把案例添加到实例化好的测试套件中
    # suite.addTests(tests)
    # suite.addTests(t2)
    # # t = [t3("test_add"), t3("test_minus"), t3("test_multi"), t3("test_divide")]
    # # suite.addTests(tests)
    # with open('UnittestTextReport.txt', 'a') as  f:
    #     # 实例化一个参数执行类
    #     runner = unittest.TextTestRunner(stream=f, verbosity=2)
    #
    #     # 测试执行类的实例执行测试套件
    #     runner.run(suite)



