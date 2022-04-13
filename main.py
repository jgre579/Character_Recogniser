import sys
from PyQt5.QtWidgets import *

from PyQt5 import QtWidgets, QtCore
from scripts.DVView import DVView
from scripts.MainController import MainController
from scripts.MainWindow import MainWindow
from scripts.Model import Model

if __name__ == "__main__":
    app = QApplication(sys.argv)

    model = Model()
    controller = MainController(model)
    model.load_combined_dataset()

    base_ui = QWidget()
    dv_view_ui = DVView(model)

    window = MainWindow(
        base_ui,
        dv_view_ui,
    )
    window.show()

    sys.exit(app.exec())
