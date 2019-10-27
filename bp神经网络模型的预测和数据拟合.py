###拟合旅游收入

import numpy as np

import matplotlib.pyplot as plt

from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei']

plt.rcParams['axes.unicode_minus'] = False
#定义x、y散点坐标

x = [-3,-0.5,8,15,22,27.5,28,27,21,13,5.5,-2.5]

x = np.array(x)

print('温度 is :\n',x)

num = [40852,55877.9,47812.8,74831,80043.2,77446.8,84037.4,102784.6,74605.9,97029.6,58715,76539.2]

y = np.array(num)

print('原始数据 is :\n',y)

#用11次多项式拟合

f1 = np.polyfit(x, y, 11)

print('拟合误差值 is :\n',f1)
p1 = np.poly1d(f1)

print('拟合函数方程式 is :\n',p1)
#也可使用yvals=np.polyval(f1, x)

yvals = p1(x) #拟合y值

print('拟和预测数值 is :\n',yvals)

#绘图
plot1 = plt.plot(x, y, 's',label='原始数据')

plot2 = plt.plot(x, yvals, 'r',label='拟合预测数据')

plt.xlabel('气温')

plt.ylabel('收入（万元）')

plt.legend(loc=4) #指定legend的位置右下角

plt.title('2018年北京市旅游收入拟合数据')

plt.show()


