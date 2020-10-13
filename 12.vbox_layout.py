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
        vbox = QVBoxLayout()
        button_1 = QPushButton("Open", self)
        button_2 = QPushButton("Save", self)
        
        vbox.addStretch()
        # Add Button to widget
        vbox.addWidget(button_1)
        vbox.addWidget(button_2)
        #vbox.addStretch()

        # Set the Layout
        self.setLayout(vbox)

        # Show display
        self.show()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == "__main__":
    main()