# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(417, 510)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 401, 99))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.calculation = QtWidgets.QLineEdit(self.layoutWidget)
        self.calculation.setObjectName("calculation")
        self.verticalLayout.addWidget(self.calculation)
        self.output = QtWidgets.QTextEdit(self.layoutWidget)
        self.output.setEnabled(True)
        self.output.setObjectName("output")
        self.verticalLayout.addWidget(self.output)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(11, 115, 396, 381))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.one = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.one.sizePolicy().hasHeightForWidth())
        self.one.setSizePolicy(sizePolicy)
        self.one.setObjectName("one")
        self.gridLayout_6.addWidget(self.one, 3, 2, 1, 1)
        self.nine = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nine.sizePolicy().hasHeightForWidth())
        self.nine.setSizePolicy(sizePolicy)
        self.nine.setObjectName("nine")
        self.gridLayout_6.addWidget(self.nine, 1, 0, 1, 1)
        self.zero = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zero.sizePolicy().hasHeightForWidth())
        self.zero.setSizePolicy(sizePolicy)
        self.zero.setStyleSheet("")
        self.zero.setObjectName("zero")
        self.gridLayout_6.addWidget(self.zero, 0, 0, 1, 1)
        self.seven = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.seven.sizePolicy().hasHeightForWidth())
        self.seven.setSizePolicy(sizePolicy)
        self.seven.setMouseTracking(True)
        self.seven.setObjectName("seven")
        self.gridLayout_6.addWidget(self.seven, 1, 2, 1, 1)
        self.exponent = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exponent.sizePolicy().hasHeightForWidth())
        self.exponent.setSizePolicy(sizePolicy)
        self.exponent.setMinimumSize(QtCore.QSize(94, 0))
        self.exponent.setMaximumSize(QtCore.QSize(94, 16777215))
        self.exponent.setObjectName("exponent")
        self.gridLayout_6.addWidget(self.exponent, 2, 3, 1, 1)
        self.divide = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.divide.sizePolicy().hasHeightForWidth())
        self.divide.setSizePolicy(sizePolicy)
        self.divide.setMinimumSize(QtCore.QSize(94, 0))
        self.divide.setMaximumSize(QtCore.QSize(94, 16777215))
        self.divide.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.divide.setMouseTracking(False)
        self.divide.setTabletTracking(False)
        self.divide.setAcceptDrops(False)
        self.divide.setAutoFillBackground(False)
        self.divide.setStyleSheet("QPushButton:hover{background-color: rgb(255, 74, 29);}")
        self.divide.setObjectName("divide")
        self.gridLayout_6.addWidget(self.divide, 1, 3, 1, 1)
        self.multiply = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.multiply.sizePolicy().hasHeightForWidth())
        self.multiply.setSizePolicy(sizePolicy)
        self.multiply.setMinimumSize(QtCore.QSize(94, 0))
        self.multiply.setMaximumSize(QtCore.QSize(94, 16777215))
        self.multiply.setObjectName("multiply")
        self.gridLayout_6.addWidget(self.multiply, 0, 3, 1, 1)
        self.equal = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.equal.sizePolicy().hasHeightForWidth())
        self.equal.setSizePolicy(sizePolicy)
        self.equal.setMinimumSize(QtCore.QSize(94, 0))
        self.equal.setMaximumSize(QtCore.QSize(94, 16777215))
        self.equal.setObjectName("equal")
        self.gridLayout_6.addWidget(self.equal, 3, 3, 1, 1)
        self.six = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.six.sizePolicy().hasHeightForWidth())
        self.six.setSizePolicy(sizePolicy)
        self.six.setObjectName("six")
        self.gridLayout_6.addWidget(self.six, 2, 0, 1, 1)
        self.five = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.five.sizePolicy().hasHeightForWidth())
        self.five.setSizePolicy(sizePolicy)
        self.five.setObjectName("five")
        self.gridLayout_6.addWidget(self.five, 2, 1, 1, 1)
        self.three = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.three.sizePolicy().hasHeightForWidth())
        self.three.setSizePolicy(sizePolicy)
        self.three.setMinimumSize(QtCore.QSize(94, 0))
        self.three.setMaximumSize(QtCore.QSize(94, 16777215))
        self.three.setObjectName("three")
        self.gridLayout_6.addWidget(self.three, 3, 0, 1, 1)
        self.four = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.four.sizePolicy().hasHeightForWidth())
        self.four.setSizePolicy(sizePolicy)
        self.four.setObjectName("four")
        self.gridLayout_6.addWidget(self.four, 2, 2, 1, 1)
        self.two = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.two.sizePolicy().hasHeightForWidth())
        self.two.setSizePolicy(sizePolicy)
        self.two.setMinimumSize(QtCore.QSize(94, 0))
        self.two.setMaximumSize(QtCore.QSize(94, 16777215))
        self.two.setObjectName("two")
        self.gridLayout_6.addWidget(self.two, 3, 1, 1, 1)
        self.minus = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minus.sizePolicy().hasHeightForWidth())
        self.minus.setSizePolicy(sizePolicy)
        self.minus.setMinimumSize(QtCore.QSize(94, 0))
        self.minus.setMaximumSize(QtCore.QSize(94, 16777215))
        self.minus.setObjectName("minus")
        self.gridLayout_6.addWidget(self.minus, 0, 2, 1, 1)
        self.eight = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eight.sizePolicy().hasHeightForWidth())
        self.eight.setSizePolicy(sizePolicy)
        self.eight.setObjectName("eight")
        self.gridLayout_6.addWidget(self.eight, 1, 1, 1, 1)
        self.plus = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plus.sizePolicy().hasHeightForWidth())
        self.plus.setSizePolicy(sizePolicy)
        self.plus.setMinimumSize(QtCore.QSize(94, 0))
        self.plus.setMaximumSize(QtCore.QSize(94, 16777215))
        self.plus.setMouseTracking(True)
        self.plus.setObjectName("plus")
        self.gridLayout_6.addWidget(self.plus, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 422, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.button_pressed()
        self.centralwidget.keyPressEvent = self.key_pressed

    def key_pressed(self, event):
        if event.key()==QtCore.Qt.Key_Escape:
            self.calculation.clear()
            self.output.clear()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.one.setText(_translate("MainWindow", "1"))
        self.nine.setText(_translate("MainWindow", "9"))
        self.zero.setText(_translate("MainWindow", "0"))
        self.seven.setText(_translate("MainWindow", "7"))
        self.exponent.setText(_translate("MainWindow", "e"))
        self.divide.setText(_translate("MainWindow", "/"))
        self.multiply.setText(_translate("MainWindow", "*"))
        self.equal.setText(_translate("MainWindow", "="))
        self.six.setText(_translate("MainWindow", "6"))
        self.five.setText(_translate("MainWindow", "5"))
        self.three.setText(_translate("MainWindow", "3"))
        self.four.setText(_translate("MainWindow", "4"))
        self.two.setText(_translate("MainWindow", "2"))
        self.minus.setText(_translate("MainWindow", "-"))
        self.eight.setText(_translate("MainWindow", "8"))
        self.plus.setText(_translate("MainWindow", "+"))

        self.one.setStyleSheet('''QPushButton{font-size:30px;
                               font-weight:bold;}
                               QPushButton:hover{background-color: rgb(0, 152, 255)}''')
        self.two.setStyleSheet('''QPushButton{font-size:30px;
                               font-weight:bold;}
                               QPushButton:hover{background-color: rgb(0, 152, 255)}''')
        self.three.setStyleSheet('''QPushButton{font-size:30px;
                               font-weight:bold;}
                               QPushButton:hover{background-color: rgb(0, 152, 255)}''')
        self.four.setStyleSheet('''QPushButton{font-size:30px;
                               font-weight:bold;}
                               QPushButton:hover{background-color: rgb(0, 152, 255)}''')
        self.five.setStyleSheet('''QPushButton{font-size:30px;
                               font-weight:bold;}
                               QPushButton:hover{background-color: rgb(0, 152, 255)}''')
        self.six.setStyleSheet('''QPushButton{font-size:30px;
                               font-weight:bold;}
                               QPushButton:hover{background-color: rgb(0, 152, 255)}''')
        self.seven.setStyleSheet('''QPushButton{font-size:30px;
                               font-weight:bold;}
                               QPushButton:hover{background-color: rgb(0, 152, 255)}''')
        self.eight.setStyleSheet('''QPushButton{font-size:30px;
                               font-weight:bold;}
                               QPushButton:hover{background-color: rgb(0, 152, 255)}''')
        self.nine.setStyleSheet('''QPushButton{font-size:30px;
                               font-weight:bold;}
                               QPushButton:hover{background-color: rgb(0, 152, 255)}''')
        self.zero.setStyleSheet('''QPushButton{font-size:30px;
                               font-weight:bold;}
                               QPushButton:hover{background-color: rgb(0, 152, 255)}''')
        self.multiply.setStyleSheet('''QPushButton{font-size:30px;
                               font-weight:bold;}
                               QPushButton:hover{background-color: rgb(0, 152, 255)}''')
        self.divide.setStyleSheet('''QPushButton{font-size:30px;
                               font-weight:bold;}
                               QPushButton:hover{background-color: rgb(0, 152, 255)}''')
        self.minus.setStyleSheet('''QPushButton{font-size:30px;
                               font-weight:bold;}
                               QPushButton:hover{background-color: rgb(0, 152, 255)}''')
        self.plus.setStyleSheet('''QPushButton{font-size:30px;
                               font-weight:bold;}
                               QPushButton:hover{background-color: rgb(0, 152, 255)}''')
        self.equal.setStyleSheet('''QPushButton{font-size:30px;
                               font-weight:bold;}
                               QPushButton:hover{background-color: rgb(0, 152, 255)}''')
        self.exponent.setStyleSheet('''QPushButton{font-size:30px;
                               font-weight:bold;}
                               QPushButton:hover{background-color: rgb(0, 152, 255)}''')
        self.output.setStyleSheet("QTextEdit{font-size:40px}")

    def button_pressed(self):
        self.one.clicked.connect(lambda:self.output.insertPlainText('1'))
        self.two.clicked.connect(lambda:self.output.insertPlainText('2'))
        self.three.clicked.connect(lambda:self.output.insertPlainText('3'))
        self.four.clicked.connect(lambda:self.output.insertPlainText('4'))
        self.five.clicked.connect(lambda:self.output.insertPlainText('5'))
        self.six.clicked.connect(lambda:self.output.insertPlainText('6'))
        self.seven.clicked.connect(lambda:self.output.insertPlainText('7'))
        self.eight.clicked.connect(lambda:self.output.insertPlainText('8'))
        self.nine.clicked.connect(lambda:self.output.insertPlainText('9'))
        self.zero.clicked.connect(lambda:self.output.insertPlainText('0'))
        self.plus.clicked.connect(lambda:self.output.insertPlainText('+'))
        self.minus.clicked.connect(lambda:self.output.insertPlainText('-'))
        self.multiply.clicked.connect(lambda:self.output.insertPlainText('*'))
        self.divide.clicked.connect(lambda:self.output.insertPlainText('/'))
        self.exponent.clicked.connect(lambda:self.output.insertPlainText('^'))
        self.equal.clicked.connect(self.calculate)

    def calculate(self):
        try:
            ops = self.output.toPlainText()
            ops = ops.replace('^', "**")
            res = str(eval(ops))
        except:
            self.calculation.setText("Invalid Operation")
            self.output.clear()
        else:
            self.output.setText(res)
            ops = ops.replace('**', "^")
            self.calculation.setText(ops+' =')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
