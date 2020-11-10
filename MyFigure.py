#-*-coding:utf-8-*-
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import numpy as np


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

        #画图
        def plot(self):
            # self.axes0 = self.fig.add_subplot(111)
            t = np.arange(0.0, 3.0, 0.01)
            s = np.sin(2 * np.pi * t)
            self.axes.plot(t, s)


