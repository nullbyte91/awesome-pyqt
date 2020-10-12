import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font = QFont("Times")

class Window(QWidget): 

    def __init__(self):

        super().__init__()

        # Set the window size
        self.setGeometry(250, 150, 500, 500)

        # Set the window title
        self.setWindowTitle("Window")

        self.UI()

    def UI(self):
        button = QPushButton("Click Me!", self)
        button.setFont(font)
        button.move(200, 150)
        button.clicked.connect(self.messageBox)

        # show
        self.show()

    def messageBox(self):
        mbox = QMessageBox.question(self, "Warning !!!!", "Are you sure exit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if QMessageBox.Yes:
            sys.exit()

# Main method
def main():
    App = QApplication(sys.argv)
    window = Window() 
    sys.exit(App.exec_())

if __name__ == "__main__":
    main()
        