import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget


class MyApp(QWidget):
    def __init__(self):
        super(MyApp, self).__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Reimplementing event handler')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Escape:
            self.close()
        elif QKeyEvent.key() == Qt.Key_F:
            self.showFullScreen()
        elif QKeyEvent.key() == Qt.Key_N:
            self.showNormal()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())