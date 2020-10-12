import sys
from PyQt5.QtWidgets import *


class Window(QWidget): 

    def __init__(self):

        super().__init__()

        # Set the window size
        self.setGeometry(50, 50, 350, 350)

        # Set the window title
        self.setWindowTitle("Login Window")

        self.UI()

    def UI(self):
        # Creating a Line Edit for userName
        self.userName = QLineEdit(self)
        self.userName.setPlaceholderText("Please Enter your name")
        self.userName.move(120, 50)

        # Creatung a Line Edit for Password
        self.password = QLineEdit(self)
        self.password.setPlaceholderText("Please Enter your password")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.move(120, 80)

        button = QPushButton("Save", self)
        button.move(180, 110)
        button.clicked.connect(self.showVal)

        # show
        self.show()
    
    def showVal(self):
        name = self.userName.text()
        password = self.password.text()

        print("User Name: {} Password: {}".format(name, password))
        
# Main method
def main():
    App = QApplication(sys.argv)
    window = Window() 
    sys.exit(App.exec_())

if __name__ == "__main__":
    main()
        