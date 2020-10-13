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
        
        # Main Layout
        mainLayout = QVBoxLayout()

        # Top Layout
        topLayout = QHBoxLayout()

        # Botton Layout
        bottomLayout = QHBoxLayout()
        
        cbox = QCheckBox("Check Box")

        topLayout.addWidget(cbox)
        
        button_1 = QPushButton("Button 1")
        button_2 = QPushButton("Button 2")

        bottomLayout.addWidget(button_1)
        bottomLayout.addWidget(button_2)

        # Add bottom and top to Main Layout
        mainLayout.addLayout(topLayout)
        mainLayout.addLayout(bottomLayout)
        
        self.setLayout(mainLayout)

        # Show display
        self.show()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == "__main__":
    main()