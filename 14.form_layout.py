import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Create a Window
        self.setGeometry(50, 50, 400, 400)

        # Set Window Title
        self.setWindowTitle("HBOX Layout")

        self.UI()
    
    def UI(self):
        
        # Form Layout
        formLayout = QFormLayout()

        name_text = QLabel("Name: ")
        name_input = QLineEdit()

        pass_text = QLabel("Password: ")
        pass_input = QLineEdit()

        hbox = QHBoxLayout()
        hbox.addWidget(QPushButton("Save"))
        hbox.addWidget(QPushButton("Login"))
        
        formLayout.addRow(name_text, name_input)
        formLayout.addRow(pass_text, pass_input)
        formLayout.addRow(hbox)

        self.setLayout(formLayout)
        # Show display
        self.show()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == "__main__":
    main()