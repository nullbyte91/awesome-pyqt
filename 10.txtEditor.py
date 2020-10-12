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
        # Text Editor
        self.editor = QTextEdit(self)
        self.editor.move(150, 80)

        button = QPushButton("Send", self)

        button.move(320, 280)

        button.clicked.connect(self.getValue)

        # show
        self.show()

    def getValue(self):
        text = self.editor.toPlainText()
        print(text)
        
# Main method
def main():
    App = QApplication(sys.argv)
    window = Window() 
    sys.exit(App.exec_())

if __name__ == "__main__":
    main()
        