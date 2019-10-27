#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:luoguan
# datetime:2019/9/18 20:29
# software: Pycharm 2019.1 python 3.5.4
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_gaussian_quantiles

#生成二维正态分布，生成的数据分为两类，500个样本，2个样本特征，协方差系数为2
X1,y1=make_gaussian_quantiles(cov=2.0,n_samples=500,
                              n_features=2,n_classes=2,
                              random_state=1)

#生成二维正态分布，生成的数据分为两类，500个样本，2个样本特征，协方差系数为1.5
X2,y2=make_gaussian_quantiles(mean=(3,3),cov=1.5,
                              n_samples=500,n_features=2,
                              n_classes=2,random_state=1)
#将两组数据合为一组
X=np.concatenate((X1,X2))
y=np.concatenate((y1,-y2+1))

#绘画生成的数据点
plt.figure()
plt.scatter(X[:,0],X[:,1],marker='o',c=y)
plt.show()
# 训练数据
clf=AdaBoostClassifier(DecisionTreeClassifier(
                       max_depth=2,min_samples_split=20,
                       min_samples_leaf=5),algorithm="SAMME",
                       n_estimators=200,learning_rate=0.8)
clf.fit(X,y)

#将训练结果绘画出来
plt.figure()
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02))
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
cs = plt.contourf(xx, yy, Z, cmap=plt.cm.Paired)
plt.scatter(X[:, 0], X[:, 1], marker='o', c=y)
plt.show()

#训练模型的得分
print(clf.score(X,y))
#0.913333333333
