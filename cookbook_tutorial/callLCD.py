#!/usr/bin/env python
# coding: utf-8

import sys

from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import QTimer, QTime

from lcdnumber import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        timer = QTimer(self)
        timer.timeout.connect(self.showlcd)
        timer.start(1000)

        self.show()

    def showlcd(self):
        time = QTime.currentTime()
        text = time.toString('mm:ss')
        self.ui.lcdNumber.display(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())