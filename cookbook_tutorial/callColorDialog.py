#!/usr/bin/env python
# coding: utf-8

import sys

from PyQt5.QtWidgets import QApplication, QDialog, QColorDialog
from PyQt5.QtGui import QColor

from colordialog import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super(MyForm, self).__init__()
        color = QColor(0, 0, 0)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.frameColor.setStyleSheet('QWidget { background-color: %s }' % color.name())

        self.ui.pushButtonColor.clicked.connect(self.disp_color)

        self.show()

    def disp_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.ui.frameColor.setStyleSheet("QWidget { background-color: %s }" % color.name())
            self.ui.labelColor.setText("You have selected the color with code: %s }" % str(color.name()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())



