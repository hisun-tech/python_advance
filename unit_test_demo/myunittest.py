# !/usr/bin/env python
# encoding: utf-8


"""
  @author: gaogao
  @file: myunittest.py
  @time: 2021/7/20 9:47
  @desc:
"""

import unittest
import func


class Test3(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("this is class before")

    @classmethod
    def tearDownClass(cls) -> None:
        print("this is class after")

    # def setUp(self) -> None:
    #     print("this is before")
    #
    # def tearDown(self) -> None:
    #     print("this is after")

    def test_add(self):
        self.assertEqual(3, func.add(1, 2))

    def test_minus(self):
        self.assertEqual(2, func.minus(4, 2))

    def test_multi(self):
        self.assertEqual(4, func.multi(2, 2))

    def test_divide(self):
        self.assertEqual(2, func.divide(4, 2))
