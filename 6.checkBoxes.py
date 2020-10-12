import sys
from PyQt5.QtWidgets import *


class Window(QWidget): 

    def __init__(self):

        super().__init__()

        # Set the window size
        self.setGeometry(100, 100, 350, 350)

        # Set the window title
        self.setWindowTitle("Combo Window")

        self.UI()

        self.show()

    def UI(self):
        self.combo = QComboBox(self)
        self.combo.move(150, 100)
        
        button = QPushButton("save", self)
        button.move(150, 130)
        button.clicked.connect(self.display)

        lang_list = ["c", "c++", "java", "css"]

        for item in lang_list:
            self.combo.addItem(item)
        
        self.show()

    def display(self):
        print(self.combo.currentText())

# Main method
def main():
    App = QApplication(sys.argv)
    window = Window() 
    sys.exit(App.exec_())

if __name__ == "__main__":
    main()
        