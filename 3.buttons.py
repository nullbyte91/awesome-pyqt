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
        self.text = QLabel("Hello world", self)

        # Create a Enter button
        enterButton = QPushButton("Enter", self)

        # Create a Exit button
        exitButton = QPushButton("Exit", self)

        # Set Text X, Y Position
        self.text.move(160, 50)

        # Set Enter Button X, Y
        enterButton.move(100, 80)

        # Set Exit Button X, Y
        exitButton.move(200, 80)
        
        # Enter Button connect/Action
        enterButton.clicked.connect(self.enterFun)

        # Exit Button connect/Action
        exitButton.clicked.connect(self.exitFun)
        
        # show
        self.show()

    def enterFun(self):
        self.text.setText("You clicked Enter")
        self.text.resize(150, 20)

    def exitFun(self):
        self.text.setText("You clicked Exit")
        self.text.resize(150, 20)

# Main method
def main():
    App = QApplication(sys.argv)
    window = Window() 
    sys.exit(App.exec_())

if __name__ == "__main__":
    main()
        