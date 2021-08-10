# !/usr/bin/env python
# encoding: utf-8


"""
  @author: gaogao
  @file: generator_demo1.py
  @time: 2021/7/20 11:45
  @desc:
"""


def generator(k):
    i = 1
    while True:
        yield i ** k
        i += 1


gen_1 = generator(1)
gen_3 = generator(3)
print("gen_1", gen_1)
print("gen_3", gen_3)


def get_sum(n):
    sum_1, sum_3 = 0, 0
    for i in range(n):
        next_1 = next(gen_1)
        next_3 = next(gen_3)
        print(f"next_1={next_1},next_3={next_3}")
        sum_1 += next_1
        sum_3 += next_3
    print(sum_1 * sum_1, sum_3)


# get_sum(10)


def index_normal(L, target):
    result = []
    for i, num in enumerate(L):
        if num == target:
            result.append(i)
    return result


def index_generator(L, target):
    for i, num in enumerate(L):
        if num == target:
            yield i


import time


# start = time.time()
# print("start", start)
# print(index_normal([1, 6, 2, 4, 5, 2, 8, 6, 3, 2], 2))
#
# print("end1", time.time())
# start = time.time()
# print("start1", start)
# print(list(index_generator([1, 6, 2, 4, 5, 2, 8, 6, 3, 2], 2)))
# print("end2", time.time())


def is_subsequence(a, b):
    b = iter(b)
    return all(i in b for i in a)


print(is_subsequence([1, 3, 5], [1, 2, 3, 4, 5]))
print(is_subsequence([1, 4, 3], [1, 2, 3, 4, 5]))
