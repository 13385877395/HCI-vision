import sys

from CogPara import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox,QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from MyFigure import MyFigure
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setupUi(self)
        self.setWindowTitle('视觉反应分析 ')

        #实例化一个figure
        self.F = MyFigure()
        self.setCentralWidget(self.F)  #把figure放到widget里面
        self.plotcos()

    #一个测试用的图像
    def plotcos(self):
        t = np.arange(0.0, 5.0, 0.01)
        s = np.cos(2 * np.pi * t)
        self.F.axes.plot(t, s)
        self.F.fig.suptitle("cos")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
