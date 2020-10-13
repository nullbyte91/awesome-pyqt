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
        
        # Horizontal Box Layout creation
        hbox = QHBoxLayout()
        button_1 = QPushButton("Button_1", self)
        button_2 = QPushButton("Button_2", self)
        
        hbox.addStretch()
        # Add Button to widget
        hbox.addWidget(button_1)
        hbox.addWidget(button_2)
        hbox.addStretch()

        # Set the Layout
        self.setLayout(hbox)

        # Show display
        self.show()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == "__main__":
    main()