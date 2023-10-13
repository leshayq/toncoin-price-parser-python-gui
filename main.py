from setupUI import *
from PyQt6 import QtCore, QtGui, QtWidgets
import sys, os


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    exit_code = app.exec()
    sys.exit(exit_code)
