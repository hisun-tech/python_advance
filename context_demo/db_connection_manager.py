# !/usr/bin/env python
# encoding: utf-8


"""
  @author: gaogao
  @file: db_connection_manager.py
  @time: 2021/7/29 14:00
  @desc:
"""


class DBConnectionManager:
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
        self.connection = None

    def __enter__(self):
        self.connection = DBClient(self.hostname, self.port)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()


with DBConnectionManager("localhost", "8080") as db_client:
    pass
