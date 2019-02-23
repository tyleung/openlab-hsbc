#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2019/2/24 03:40
# @Author  : chen
# @Site    : 
# @File    : realtime_monitor_service.py
# @Software: PyCharm

__author__ = "chen"

import logging
from datetime import datetime as dt
from datetime import timedelta
import numpy as np
import pandas as pd
import random

logger = logging.getLogger(__name__)

class Realtime_Monitor(object):

  timerange = pd.date_range(start=dt.now().strftime('%Y%m%d'),
                            end=(dt.now() + timedelta(days=1)).strftime('%Y%m%d'),
                            freq='5min')
  rand_data = []
  value = 0
  for _ in range(len(timerange)):
    value = np.abs(value + random.random() * 21 - 10)
    rand_data.append(value)
  data = pd.Series(index=timerange, data=rand_data)

  def __init__(self):
    pass

  @staticmethod
  def reset_monitor():
    timerange = pd.date_range(start=dt.now().strftime('%Y%m%d'),
                              end=(dt.now() + timedelta(days=1)).strftime('%Y%m%d'),
                              freq='min')
    rand_data = []
    value = 0
    for _ in range(len(timerange)):
      value = np.abs(value + random.random() * 21 - 10)
      rand_data.append(value)
      Realtime_Monitor.data = pd.Series(index=timerange, data=rand_data)

  @staticmethod
  def get_current_data():
    Realtime_Monitor.update_data()
    # xdata = Realtime_Monitor.data.reset_index()['index'].astype('str').tolist()
    xdata = Realtime_Monitor.data.reset_index()['index'].astype('str').apply(lambda x: x.split()[1]).tolist()
    ydata = Realtime_Monitor.data.tolist()
    return (xdata, ydata)

  @staticmethod
  def update_data():
    for _ in range(5):
      data = Realtime_Monitor.data
      value = np.abs(data[-1] + random.random() * 21 - 10)
      Realtime_Monitor.data = Realtime_Monitor.data.append(pd.Series(index=[(data.index[-1] + timedelta(minutes=5))], data=[value]))[1:]