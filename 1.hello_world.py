# importing the required libraries 
from PyQt5.QtWidgets import * 
import sys

class Window(QWidget): 
    def __init__(self): 
        super().__init__() 
  
        # set the title 
        self.setWindowTitle("Hello World Window") 
  
        # setting  the geometry of window 
        # setGeometry(left, top, width, height) 
        self.setGeometry(50, 50, 300, 450) 
  
        # show all the widgets 
        self.show()
          
# create pyqt5 app 
App = QApplication(sys.argv) 
  
# create the instance of our Window 
window = Window() 

# start the app 
sys.exit(App.exec_()) 