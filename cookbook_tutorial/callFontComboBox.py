#!/usr/bin/env python
# coding: utf-8

import sys

from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtGui

from fontcombobox import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.fontComboBox.currentFontChanged.connect(self.changFont)
        self.show()

    def changFont(self):
        myFont = QtGui.QFont(
            self.ui.fontComboBox.itemText(
                self.ui.fontComboBox.currentIndex()
            ), 15
        )
        self.ui.textEdit.setFont(myFont)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())