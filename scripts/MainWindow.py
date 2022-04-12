from PyQt5.QtWidgets import *
from scripts.DVView import DVView


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.buildUI()

    def buildUI(self):

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)
        self.setWindowTitle('My First Application')
        self.move(300, 300)
        self.resize(650, 550)
        mainLayout = QVBoxLayout()
        BaseUi = QWidget(self)
        Ui = DVView(self)

        self.stack = QStackedWidget(self)
        self.stack.addWidget(BaseUi)
        self.stack.addWidget(Ui)

        mainLayout.addWidget(self.stack)

        centralWidget.setLayout(mainLayout)

        self.stack.setCurrentIndex(1)

        exitAction = QAction('Exit', self)
        newModelAction = QAction('New Model', self)

        windowDV = QAction('Dataset Viewer', self)

        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        menuFile = menubar.addMenu('&File')
        menuWindow = menubar.addMenu('&Window')
        menuOptions = menubar.addMenu('&Options')
        menuHelp = menubar.addMenu('Help')
        menuFile.addAction(newModelAction)
        menuFile.addAction(exitAction)
