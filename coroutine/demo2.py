# !/usr/bin/env python
# encoding: utf-8


"""
  @author: gaogao
  @file: demo2.py
  @time: 2021/7/21 14:28
  @desc:
"""
import asyncio
import time


# async声明异步函数
async def crawl_page(url):
    print(f"crawling {url}")
    sleep_time = int(url.split("_")[-1])
    await asyncio.sleep(sleep_time)
    print(f"OK {url}")


async def main(urls):
    tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
    await asyncio.gather(*tasks)
    # for task in tasks:
    #     await task


start = time.time()
asyncio.run(main(["url_1", "url_2", "url_3", "url_4"]))
print(str(time.time() - start))
