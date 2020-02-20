#!/usr/bin/env python
# coding: utf-8

import sys

from PyQt5.QtWidgets import QDialog, QApplication

from progressbar import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # self.ui.progressBar.setValue(0)

        self.ui.pushButtonStart.clicked.connect(self.update_bar)
        self.show()

    def update_bar(self):
        x = 0
        while x < 100:
            x += 0.0001
            self.ui.progressBar.setValue(x)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())