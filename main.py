import sys
from PyQt5 import QtWidgets
from scripts.DVModel import *
from scripts.MainController import *
from scripts.DVView import *


class App(QtWidgets.QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model = DatasetViewerModel()
        self.main_ctrl = MainController(self.model)
        self.main_view = Ui_MainWindow(self.model, self.main_ctrl)
        self.main_view.show()


if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())
