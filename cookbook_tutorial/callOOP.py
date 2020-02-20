#!/usr/bin/env python
# coding: utf-8

import sys

from PyQt5.QtWidgets import QApplication, QDialog

from oop import Ui_Dialog


class Student:
    name = ""

    def __init__(self, name):
        self.name = name

    def print_name(self):
        return self.name


class MyForm(QDialog):
    def __init__(self):
        super(MyForm, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonClickMe.clicked.connect(self.disp_message)

        self.show()

    def disp_message(self):
        studentObj = Student(self.ui.lineEditName.text())
        self.ui.labelResponse.setText("Hello " + studentObj.print_name())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())