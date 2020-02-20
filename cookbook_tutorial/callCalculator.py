#!/usr/bin/env python
# coding: utf-8

import sys

from PyQt5.QtWidgets import QDialog, QApplication

from calculator import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonPlus.clicked.connect(self.add_two_num)
        self.ui.pushButtonSubtract.clicked.connect(self.subtract_twon_num)
        self.ui.pushButtonMultiply.clicked.connect(self.multiply_two_num)
        self.ui.pushButtonDivide.clicked.connect(self.divide_two_num)
        self.show()

    def add_two_num(self):
        if len(self.ui.lineEditFirstNumber.text()) != 0:
            a = int(self.ui.lineEditFirstNumber.text())
        else:
            a = 0

        if len(self.ui.lineEditSecondNumber.text()) != 0:
            b = int(self.ui.lineEditSecondNumber.text())
        else:
            b = 0

        sum = a + b
        self.ui.labelResult.setText("Addition: " + str(sum))

    def subtract_twon_num(self):
        if len(self.ui.lineEditFirstNumber.text()) != 0:
            a = int(self.ui.lineEditFirstNumber.text())
        else:
            a = 0

        if len(self.ui.lineEditSecondNumber.text()) != 0:
            b = int(self.ui.lineEditSecondNumber.text())
        else:
            b = 0

        diff = a - b
        self.ui.labelResult.setText("Substraction: " + str(diff))

    def multiply_two_num(self):
        if len(self.ui.lineEditFirstNumber.text()) != 0:
            a = int(self.ui.lineEditFirstNumber.text())
        else:
            a = 0

        if len(self.ui.lineEditSecondNumber.text()) != 0:
            b = int(self.ui.lineEditSecondNumber.text())
        else:
            b = 0

        mult = a * b
        self.ui.labelResult.setText("Multiplication: " + str(mult))

    def divide_two_num(self):
        if len(self.ui.lineEditFirstNumber.text()) != 0:
            a = int(self.ui.lineEditFirstNumber.text())
        else:
            a = 0

        if len(self.ui.lineEditSecondNumber.text()) != 0:
            b = int(self.ui.lineEditSecondNumber.text())
        else:
            b = 0

        division = a / b
        self.ui.labelResult.setText("Division: " + str(round(division, 2)))


if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())