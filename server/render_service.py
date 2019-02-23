#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2019/2/24 02:02
# @Author  : chen
# @Site    : 
# @File    : render_service.py.py
# @Software: PyCharm

__author__ = "chen"


# {
#     "title": {
#         "text": "chart for age distribution",
#         "left": "center",
#         "textStyle":{
#             "color":"#111",
#             "fontStyle": "normal",
#             "fontWeight": "bold",
#             "fontFamily": "sans-serif",
#             "fontSize": 22
#         }
#     },
#     "xAxis": {
#         "type": "category",
#         "data": ["[0, 10)", "[21, 30)", "[15, 21)", "[10, 15)", "[30, 35)",
#        "[35, 100)"]
#     },
#     "yAxis": {
#         "type": "value"
#     },
#     "series": [{
#         "data": [2578, 2249, 1603, 1293, 1222, 1055],
#         "type": "bar"
#     }]
# }


class Echart_Graph(object):

  def __init__(self):
    self.title = {"text": "The Chart", "left": "center"}
    self.textStyle = {"color":"#111", "fontStyle": "normal", "fontWeight": "bold", "fontFamily": "sans-serif", "fontSize": 22}
    self.xAxis = {"type": "category", "data": []}
    self.yAxis = {"type": "value"}
    self.series = [{"data":[], "type": "line", "name": "", "color": "red", "showSymbol": "false", "hoverAnimation": "false"}]

  def to_dict(self):
    s = dict()
    self.title['textStyle'] = self.textStyle
    s['title'] = self.title
    s['xAxis'] = self.xAxis
    s['yAxis'] = self.yAxis
    s['series'] = self.series
    return s

class Graph_Formatter(object):

  def __init__(self):
    pass

  def get_graph(self, data=[]):
    return Echart_Graph().to_dict()