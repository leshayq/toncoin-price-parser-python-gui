from PyQt6 import QtCore, QtGui, QtWidgets
from parse import parse

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(481, 344)
        MainWindow.setFixedSize(481, 344)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.994, y2:0.017, stop:0 rgba(46, 118, 243, 255), stop:0.738636 rgba(31, 111, 162, 255))")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, -290, 531, 741))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("ton.png"))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 50, 91, 31))

        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)

        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(False)
        self.label_2.setOpenExternalLinks(False)
        self.label_2.setObjectName("label_2")

        self.price_line = QtWidgets.QLineEdit(self.centralwidget)
        self.price_line.setGeometry(QtCore.QRect(110, 90, 321, 41))
        self.price_line.setObjectName("lineEdit")
        self.price_line.setAutoFillBackground(False)
        self.price_line.setStyleSheet("color: white;")
        self.price_line.setText('')

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.price_line.setFont(font)

        self.get_button = QtWidgets.QPushButton(self.centralwidget)
        self.get_button.setGeometry(QtCore.QRect(110, 150, 211, 41))
        self.get_button.setObjectName("pushButton")
        self.get_button.setText('Get')
        self.get_button.clicked.connect(self.button_clicked)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 210, 101, 21))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def button_clicked(self):
        self.price_line.setText(parse())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TonCoinTracker"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Toncoin</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">by leshayq</span></p></body></html>"))