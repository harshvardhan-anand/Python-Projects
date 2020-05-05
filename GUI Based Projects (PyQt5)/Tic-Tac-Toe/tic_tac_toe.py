# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tictactoe.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from itertools import combinations, permutations
import numpy as np


class Ui_MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(571, 448)
        MainWindow.setStyleSheet("background-color: rgb(17, 255, 176);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.p6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p6.sizePolicy().hasHeightForWidth())
        self.p6.setSizePolicy(sizePolicy)
        self.p6.setStyleSheet("background-color: rgb(254, 255, 142);")
        self.p6.setText("")
        self.p6.setObjectName("p6")
        self.gridLayout.addWidget(self.p6, 2, 2, 1, 1)
        self.p2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p2.sizePolicy().hasHeightForWidth())
        self.p2.setSizePolicy(sizePolicy)
        self.p2.setStyleSheet("background-color: rgb(254, 255, 142);")
        self.p2.setText("")
        self.p2.setObjectName("p2")
        self.gridLayout.addWidget(self.p2, 1, 1, 1, 1)
        self.p3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p3.sizePolicy().hasHeightForWidth())
        self.p3.setSizePolicy(sizePolicy)
        self.p3.setStyleSheet("background-color: rgb(254, 255, 142);")
        self.p3.setText("")
        self.p3.setObjectName("p3")
        self.gridLayout.addWidget(self.p3, 1, 2, 1, 1)
        self.p5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p5.sizePolicy().hasHeightForWidth())
        self.p5.setSizePolicy(sizePolicy)
        self.p5.setStyleSheet("background-color: rgb(254, 255, 142);")
        self.p5.setText("")
        self.p5.setObjectName("p5")
        self.gridLayout.addWidget(self.p5, 2, 1, 1, 1)
        self.p7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p7.sizePolicy().hasHeightForWidth())
        self.p7.setSizePolicy(sizePolicy)
        self.p7.setStyleSheet("background-color: rgb(254, 255, 142);")
        self.p7.setText("")
        self.p7.setObjectName("p7")
        self.gridLayout.addWidget(self.p7, 3, 0, 1, 1)
        self.p8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p8.sizePolicy().hasHeightForWidth())
        self.p8.setSizePolicy(sizePolicy)
        self.p8.setStyleSheet("background-color: rgb(254, 255, 142);")
        self.p8.setText("")
        self.p8.setObjectName("p8")
        self.gridLayout.addWidget(self.p8, 3, 1, 1, 1)
        self.p1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p1.sizePolicy().hasHeightForWidth())
        self.p1.setSizePolicy(sizePolicy)
        self.p1.setStyleSheet("background-color: rgb(254, 255, 142);")
        self.p1.setText("")
        self.p1.setObjectName("p1")
        self.gridLayout.addWidget(self.p1, 1, 0, 1, 1)
        self.p4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p4.sizePolicy().hasHeightForWidth())
        self.p4.setSizePolicy(sizePolicy)
        self.p4.setStyleSheet("background-color: rgb(254, 255, 142);")
        self.p4.setText("")
        self.p4.setObjectName("p4")
        self.gridLayout.addWidget(self.p4, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit1.setObjectName("lineEdit1")
        self.horizontalLayout.addWidget(self.lineEdit1)
        self.lineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit2.setObjectName("lineEdit2")
        self.horizontalLayout.addWidget(self.lineEdit2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 3)
        self.p9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p9.sizePolicy().hasHeightForWidth())
        self.p9.setSizePolicy(sizePolicy)
        self.p9.setStyleSheet("background-color: rgb(254, 255, 142);")
        self.p9.setText("")
        self.p9.setObjectName("p9")
        self.gridLayout.addWidget(self.p9, 3, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.button_pressed()
        self.flag=0
        self.reset()
        self.all_button = ['p1','p2','p3','p4','p5','p6','p7','p8','p9']
        self.get_all_possible()
        self.setStatus()
        self.winx = self.wino = 0

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit1.setText("Player 1 (X) = 0")
        self.lineEdit2.setText("Player 2 (O) = 0")
        self.lineEdit1.setEnabled(False)
        self.lineEdit2.setEnabled(False)
        self.lineEdit1.setStyleSheet("QLineEdit:disabled{color:black}")
        self.lineEdit2.setStyleSheet("QLineEdit:disabled{color:black}")

    def get_all_possible(self):
        g1 = [('p1', 'p2', 'p3'),
              ('p3', 'p6', 'p9'),
              ('p7', 'p8', 'p9'),
              ('p1', 'p4', 'p7'),
              ('p1', 'p5', 'p9'),
              ('p3', 'p5', 'p7'),
              ('p4', 'p5', 'p6'),
              ('p1', 'p4', 'p7'),
              ('p2', 'p5', 'p8')]
        all_elements = []
        for i in g1:
            all_elements.append(list(permutations(i)))
        all_e = []
        for i in all_elements:
            for j in i:
                all_e.append(j)
        self.all_e = set(all_e)

    def find_ans(self, iterable):
        outcome = (list(combinations(iterable, 3)))
        found = any([x for x in outcome if x in self.all_e])
        print(outcome)
        return found

    def loose_win(self):
        # print(self.winx)
        if (len(self.x)>=3) or (len(self.o)>=3):
            if self.find_ans(self.x):
                self.winx+=1
                self.lineEdit1.setText("Player 1 (X) = "+str(self.winx))
            else:
                if self.find_ans(self.o):
                    self.wino+=1
                    self.lineEdit2.setText("Player 2 (O) = "+str(self.wino))

            if self.winx>self.wino:
                for i in self.all_button:
                    button = eval("self."+i)
                    button.setEnabled(False)
                text = "Player 1 won!!!"
                self.show_msg(text)
            elif self.wino>self.winx:
                for i in self.all_button:
                    button = eval("self."+i)
                    button.setEnabled(False)
                text = "Player 2 won!!!"
                self.show_msg(text)
            else:
                text = "Its a draw :|"
                self.show_msg(text)

    def show_msg(self, text):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText(text)
        msg.setWindowTitle("Game End")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()
        self.flag = 1
        self.reset()



    def reset(self):
        self.status=0
        self.x = []
        self.o = []
        if self.flag:
            for i in self.all_button:
                button = eval("self."+i)
                button.setEnabled(True)
                button.setText("")
                button.setStyleSheet("background-color: rgb(254, 255, 142);")


    def button_pressed(self):
        self.p1.clicked.connect(self.action)
        self.p2.clicked.connect(self.action)
        self.p3.clicked.connect(self.action)
        self.p4.clicked.connect(self.action)
        self.p5.clicked.connect(self.action)
        self.p6.clicked.connect(self.action)
        self.p7.clicked.connect(self.action)
        self.p8.clicked.connect(self.action)
        self.p9.clicked.connect(self.action)

    def setStatus(self):
        if self.status%2==0:
            self.statusBar.showMessage("Player 1's chance")
        else:
            self.statusBar.showMessage("Player 2's chance")


    def action(self):
        # print(type(clicked_button.objectName()))
        # print(eval("self."+clicked_button))
        # Alternatively changing "X" and "O"

        clicked_button = self.sender().objectName()
        button = eval("self."+clicked_button)
        button.setEnabled(False)

        if (self.status%2)==0:
            button.setText("X")
            button.setStyleSheet('''QPushButton:disabled{color:black;font-size:50px;background-color:rgb(254, 255, 142);
                                     font-weight:bold}''')
            self.x.append(clicked_button)
        else:
            button = eval("self."+clicked_button)
            button.setText("O")
            button.setStyleSheet('''QPushButton:disabled{color:black;font-size:50px;background-color:rgb(254, 255, 142);
                                     font-weight:bold}''')
            self.o.append(clicked_button)
        # print(self.x)
        self.status+=1
        self.setStatus()
        self.loose_win()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
