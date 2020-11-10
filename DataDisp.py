import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication,QMainWindow,QGridLayout
from PyQt5.QtCore import QTimer
import sys,time
import numpy as np

from CogPara import Ui_MainWindow
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.lines import Line2D
import matplotlib
import matplotlib.cbook as cbook

# fig = plt.figure()#获取一个对象

# ax = fig.add_subplot(111)#获取一个轴

# ax.set(xlim = [0.5, 1], ylim = [-1, 8], title = "test", ylabel = 'Y', xlabeL = 'X')#设置坐标系的参数

# plt.show()
class ImgDisp(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__()
        self.setupUi(Ui_MainWindow)
        self.set_widgit()

    def set_widgit(self):
        self.LineCanvas()

    def LineCanvas(self):
        self.LineFigure = Figure_Canvas()#实例一个画布对象
        self.LineFigureLayout = QGridLayout(self.LineDisplayGB)#
        self.LineFigureLayout.addWidget(self.LineFigure)#将linefigure这个组件添加到容器里面
        self.LineFigure.ax.set_xlim(-4, 4)#设置坐标轴的范围
        self.LineFigure.ax.set_ylim(-1, 1)
        self.line = Line2D(self.x, self.z)#设置一根线条
        self.LineFigure.ax.add_line(self.line)#将线条放到轴里面




class Figure_Canvas(FigureCanvas):#一个画布类，有一个轴
    def __init__(self,parent=None,width=3.9,height=2.7,dpi=100):
        self.fig=Figure(figsize=(width,height),dpi=100)
        super(Figure_Canvas,self).__init__(self.fig)
        self.ax=self.fig.add_subplot(111)


# plt.plot([1, 2, 3, 4, 7], [10, 20, 25, 30, 6], color='lightblue', linewidth=2)
# plt.xlim(0.5, 4.5)
# plt.show()

if __name__=='__main__': 
    app=QApplication(sys.argv)
    ui=ImgDisp()
 
    ui.show()
    sys.exit(app.exec_())