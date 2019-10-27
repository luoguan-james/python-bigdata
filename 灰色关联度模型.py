#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:luoguan
# datetime:2019/9/19 3:32
# software: Pycharm 2019.1 python 3.5.4
from pylab import *
import numpy as np
import matplotlib.pylab as plt
import pandas as pd
mpl.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
x51=[1901,2160,2119,3078,2996,2666,3101,3648,2889,3557,2079,1500]
x41=[3.4,6.5,4.1,2.2,1.7,2.4,2.3,4.1,3.3,1.1,2.8,4.3]
year = np.arange(1,13,1)
plt.subplot(2,1,1)
plt.plot(year,x51,label="旅游人数随时间的变化曲线")
plt.legend()
plt.subplot(2,1,2)
plt.plot(year,x41,color="red",label="风效指数随时间的变化曲线")
plt.legend()
plt.show()