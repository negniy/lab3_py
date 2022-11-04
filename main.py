from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self). __init__()
        
        self.setWindowTitle("Программа о розах и тюльпанах")
        self.setGeometry(150, 150, 700, 700)
          
        self.btn=QtWidgets.QPushButton(self)
        self.btn.move(50, 50)
        self.btn.setText("путь к папке исходного датасета")
        self.btn.setFixedWidth(600)
        self.btn.clicked.connect(self.create_annotation)
    

    def create_annotation(self):
        print(1)

def applicaion():
    app = QApplication(sys.argv)
    window = Window()
    
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    applicaion()