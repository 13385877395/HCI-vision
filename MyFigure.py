#-*-coding:utf-8-*-
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import numpy as np
from  readdemo import get_data

import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class MyFigure(FigureCanvas):
    def __init__(self, width = 5, height = 4, dpi = 100):
        #创建一个figure
        self.fig = Figure(figsize=(width, height), dpi = dpi)
        #在父类中激活figure
        super(MyFigure, self).__init__(self.fig)
        #创建子图
        self.axes = self.fig.add_subplot(111)
        x = [1,2,3]
        y = [2,2,3]
        # self.plot()


    def plot(self):
        # test_day[x][y]可以查看第x天，受试者y的信息
        testers, testers_day = get_data()
    
        days = [index for index, value in enumerate(testers_day)]#获取天数list
        val_day = []#某一天
        day_val_dic = {}#该字典记录，对应天数的所有受试者的反应时间（在一个list里面）
        for day in days:#将对应天数的众多受试者全部加入一个list,
            #每天的n名受试者以字典的形式存储，如：day01 = {A01:[[A01测的第一组数据], [A01测的第二组数据]]}
            result_day = testers_day[day]#result_day为上述字典
            dict_keys = list(result_day.keys())
            #对每个受试者进行遍历
            for key in dict_keys:
                # 对受试者的不同组进行遍历
                for group in result_day[key]:#gourp为对应key的value，这个value为一个list。
                    # 对受试者的具体组进行遍历
                    for val in group:
                        val_day.append(val)
            day_val_dic[day] = val_day

        x = []#x轴是天数
        y = []#y轴是反应时间

        x1 = [2,4,5]
        y1 = [2,4,5]
        print(list(day_val_dic.keys()))
        for day in list(day_val_dic.keys()):
            for val in day_val_dic[day]:
                x.append(day)
                y.append(val)

        # self.axes.plot(x, y, color='green', marker='o', linestyle='dashed',
        #             linewidth=1, markersize=3)
        self.axes.plot(x, y, "bo-" , x1, y1,  "go")

        # plt.plot(x, y)
        # plt.show()

if __name__ == "__main__":
    F = MyFigure()
    # print(dir(FigureCanvas))