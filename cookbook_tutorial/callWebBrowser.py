#!/usr/bin/env python
# coding: utf-8

import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QDialog

from webbrowser import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super(MyForm, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonGo.clicked.connect(self.disp_site)

        self.show()

    def disp_site(self):
        self.ui.widget.load(QUrl(self.ui.lineEditURL.text()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())