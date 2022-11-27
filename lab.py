import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap

from changed_dataset import copy_to_another as to_another
from create_annotation import create_annotation as make_ann
from iterator import Iterator
from random_dataset import random_copy as random


class Ui_MainWindow(object):
    def setupUi(self, MainWindow)-> None:
        """ 
        конструктор 
        Args:
            MainWindow (_type_): родительский класс для окна
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 550)
        MainWindow.setStyleSheet("\n"
"background-color: rgb(197, 255, 251);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 450, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(4, 59, 441, 341))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(-1, -1, 441, 311))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_3.addWidget(self.pushButton_5)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(-1, -1, 441, 311))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_4.addWidget(self.pushButton_6)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 410, 431, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.folderpath = QtWidgets.QFileDialog.getExistingDirectory(MainWindow, "Выберите папку с датасетом")
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        make_ann("temp_annotation.csv", ["rose", "tulip"], self.folderpath)
        self.rose_iterator = Iterator('temp_annotation.csv', 'rose')
        self.tulip_iterator = Iterator('temp_annotation.csv', 'tulip')
        self.add_functions()

    def retranslateUi(self, MainWindow)-> None:
        """
        показывает то что будет выводиться на экран
        Args:
            MainWindow (_type_): родительский класс для окна
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Моя программа"))
        self.label.setText(_translate("MainWindow", "Программа по работе с изображениями"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_5.setText(_translate("MainWindow", "Следующая роза"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Розы"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_6.setText(_translate("MainWindow", "Следующий тюльпан"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Тюльпаны"))
        self.pushButton.setText(_translate("MainWindow", "Создать аннотацию"))
        self.pushButton_2.setText(_translate("MainWindow", "Перенести в другую директорию"))
        self.pushButton_3.setText(_translate("MainWindow", "Перезаписать со случайными номерами"))
        
    def add_functions(self)-> None:
        """обработчик событий
        """
        self.pushButton_5.clicked.connect(lambda: self.next_rose())
        self.pushButton_6.clicked.connect(lambda: self.next_tulip())
        self.pushButton.clicked.connect(lambda: self.create_annotation()) #чтобы метод не только передавался но и выполнялся
        self.pushButton_2.clicked.connect(lambda: self.copy_to_another())
        self.pushButton_3.clicked.connect(lambda: self.random_copy())
        
    def create_annotation(self)-> None:
        """функция создания аннотации
        """
        make_ann("annotation.csv", ["rose", "tulip"], self.folderpath)
        
    def copy_to_another(self)-> None:
        """копирует датасет в другую директорию и создает аннотацию
        """
        to_another("changed_annotation.csv", ["rose", "tulip"], self.folderpath)
        print("ready")
    
    def random_copy(self)-> None:
        """копирует с рандомными номерами и создает аннотацию
        """
        random("random_annotation.csv", ["rose", "tulip"], self.folderpath)
        print("ready")
        
    def next_rose(self)-> None:
        """помещает в лейбл2 изображение розы
        """
        self.image_way_rose = next(self.rose_iterator)
        while self.image_way_rose == None:
            self.image_way_rose = next(self.rose_iterator)
        if os.path.isfile(str(self.image_way_rose)):
            image = QPixmap(self.image_way_rose)
            self.label_2.clear()
            self.label_2.setPixmap(image)
            self.label_2.adjustSize()
            self.label_2.move(0, 0)
            self.label_2.show()
        else:
            print('image dont find')

    def next_tulip(self) -> None:
        """помещает в лейбл3 изображение тюльпана
        """
        self.image_way_tulip = next(self.tulip_iterator)
        while self.image_way_tulip == None:
            self.image_way_tulip = next(self.tulip_iterator)
        if os.path.isfile(str(self.image_way_tulip)):
            image = QPixmap(self.image_way_tulip)
            self.label_3.clear()
            self.label_3.setPixmap(image)
            self.label_3.adjustSize()
            self.label_3.move(0, 0)
            self.label_3.show()
        else:
            print('image dont find')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    os.remove("temp_annotation.csv")
    sys.exit(app.exec_())
    
