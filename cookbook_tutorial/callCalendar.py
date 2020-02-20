#!/usr/bin/env python
# coding: utf-8

import sys

from PyQt5.QtWidgets import QApplication, QDialog

from calendar import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.calendarWidget.selectionChanged.connect(self.disp_date)

        self.show()

    def disp_date(self):
        self.ui.dateEdit.setDisplayFormat('MMM d yyyy')
        self.ui.dateEdit.setDate(self.ui.calendarWidget.selectedDate())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())