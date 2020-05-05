import sys
import PyQt5.QtWidgets as qw

def clicked():
    # this function will be called when mouse is clicked
    print('clicked')

def window():
    # application object
    app = qw.QApplication([])

    # application window
    win = qw.QMainWindow()  # --

    # set windows location. The position is the location of top left corner of the window.
    # (x_position, y_position, width, height)
    win.setGeometry(200, 200, 200, 200)

    # setting window title
    win.setWindowTitle("I am window title")

    # # set label to the window
    # label = qw.QLabel(win)
    # label.setText("This is a label")
    # label.move(50, 60)  # (x, y) from top left corner

    # setting button to the window
    button = qw.QPushButton(win)
    button.setText("Click me")
    button.clicked.connect(clicked)
    # showing application window
    win.show() 
    # so called clean exit for the below line otherwise we can use app.exec_() also.
    sys.exit(app.exec_())


window()
