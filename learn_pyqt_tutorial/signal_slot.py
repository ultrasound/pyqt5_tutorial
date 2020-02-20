#!/usr/bin/env python
# coding: utf-8
import sys

from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.windowTitleChanged.connect(self.onWindowTitleChange)

        self.windowTitleChanged.connect(lambda x: self.my_custom_fn())

        self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x))

        self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x, 2))

        self.setWindowTitle("My Awesome App")

        label = QLabel("This is awesone")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

    def onWindowTitleChange(self, s):
        print(s)

    def my_custom_fn(self, a="Heloo", b=5):
        print(a, b)

    def contextMenuEvent(self, QContextMenuEvent):
        print("Context menu event!")
        super().contextMenuEvent(QContextMenuEvent)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())