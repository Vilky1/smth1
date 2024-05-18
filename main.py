from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import time
from PyQt5.uic import loadUiType

ui,_ = loadUiType('main.ui')

class MainApp(QMainWindow , ui):
    def __init__(self , parent=None):
        super(MainApp , self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.loopyloop)
    def loopyloop(self):
        for i in range(10):
            print(i)
            time.sleep(1)


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()

