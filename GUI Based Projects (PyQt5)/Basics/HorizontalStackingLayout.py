from qtpy.QtWidgets import *

app = QApplication([])

# Create label and button
label1 = QLabel('Label 1')
label2 = QLabel('Label 2')
label3 = QLabel('Label 3')
button = QPushButton('Press me!')

# horizontal stacking
layout = QHBoxLayout()
layout.addWidget(label1)
layout.addWidget(label2)
layout.addWidget(label3)
layout.addWidget(button)

widget = QWidget()
widget.setLayout(layout)
widget.show()

app.exec_()