import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from Ui_DatasetViewer import Ui_MainWindow
#Form, Window = uic.loadUiType("DatasetViewer.ui")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ui_MainWindow()
    ex.show()
    sys.exit(app.exec_())
