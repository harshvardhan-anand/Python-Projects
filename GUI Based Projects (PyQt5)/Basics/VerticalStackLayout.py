# QVBoxLayout is used to stack widgets vertically stacked

import qtpy.QtWidgets as qw

# create application
app = qw.QApplication([])

# create and show label
label = qw.QLabel("I am a label")
label.show()

# create and show button
button = qw.QPushButton("Click Me")
def callback(event):
    print("I am from callback")
button.clicked.connect(callback)
button.show()

# create layout and widgets
layout = qw.QVBoxLayout()
# label is placed on top of button
layout.addWidget(label)
layout.addWidget(button)
# Layout is not a widget so at first we need to set the layout to the parent widget
widget = qw.QWidget()
widget.setLayout(layout)
# now show the widget
widget.show()

# event loop
app.exec_()