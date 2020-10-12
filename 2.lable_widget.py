import sys
from PyQt5.QtWidgets import *


class Window(QWidget): 

    def __init__(self):

        super().__init__()

        # Set the window size
        self.setGeometry(50, 50, 600, 400)

        # Set the window title
        self.setWindowTitle("Window")

        self.UI()

    def UI(self):
        # Creating a label widgets
        text = QLabel("Hello world", self)

        # show
        self.show()

# Main method
def main():
    App = QApplication(sys.argv)
    window = Window() 
    sys.exit(App.exec_())

if __name__ == "__main__":
    main()
        