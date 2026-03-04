import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon,  QFont, QPixmap #loads and manages the image file befor it is placed in a lable
from PyQt5.QtCore import Qt
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
        #y : distance from top of your 
        self.setWindowIcon(QIcon("images/Greg.png"))
        self.lable=QLabel("hello", self)
        #added lkable
        #placing labke
        self.setStyleSheet(
            "color: pink;"
            "background-color: #87CEFA;"
            "font-weight: bold;"
            "font-style: italic;"
            "text-decoration: underline;"
        )
        #self.lable.setGeometry("0,0,500,100")
        self.lable.setAlignment(Qt.AlignCenter)
        self.piclable = QLabel(self)
        self.piclable.setGeometry(0,100, 300,250)
        self.pixmap = QPixmap("images/Greg.png")
        #put the image (pixmap imto the lable)
        self.piclable.setPixmap(self.pixmap)
        #if image is too big or too small we can make it fit
        self.piclable.setScaledContents(True)
        self.piclable.setGeometry(self.width(
        ) - self.piclable.width(), self.height() - self.piclable.height(),300,250)
def main():
    app = QApplication(sys.argv) #creates th emain applictaion and passes in an y command line arguments
    window = MainWindow() #instatiste our main window
    window.show()
    sys.exit(app.exec_()) #starts an aplictaion loop will keep runing until close the winddow

if __name__ == "__main__":
    main()