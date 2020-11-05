import sys
from  readdemo import get_data

from CogPara import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox,QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setupUi(self)
        self.setWindowTitle('视觉反应分析 ')
        print(get_data())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
