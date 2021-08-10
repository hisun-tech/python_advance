# !/usr/bin/env python
# encoding: utf-8


"""
  @author: gaogao
  @file: demo1.py
  @time: 2021/7/20 16:21
  @desc:
"""

import time


def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    time.sleep(sleep_time)
    print('OK {}'.format(url))


def main(urls):
    for url in urls:
        crawl_page(url)


start = time.time()
main(['url_1', 'url_2', 'url_3', 'url_4'])
print(str(time.time() - start))
