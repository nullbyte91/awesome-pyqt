# PyQT GUI code snippet
PyQt5 is a comprehensive set of Python bindings for Qt v5. It is implemented as more than 35 extension modules and enables Python to be used as an alternative application development language to C++ on all supported platforms including iOS and Android.

## Import Components
```python
from PyQt5.QtWidgets import *

```

## Simple Window
```python
class Window(QWidget): 
    def __init__(self): 
        super().__init__() 
  
        # set the title 
        self.setWindowTitle("Hello World Window") 
  
        # Create a Window
        # setGeometry(left, top, width, height) 
        self.setGeometry(50, 50, 300, 450) 
  
        # show all the widgets 
        self.show()
          
# Create pyqt5 app 
App = QApplication(sys.argv) 
  
# Create the instance of our Window 
window = Window() 

# Start the app 
sys.exit(App.exec_()) 
```
 
## Label Widget
```python
# Creating a label widgets
self.text = QLabel("Label Widget", self)

# Set Text X, Y Position
self.text.move(160, 50)
```

## Buttons
```python

# Create a Enter button
enterButton = QPushButton("Enter", self)

# Create a Exit button
exitButton = QPushButton("Exit", self)

# Set Enter Button X, Y
enterButton.move(100, 80)

# Set Exit Button X, Y
exitButton.move(200, 80)

# Enter Button connect/Action
enterButton.clicked.connect(self.enterFun)

# Exit Button connect/Action
exitButton.clicked.connect(self.exitFun)

# Enter callback function
def enterFun(self):
    self.text.setText("You clicked Enter")
    self.text.resize(150, 20)

# Exit callback function
def exitFun(self):
    self.text.setText("You clicked Exit")
    self.text.resize(150, 20)

```

## LineEdit Widget
```python
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
```

## Load Image
```python
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
```

## ComboBox
```python
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
```

## Radio Buttons
```python
    self.male = QRadioButton("Male", self)
    self.male.move(150, 110)

    self.female = QRadioButton("Female", self)
    self.female.move(210, 110) 

```

## MessageBox Widget
```python
QMessageBox.question(self, "Warning !!!!", "Are you sure exit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
```

## SpinBox Widget
```python
self.spinBox = QSpinBox(self)
self.spinBox.move(150, 100)
self.spinBox.setFont(font)
#self.spinBox.setMinimum(25)
#self.spinBox.setMaximum(25)
self.spinBox.setRange(0, 200)
self.spinBox.valueChanged.connect(self.getVal)
```

## Text Editor
```python
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
```

## Horizontal Box Layout
```python
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
```

## Vertical Box Layout
```python
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
```

## Horizontal and Vertical Box Layout together
```python
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
```

## Form Layout
```python
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
```