import sys
from PyQt5.QtWidgets import QLabel, QWidget,QVBoxLayout,QHBoxLayout,QGridLayout, QMainWindow, QApplication
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Layout Example")
        self.setGeometry(700, 300, 400, 400)
        #up to this point we did all our widget creation in the init
        #eventually that gets super messy
        #Lets create some functions to pull that stuff out
        self.initUI()
 
    def initUI(self):
        #Layout Managers.
        #The QMainWindow already has its own layout manager that cannot be overwritten
        #So we must create a single widget to put our layout manager in
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        #This central widget will act as a container for all other widgets
        label1 = QLabel("Label 1")
        label2 = QLabel("Label 2")
        label3 = QLabel("Label 3")
        label4 = QLabel("Label 4")
        label5 = QLabel("Label 5")
 
        #Give our labels some color
        label1.setStyleSheet("background-color: red")
        label2.setStyleSheet("background-color: blue")
        label3.setStyleSheet("background-color: yellow")
        label4.setStyleSheet("background-color: orange")
        label5.setStyleSheet("background-color: green")
        #Labelsdon't show up because I didn't specify a parent container
 
        #enter layout managers
        # vertical - QVBoxLayout
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
     
 
        hbox.addWidget(label1)
        hbox.addWidget(label2)
        vbox.addLayout(hbox)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        vbox.addWidget(label5)
 
        grid = QGridLayout()
        grid.addWidget(label1, 0, 0)#(0,0 is row,col)
        grid.addWidget(label2, 0, 1)#(0,0 is row,col)
        grid.addWidget(label3, 0, 2)#(0,0 is row,col)
        grid.addWidget(label4, 1, 0)#(0,0 is row,col)
        grid.addWidget(label5, 1, 2)#(0,0 is row,col)
        self.central_widget.setLayout(grid)
 
def main():
    app = QApplication(sys.argv) # Creates the main application and passes in an y command line arguments
    window = MainWindow() # Instantiate our main window
    window.show() #Make the window visible
    # Starts the application loop. The program will keep running until you close the window
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()