# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TextEditor.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(584, 399)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(-1, -1, 16777, 16777))
        self.textEdit.setMouseTracking(False)
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 584, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOps = QtWidgets.QMenu(self.menubar)
        self.menuOps.setObjectName("menuOps")

        MainWindow.setMenuBar(self.menubar)

        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionSaveAs = QtWidgets.QAction(MainWindow)
        self.actionSaveAs.setObjectName("actionSaveAs")

        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSaveAs)

        self.menuOps.addAction(self.actionCut)
        self.menuOps.addAction(self.actionCopy)
        self.menuOps.addAction(self.actionPaste)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOps.menuAction())

        self.msg = QMessageBox()
        self.file = QFileDialog()

        self.filetype = None   # filetype means whether we are opening a saved file or not

        self.actionSave.triggered.connect(self.save)
        self.actionSaveAs.triggered.connect(self.prompt)
        self.actionOpen.triggered.connect(self.openFile)
        self.actionPaste.triggered.connect(self.paste)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SuperNotepad"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.menuFile.setTitle(_translate("MainWindow", "File "))
        self.menuOps.setTitle(_translate("MainWindow", "Ops"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionSaveAs.setText(_translate("MainWindow", "Save As"))
        self.actionSaveAs.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))



    def prompt(self):
        # we will show popup message box when save was triggered
        self.msg.setText("Do you want to save the file?")
        self.msg.setIcon(self.msg.Information)
        self.msg.setWindowTitle("Super Notepad")
        self.msg.setStandardButtons(self.msg.Yes | self.msg.No)
        retrived = self.msg.exec_()
        if retrived == 16384:
            self.saveAs() 
        elif retrived == 65536:
            pass


    def writer(self, filename):
        data = self.textEdit.toPlainText()
        with open(filename, 'w') as file:
           file.write(data)

    def saveAs(self):
        filename, _ = self.file.getSaveFileName()
        if (filename != ''):
            if '.txt' not in filename:
                filename = filename+'.txt'
            self.writer(filename)
            filename = os.path.basename(filename)
            filename, _ = os.path.splitext(filename)
            self.filetype = filename+' - SuperNotepad'
            MainWindow.setWindowTitle(os.path.basename(self.filetype))


    def save(self):
        def extract():
            return self.filetype.split()[0]

        if (self.filetype==None):
            self.prompt()
        else:
            filename = extract()
            self.writer(filename)


    def openFile(self):
        file_name, _ = self.file.getOpenFileName()
        data = None
        filename= os.path.basename(file_name)
        self.filetype = os.path.splitext(filename)[0]+' - SuperNotepad'
        MainWindow.setWindowTitle(self.filetype)
        try:
            with open(file_name, 'r') as file:
                data = file.read()
        except:
            pass
        finally:
            self.textEdit.setText(data)

    def paste(self):
        # if PySide2.QtGui.QClipboard.ownsClipboard():
        # a = (QtGui.QClipboard.image(mode=QClipboard.Clipboard)
        # pass




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
