# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Jorda\OneDrive\Desktop\UoA2022\COMPSYS 302\2022-python-01\scripts\DatasetViewer.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from scripts.MainController import MainController
from scripts.Model import *
from PIL import Image

class DVView(QWidget):

    def __init__(self, model):
        super().__init__()
        self.model = model
        self.createUi()   

    def createUi(self):
 
        self.horizLayout = QHBoxLayout()
        self.createScrollArea()
        self.horizLayout.addWidget(self.scrollArea)
        self.horizLayout.insertSpacing(1, 20)
        self.createButtonArea()
        self.horizLayout.addLayout(self.verticalLayout)
        self.setLayout(self.horizLayout)

    def scrollbar_moved(self, current_row):
        if(self.scrollbar.value() == self.scrollbar.maximum()):
            print("Generate images: " + str(self.scrollbar.value()))
            self.images.append(self.load_images_for_scrolling(6))
        print(str(self.scrollbar.value()))
        #print('Current row ' + str(current_row/6))
        #print("Number or gerneated images: " + str(current_row*4))


    def createScrollArea(self):
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaContents = QWidget(self.scrollArea)
        self.scrollArea.setWidget(self.scrollAreaContents)
        self.gridLayout = QGridLayout(self.scrollAreaContents)
        
        self.scrollbar = self.scrollArea.verticalScrollBar()
        self.scrollbar.valueChanged.connect(lambda: self.scrollbar_moved(self.current_row))

        self.images = []
        self.current_row = 0;
        # Inital loading of images to scrollable area
        self.images.append(self.load_images_for_scrolling(6))

        #self.images.append(self.load_images_for_scrolling(20))

    def load_images_for_scrolling(self, rows):

        row_width = 4
        images = []

        for i in range(0, rows):
            for j in range(0, row_width):

                digitImage = QLabel()
                image_num = len(images) + self.current_row * row_width
                piximap = QtGui.QPixmap(self.build_image(self.model.get_image(image_num), image_num))
                digitImage.setPixmap(piximap)
                digitImage.setMinimumSize(QtCore.QSize(100, 100))
                digitImage.setAlignment(QtCore.Qt.AlignCenter)
                images.append(digitImage)
                self.gridLayout.addWidget(digitImage, i + self.current_row, j)
            self.current_row += 1
    

        return images
            
        


    
    def build_image(self, image_data, name):

        im = Image.fromarray(image_data)
        addr = Model.get_image_address(str(name))
        im.save(addr)
        return addr

    
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
        