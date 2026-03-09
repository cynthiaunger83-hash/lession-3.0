import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon,  QFont, QPixmap #loads and manages the image file befor it is placed in a label
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CMP 25-26 Year 1")
        self.setGeometry(700,300,800,600) #xy,width,hight
        #x: distance from th left edge of your screen
        #y : distance from top of your 
        self.setWindowIcon(QIcon("images/Greg.png"))
        self.label=QLabel("i dont know", self)
        #added lkable
        #placing labke
        self.label.setStyleSheet(
            "color: black;"
            "font-weight: bold;"
            "font-style: italic;"
            "text-decoration: underline;"
        )
        self.setStyleSheet(
            "backgroun"
        )
        self.label.setGeometry(0,0,500,100)
        self.label.setAlignment(Qt.AlignCenter)
        self.label=QLabel("hello", self)
        #added lkable
        #placing labke
        self.label.setGeometry(0,0,300,100)
        self.label=QLabel("goodbye", self)
        #added lkable
        #placing labke
        self.label.setGeometry(0,0,800,100)
        self.piclabel = QLabel(self)
        self.piclabel.setGeometry(0,60, 300,250)
        self.pixmap = QPixmap("images/Greg.png")
        #put the image (pixmap imto the label)
        self.piclabel.setPixmap(self.pixmap)
        #if image is too big or too small we can make it fit
        self.piclabel.setScaledContents(True)
        self.piclabel.setGeometry(self.width(
        ) - self.piclabel.width(), self.height() - self.piclabel.height(),300,250)

        self.label.setAlignment(Qt.AlignCenter)
        self.piclabel = QLabel(self)
        self.piclabel.setGeometry(10,69, 300,250)
        self.pixmap = QPixmap("images/Greg.png")
        #put the image (pixmap imto the label)
        self.piclabel.setPixmap(self.pixmap)
        #if image is too big or too small we can make it fit
        self.piclabel.setScaledContents(True)
        self.piclabel.setGeometry(self.width(
        ) - self.piclabel.width(), self.height() - self.piclabel.height(),150,125)
        self.label.setAlignment(Qt.AlignCenter)
        self.piclabel = QLabel(self)
        self.piclabel.setGeometry(10,69, 300,250)
        self.pixmap = QPixmap("images/Greg.png")
        #put the image (pixmap imto the label)
        self.piclabel.setPixmap(self.pixmap)
        #if image is too big or too small we can make it fit
        self.piclabel.setScaledContents(True)
        self.piclabel.setGeometry(self.width(
        ) - self.piclabel.width(), self.height() - self.piclabel.height(),75,62)
def main():
    app = QApplication(sys.argv) #creates th emain applictaion and passes in an y command line arguments
    window = MainWindow() #instatiste our main window
    window.show()
    sys.exit(app.exec_()) #starts an aplictaion loop will keep runing until close the winddow

if __name__ == "__main__":
    main()