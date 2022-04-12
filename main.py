import sys
from PyQt5.QtWidgets import *
from scripts.DVView import DVView


class MyWid(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setParent(parent)
        btn1 = QPushButton("hello")
        btn2 = QPushButton("Guten Tag")

        layout = QVBoxLayout()
        layout.addWidget(btn1)
        layout.addWidget(btn2)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    centralWidget = QWidget(window)
    window.setCentralWidget(centralWidget)
    window.setWindowTitle('My First Application')
    window.move(300, 300)
    window.resize(650, 550)
    BaseUi = QWidget(window)
    Ui = DVView(window)

    mainLayout = QVBoxLayout()

    stack = QStackedWidget(window)
    stack.addWidget(BaseUi)
    stack.addWidget(Ui)

    mainLayout.addWidget(stack)

    centralWidget.setLayout(mainLayout)

    stack.setCurrentIndex(1)

    window.show()
    sys.exit(app.exec())
