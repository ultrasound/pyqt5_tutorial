#!/usr/bin/env python
# coding: utf-8

import sys

from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem

from tablewidget import Ui_Dialog


class MyForm(QDialog):
    def __init__(self, data):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.data = data
        self.add_content()

    def add_content(self):
        row = 0
        for tup in self.data:
            col = 0
            for item in tup:
                one_item = QTableWidgetItem(item)
                self.ui.tableWidget.setItem(row, col, one_item)
                col += 1
            row += 1


if __name__ == '__main__':
    data = [('Suite', '40'), ('Super Luxury', '30'), ('Super Deluxe', '20'), ('Ordinary', '10')]
    app = QApplication(sys.argv)
    w = MyForm(data)
    w.show()
    sys.exit(app.exec_())


