import sys
from PyQt5.QtWidgets import *
from pip import main


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 280, 80)

        self.centralWidget = QWidget()
        self.mainLayout = QVBoxLayout()

        self.stack = QStackedWidget()
        self.btn1 = QPushButton(self)
        self.btn2 = QPushButton(self)
        self.btn1.setText("1")
        self.btn2.setText("2")
        self.stack.addWidget(self.btn1)
        self.stack.addWidget(self.btn2)

        #self.btn = QPushButton(self)
        # self.btn.setText("Testq")
        self.btn1.clicked.connect(self.next)

        # self.mainLayout.addWidget(self.btn)
        self.mainLayout.addWidget(self.stack)

        self.centralWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.centralWidget)
        self.stack.setCurrentIndex(0)

    def next(self):
        self.stack.setCurrentIndex(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    root = Window()
    root.show()
    sys.exit(app.exec())
