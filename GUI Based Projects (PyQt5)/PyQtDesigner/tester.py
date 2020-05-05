from PyQt5.QtWidgets import *


def call():
	q = QFileDialog()
	a, b = q.getSaveFileName()
	# print(q.getSaveFileName())
	with open(a+'.txt', 'w') as f:
		f.write('sdfdsfsf')

app = QApplication([])
win = QMainWindow()
# le  = QLineEdit(win)
b = QPushButton(win)
b.clicked.connect(call)
win.show()

app.exec_()