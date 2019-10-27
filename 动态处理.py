#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:luoguan
# datetime:2019/9/18 22:39
# software: Pycharm 2019.1 python 3.5.4
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

import numpy as np

import matplotlib.pyplot as plt

import matplotlib.dates as mdate

import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签

plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

date = pd.date_range('2018-09-03', '2018-09-06')

y1 = [0.9143, 0.9293, 0.9348, 0.9327]

y2 = [0.9143, 0.9294, 0.9348, 0.9327]

fig = plt.figure(figsize=(15, 10))

ax = fig.add_subplot(1, 1, 1)

ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y%m%d'))  # 设置时间标签显示格式

ax.xaxis.set_major_locator(mdate.DayLocator())

ax.set_title("y plot")

ax.plot(date, y1, 'go-', label=u'这是y1')

ax.plot(date, y2, 'yo-', label=u'这是y2')

plt.xticks(rotation=45)  # 旋转45度显示

legend = ax.legend(loc='lower center', shadow=False)













