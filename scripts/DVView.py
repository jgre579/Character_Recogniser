# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Jorda\OneDrive\Desktop\UoA2022\COMPSYS 302\2022-python-01\scripts\DatasetViewer.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *


class DVView(QWidget):
    def __init__(self):
        super().__init__()
        self.createUi()   

    def createUi(self):
 
        self.horizLayout = QHBoxLayout()
        self.createScrollArea()
        self.horizLayout.addWidget(self.scrollArea)
        self.horizLayout.insertSpacing(1, 20)
        self.createButtonArea()
        self.horizLayout.addLayout(self.verticalLayout)
        self.setLayout(self.horizLayout)

    def createScrollArea(self):
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaContents = QWidget(self.scrollArea)
        self.scrollArea.setWidget(self.scrollAreaContents)
        self.gridLayout = QGridLayout(self.scrollAreaContents)

        self.digitImages = []

        for i in range(0, 6):
            for j in range(0, 4):

                digitImage = QLabel('Test')
                digitImage.setMinimumSize(QtCore.QSize(100, 100))
                digitImage.setAlignment(QtCore.Qt.AlignCenter)
                self.digitImages.append(digitImage)
                self.gridLayout.addWidget(digitImage, i, j)

        spacerItem = QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
    
    def createButtonArea(self):

        self.verticalLayout = QVBoxLayout()
        self.comboBox = QComboBox(self)
        self.filterBtn = QPushButton("Create a filter")
        self.statsBtn = QPushButton("View Stats")

        self.comboBox.addItem("Training Set")
        self.comboBox.addItem("Test Set")

        self.verticalLayout.setSpacing(20)
        self.verticalLayout.addWidget(self.comboBox)
        self.verticalLayout.addWidget(self.filterBtn)
        self.verticalLayout.addWidget(self.statsBtn)
        self.verticalLayout.addStretch()
        