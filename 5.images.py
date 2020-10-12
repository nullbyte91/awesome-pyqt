import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

class Window(QWidget): 

    def __init__(self):

        super().__init__()

        # Set the window size
        self.setGeometry(50, 50, 800, 800)

        # Set the window title
        self.setWindowTitle("Images")

        self.UI()

    def UI(self):
        # Creating a label widgets
        self.image = QLabel(self)
        self.image.setPixmap(QPixmap("images/opencv.png"))
        self.image.move(150, 50)

        removeButton = QPushButton("Remove", self)
        removeButton.clicked.connect(self.removeImg)
        removeButton.move(400, 600)
    
        showButton = QPushButton("show", self)
        showButton.clicked.connect(self.showImg)
        showButton.move(150, 600)

        # show
        self.show()

    def removeImg(self):
        self.image.close()

    def showImg(self):
        self.image.show()

# Main method
def main():
    App = QApplication(sys.argv)
    window = Window() 
    sys.exit(App.exec_())

if __name__ == "__main__":
    main()
        