from PyQt5.QtWidgets import *
from scripts.DVView import DVView


class MainWindow(QMainWindow):
    def __init__(self, ui1, ui2):
        super().__init__()
        self.base_ui = ui1
        self.dv_view_ui = ui2
        self.buildUI()

    def addWidgetToStack(self, widget):

        self.stack.addWidget(widget)

    def display(self, index):
        self.stack.setCurrentIndex(index)

    def buildUI(self):

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)
        self.setWindowTitle("My First Application")
        self.move(300, 300)
        self.resize(650, 550)
        mainLayout = QVBoxLayout()

        self.stack = QStackedWidget(self)
        self.stack.addWidget(self.base_ui)
        self.stack.addWidget(self.dv_view_ui)

        mainLayout.addWidget(self.stack)

        centralWidget.setLayout(mainLayout)

        self.stack.setCurrentIndex(1)

        exitAction = QAction("Exit", self)
        newModelAction = QAction("New Model", self)

        windowDV = QAction("Dataset Viewer", self)
        windowBlank = QAction("Blank", self)

        windowDV.triggered.connect(lambda: self.display(1))
        windowBlank.triggered.connect(lambda: self.display(0))

        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Exit application")
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        menuFile = menubar.addMenu("&File")
        menuWindow = menubar.addMenu("&Window")
        menuOptions = menubar.addMenu("&Options")
        menuHelp = menubar.addMenu("Help")
        menuFile.addAction(newModelAction)
        menuFile.addAction(exitAction)

        menuWindow.addAction(windowDV)
        menuWindow.addAction(windowBlank)
