from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

def applicaion():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("Программа о розах и тюльпанах")
    window.setGeometry(150, 150, 700, 700)
    
    btn=QtWidgets.QPushButton(window)
    btn.move(50, 50)
    btn.setText("1")
    btn.setFixedWidth(600)
    
    
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    applicaion()