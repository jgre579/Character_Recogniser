# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Jorda\OneDrive\Desktop\UoA2022\COMPSYS 302\2022-python-01\scripts\DatasetViewer.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *


class DVView(QWidget):
    def __init__(self, centralWidget):

        super().__init__()
        self.centralwidget = centralWidget
        self.setupUi()
        # self.show()

    def setupUi(self):
        self.setParent(self.centralwidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(
            QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 652, 860))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setMinimumSize(QtCore.QSize(100, 100))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_35.setMinimumSize(QtCore.QSize(100, 100))
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.gridLayout.addWidget(self.label_35, 4, 2, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_36.setMinimumSize(QtCore.QSize(100, 100))
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.gridLayout.addWidget(self.label_36, 4, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setMinimumSize(QtCore.QSize(100, 100))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 3, 3, 1, 1)
        self.label_43 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_43.setMinimumSize(QtCore.QSize(100, 100))
        self.label_43.setAlignment(QtCore.Qt.AlignCenter)
        self.label_43.setObjectName("label_43")
        self.gridLayout.addWidget(self.label_43, 6, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setMinimumSize(QtCore.QSize(100, 100))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 1, 1, 1)
        self.label_42 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_42.setMinimumSize(QtCore.QSize(100, 100))
        self.label_42.setAlignment(QtCore.Qt.AlignCenter)
        self.label_42.setObjectName("label_42")
        self.gridLayout.addWidget(self.label_42, 6, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setMinimumSize(QtCore.QSize(100, 100))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_15.setMinimumSize(QtCore.QSize(100, 100))
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 2, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setMinimumSize(QtCore.QSize(100, 100))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setMinimumSize(QtCore.QSize(100, 100))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_13.setMinimumSize(QtCore.QSize(100, 100))
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 3, 1, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_40.setMinimumSize(QtCore.QSize(100, 100))
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName("label_40")
        self.gridLayout.addWidget(self.label_40, 7, 3, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_37.setMinimumSize(QtCore.QSize(100, 100))
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.gridLayout.addWidget(self.label_37, 6, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_16.setMinimumSize(QtCore.QSize(100, 100))
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 1, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setMinimumSize(QtCore.QSize(100, 100))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setMinimumSize(QtCore.QSize(100, 100))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_12.setMinimumSize(QtCore.QSize(100, 100))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 2, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_14.setMinimumSize(QtCore.QSize(100, 100))
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 3, 2, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_33.setMinimumSize(QtCore.QSize(100, 100))
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.gridLayout.addWidget(self.label_33, 4, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setMinimumSize(QtCore.QSize(100, 100))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_39.setMinimumSize(QtCore.QSize(100, 100))
        self.label_39.setAlignment(QtCore.Qt.AlignCenter)
        self.label_39.setObjectName("label_39")
        self.gridLayout.addWidget(self.label_39, 7, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_11.setMinimumSize(QtCore.QSize(100, 100))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setMinimumSize(QtCore.QSize(100, 100))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 2, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_38.setMinimumSize(QtCore.QSize(100, 100))
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.gridLayout.addWidget(self.label_38, 7, 1, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_41.setMinimumSize(QtCore.QSize(100, 100))
        self.label_41.setAlignment(QtCore.Qt.AlignCenter)
        self.label_41.setObjectName("label_41")
        self.gridLayout.addWidget(self.label_41, 6, 1, 1, 1)
        self.label_44 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_44.setMinimumSize(QtCore.QSize(100, 100))
        self.label_44.setAlignment(QtCore.Qt.AlignCenter)
        self.label_44.setObjectName("label_44")
        self.gridLayout.addWidget(self.label_44, 5, 0, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_34.setMinimumSize(QtCore.QSize(100, 100))
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.gridLayout.addWidget(self.label_34, 5, 1, 1, 1)
        self.label_45 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_45.setMinimumSize(QtCore.QSize(100, 100))
        self.label_45.setAlignment(QtCore.Qt.AlignCenter)
        self.label_45.setObjectName("label_45")
        self.gridLayout.addWidget(self.label_45, 4, 1, 1, 1)
        self.label_46 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_46.setMinimumSize(QtCore.QSize(100, 100))
        self.label_46.setAlignment(QtCore.Qt.AlignCenter)
        self.label_46.setObjectName("label_46")
        self.gridLayout.addWidget(self.label_46, 5, 2, 1, 1)
        self.label_47 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_47.setMinimumSize(QtCore.QSize(100, 100))
        self.label_47.setAlignment(QtCore.Qt.AlignCenter)
        self.label_47.setObjectName("label_47")
        self.gridLayout.addWidget(self.label_47, 5, 3, 1, 1)
        self.label_48 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_48.setMinimumSize(QtCore.QSize(100, 100))
        self.label_48.setAlignment(QtCore.Qt.AlignCenter)
        self.label_48.setObjectName("label_48")
        self.gridLayout.addWidget(self.label_48, 7, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        spacerItem = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtWidgets.QComboBox()
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMaximumSize(QtCore.QSize(16777215, 25))
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton()
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 25))
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton()
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 350, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.setLayout(self.horizontalLayout_2)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.setToolTip(_translate(
            "MainWindow", "vrionviwnvownvrwivowinviownvodhvauspvhauhvuph"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.label_35.setText(_translate("MainWindow", "TextLabel"))
        self.label_36.setText(_translate("MainWindow", "TextLabel"))
        self.label_10.setText(_translate("MainWindow", "TextLabel"))
        self.label_43.setText(_translate("MainWindow", "TextLabel"))
        self.label_8.setText(_translate("MainWindow", "TextLabel"))
        self.label_42.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.label_15.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_13.setText(_translate("MainWindow", "TextLabel"))
        self.label_40.setText(_translate("MainWindow", "TextLabel"))
        self.label_37.setText(_translate("MainWindow", "TextLabel"))
        self.label_16.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_12.setText(_translate("MainWindow", "TextLabel"))
        self.label_14.setText(_translate("MainWindow", "TextLabel"))
        self.label_33.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.label_39.setText(_translate("MainWindow", "TextLabel"))
        self.label_11.setText(_translate("MainWindow", "TextLabel"))
        self.label_9.setText(_translate("MainWindow", "TextLabel"))
        self.label_38.setText(_translate("MainWindow", "TextLabel"))
        self.label_41.setText(_translate("MainWindow", "TextLabel"))
        self.label_44.setText(_translate("MainWindow", "TextLabel"))
        self.label_34.setText(_translate("MainWindow", "TextLabel"))
        self.label_45.setText(_translate("MainWindow", "TextLabel"))
        self.label_46.setText(_translate("MainWindow", "TextLabel"))
        self.label_47.setText(_translate("MainWindow", "TextLabel"))
        self.label_48.setText(_translate("MainWindow", "TextLabel"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Training Set"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Test Set"))
        self.pushButton.setText(_translate("MainWindow", "Create Filter"))
        self.pushButton_2.setText(_translate("MainWindow", "View Stats"))
