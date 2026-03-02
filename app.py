import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

"""
sys: This is a built-in Python module that provides access to variables and functions that interact with the Python interpreter.
PyQt5.QtWidgets: This module contains all the main GUI “widgets” such as buttons, labels, and windows.
QApplication: This class manages the GUI application itself.
QMainWindow: This class provides a main application window that you can customize.
"""

#Create a custom window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CMP 25-26 Year 1")
        self.setGeometry(700,300,500,500) #xy,width,hight
        #x: distance from th left edge of your screen
        #y : distance from top of your screen

def main():
    app = QApplication(sys.argv) #creates th emain applictaion and passes in an y command line arguments
    window = MainWindow() #instatiste our main window
    window.show()
    sys.exit(app.exec_()) #starts an aplictaion loop will keep runing until close the winddow

if __name__ == "__main__":
    main()