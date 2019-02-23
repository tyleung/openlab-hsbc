#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2019/2/24 02:02
# @Author  : chen
# @Site    :
# @File    : render_service.py.py
# @Software: PyCharm

__author__ = "chen"

import logging

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

logger = logging.getLogger(__name__)

class Echart_Graph(object):


  def __init__(self, type='common'):

    self._type = type

    self.title = {"text": "The Chart", "left": "center"}
    self.textStyle = {"color":"#111", "fontStyle": "normal", "fontWeight": "bold", "fontFamily": "sans-serif", "fontSize": 22}
    self.tooltip = {"trigger": "axis", "axisPointer": {"animation": False}, "formatter": "function(params) {return params[0].value}"}
    self.legend = {"x": "center", "y": "bottom", "data": []}
    if type == 'common':
      self.xAxis = {"data": [0, 1, 2, 3, 4], "type": "category", "splitLine": {"show": False}}
      self.yAxis = {"type": "value", "splitLine": {"show": False}}
      self.series = [{"data":[1, 2, 1, 3, 4], "type": "line", "name": "", "color": "red", "showSymbol": False, "hoverAnimation": False}]
    elif type == 'bar':
      self.toolbox = {
        "show": True,
        "feature": {
            "mark": {"show": True},
            "dataView": {"show": True, "readOnly": False},
            "magicType": {
                "show": True,
                "type": ["pie", "funnel"]
            },
            "restore": {"show": True},
            "saveAsImage": {"show": True}
        }
      }
      self.calculable = True
      self.series = {
            "name":"面积模式",
            "type":"pie",
            "radius": [30, 110],
            "center": ["50%", "50%"],
            "roseType": "area",
            "data":[
                {"value":10, "name":"rose1"},
                {"value":5, "name":"rose2"},
                {"value":15, "name":"rose3"},
                {"value":25, "name":"rose4"},
                {"value":20, "name":"rose5"},
                {"value":35, "name":"rose6"},
                {"value":30, "name":"rose7"},
                {"value":40, "name":"rose8"}
            ]
        }


class Graph_Formatter(object):

  def get_graph(self, title_text="", xdata=[], ydata=[], series_type='line', xtype='category'):
    logger.info("start rendering graph...")
    graph = Echart_Graph()
    if len(xdata) > 0:
      graph.xAxis['data'] = xdata
      logger.info("xdata setted...")
    if len(ydata) > 0:
      graph.series[0]['data'] = ydata
      logger.info("ydata setted...")
    if title_text:
      graph.title['text'] = title_text
      logger.info("title text setted...")
    if series_type != 'pi':
      graph.series[0]['type'] = series_type
      logger.info("series type setted...")
    if xtype:
      graph.xAxis['type'] = xtype
      logger.info("xaxis type setted...")
    logger.info("finish rendering graph!")
    return graph.to_dict()
