# !/usr/bin/env python
# encoding: utf-8


"""
  @author: gaogao
  @file: demo1.py
  @time: 2021/7/23 11:24
  @desc:
"""

import objgraph
import graphviz

a = [1, 2, 3]
b = [4, 5, 6]

a.append(b)
b.append(a)

# objgraph.show_refs([a])
# objgraph.show_backrefs([a])

filename = 'test1.dot'
obj = objgraph.show_backrefs([a], filename='sample-backref-graph.png')

with open(filename) as f:
    dot_graph = f.read()
dot = graphviz.Source(dot_graph)
dot.view()
