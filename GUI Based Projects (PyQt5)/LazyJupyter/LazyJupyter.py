# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jn.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess as sp
import os
import time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(389, 188)
        MainWindow.setMaximumSize(QtCore.QSize(389, 188))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(9, 9, 371, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setObjectName("textBrowser")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(12, 74, 361, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.udemy = QtWidgets.QPushButton(self.layoutWidget)
        self.udemy.setObjectName("udemy")
        self.gridLayout.addWidget(self.udemy, 0, 0, 1, 1)
        self.github = QtWidgets.QPushButton(self.layoutWidget)
        self.github.setObjectName("github")
        self.gridLayout.addWidget(self.github, 1, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.off = QtWidgets.QPushButton(self.layoutWidget)
        self.off.setObjectName("off")
        self.horizontalLayout.addWidget(self.off)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 389, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.cmd = "jupyter notebook"
        self.udemy.clicked.connect(self.udemy_click)
        self.github.clicked.connect(self.master_click)
        self.off.clicked.connect(self.power_off)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lazy Jupyter"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#fd6005;\">Jupyter Notebook</span></p></body></html>"))
        self.udemy.setText(_translate("MainWindow", " Udemy Resources"))
        self.github.setText(_translate("MainWindow", "Master Location"))
        self.off.setText(_translate("MainWindow", "Power Off"))
        self.off.setStyleSheet("QPushButton:hover{background-color:red}")
        self.udemy.setStyleSheet("QPushButton:hover{background-color:lightgreen}")
        self.github.setStyleSheet("QPushButton:hover{background-color:lightgreen}")

    def udemy_click(self):
        sp.Popen("jupyter notebook",
                cwd='E:\PROJ.RC\__operational files__\yt vdo\youtube\_Resources_')
        self.udemy.setStyleSheet('''QPushButton{background-color:lightgreen;
                                 font-weight:bold;}''')

    def master_click(self):
        sp.Popen(self.cmd,cwd='E:\PROJ.RC\__operational files__')
        self.github.setStyleSheet('''QPushButton{background-color:lightgreen;
                                 font-weight:bold;}''')

    def power_off(self):
        self.udemy.setStyleSheet("")
        os.system("taskkill /f /im python.exe")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
