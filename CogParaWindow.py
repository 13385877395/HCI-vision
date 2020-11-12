import sys
import threading
from subprocess import Popen, PIPE

from CogPara import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox,QLineEdit
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QIcon
from MyFigure import MyFigure, QThread
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QFileDialog

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setupUi(self)
        self.setWindowTitle('视觉反应分析 ')
        #实例化一个figure
        self.F = MyFigure()
        self.verticalLayout.addWidget(self.F)  #把figure放到widget里面
        self.F.plot()
        self.openModel.clicked.connect(self.OpenModel)
        self.runModel.clicked.connect(self.RunModel)

    def OpenModel(self):
        # my_file_path = dialog.getOpenFileName(self, "打开文件", "/", "*.txt")
        my_file_path = QFileDialog.getOpenFileName( self, '选择文件', '', 'Excel files(*.txt , *.py)' )
        self.model_path = my_file_path[0]
        # 路径不能包含中文
        self.textBrowser.clear()
        self.textBrowser.append( "打开文件："+ self.model_path)
    def RunModel(self, now):
        try:
            print(self.model_path)
            self.run_process = RunModelHandler( self.model_path )
            self.run_process.trigger.connect( self.call_backlog )
            self.run_process.start()
        except:
            # 提式加载文件
            self.textBrowser.clear()
            self.textBrowser.append( "请先打开模型文件" )
            pass
    def call_backlog(self, str):
        self.textBrowser.append(str)
        self.cursor = self.textBrowser.textCursor()
        self.textBrowser.moveCursor( self.cursor.End )  # 光标移到最后，这样就会自动显示出来
        QtWidgets.QApplication.processEvents()  # 一定加上这个功能，不然有卡顿

class RunModelHandler( QThread ):
    #  通过类成员对象定义信号对象
    trigger = pyqtSignal( str )

    def __init__(self, model_path):
        super( RunModelHandler, self ).__init__()
        self.model_path = model_path
        self.Flag = True
    def run(self):
        cmd = r'python ' + self.model_path
        """"输出重定向"""
        savedStdout = sys.stdout
        sys.stdout = self
        p = Popen( cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True )
        self.thr = threading.Thread( target=self.listenTo, args=[p] )
        self.thr.start()
        sys.stdout = savedStdout

    def listenTo(self, proc):
        while self.Flag:
            savedStdout = sys.stdout
            sys.stdout = self
            srv_out = proc.stdout.readline()
            if (srv_out):
                sys.stdout.write( srv_out.decode( 'utf-8' ) )
            if (proc.poll() == 0):
                sys.stdout = savedStdout
                exit()
            sys.stdout = savedStdout



    def write(self, out_stream):
        """ :param out_stream: :return: """
        self.trigger.emit( out_stream )

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
