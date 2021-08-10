# !/usr/bin/env python
# encoding: utf-8


"""
  @author: gaogao
  @file: usb_demo.py
  @time: 2021/8/9 10:12
  @desc:
"""

import usb.core
import usb.util
import usb.backend.libusb1
import sys

backend = usb.backend.libusb1.get_backend(
    find_library=lambda x: r"C:\Users\Jingw\Downloads\libusb-1.0.20\MS64\dll\libusb-1.0.dll")
all_devs = usb.core.find(find_all=True)
print("all_devs", all_devs)
for d in all_devs:
    print(d)
