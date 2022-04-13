import sys
from PyQt5.QtWidgets import *

from PyQt5 import QtWidgets, QtCore
from scripts.MainWindow import MainWindow
from scripts.Model import Model

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    model = Model()
    model.load_combined_dataset()

    sys.exit(app.exec())
