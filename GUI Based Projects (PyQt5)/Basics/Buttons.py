from qtpy.QtWidgets import QApplication, QLabel, QPushButton

# create application
app = QApplication([])

button = QPushButton('I am a Button')

# callback funciton
def trigger(event):
    print("Printed when Triggered")

# connecting to the Callback function 
button.clicked.connect(trigger)
# lets show the button
button.show()

# run event loop
app.exec_()