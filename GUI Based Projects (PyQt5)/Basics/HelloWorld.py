from qtpy.QtWidgets import QApplication, QLabel

# initialise application
app = QApplication([]) 

# create label object
label = QLabel('Hello World')
label.show()

app.exec_()