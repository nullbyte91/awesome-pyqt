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
        self.setWindowTitle("SpinBox")

        self.UI()

    def UI(self):
        self.spinBox = QSpinBox(self)
        self.spinBox.move(150, 100)
        self.spinBox.setFont(font)
        #self.spinBox.setMinimum(25)
        #self.spinBox.setMaximum(25)
        self.spinBox.setRange(0, 200)
        self.spinBox.valueChanged.connect(self.getVal)

        self.show()

    def getVal(self):
        value = self.spinBox.value()
        print(value)

# Main method
def main():
    App = QApplication(sys.argv)
    window = Window() 
    sys.exit(App.exec_())

if __name__ == "__main__":
    main()
        