import sys
from PyQt5.QtWidgets import *


class Window(QWidget): 

    def __init__(self):

        super().__init__()

        # Set the window size
        self.setGeometry(100, 100, 350, 350)

        # Set the window title
        self.setWindowTitle("Radio Window")

        self.UI()

        self.show()

    def UI(self):
        self.userName = QLineEdit(self)
        self.userName.move(150, 50)
        self.userName.setPlaceholderText("Enter your name")

        self.emailID = QLineEdit(self)
        self.emailID.move(150, 80)
        self.emailID.setPlaceholderText("Enter email ID")

        self.male = QRadioButton("Male", self)
        self.male.move(150, 110)

        self.female = QRadioButton("Female", self)
        self.female.move(210, 110) 

        submit = QPushButton("submit", self)
        submit.move(150, 140)
        submit.clicked.connect(self.getValues)
    
    def getValues(self):
        if self.male.isChecked():
            print("UserName: " + self.userName.text() + "email ID: " + self.emailID.text() + "Gen : Male")
        else:
            print("UserName: " + self.userName.text() + "email ID: " + self.emailID.text() + "Gen : Female")

# Main method
def main():
    App = QApplication(sys.argv)
    window = Window() 
    sys.exit(App.exec_())

if __name__ == "__main__":
    main()
        