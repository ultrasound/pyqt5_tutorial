#!/usr/bin/env python
# coding: utf-8

import sys
from decimal import Decimal

from PyQt5 import QtCore, QtGui, QtWidgets, uic

qtcreator_file = "taxcalculator.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.calc_tax_button.clicked.connect(self.CalculateTax)

    def CalculateTax(self):
        price = Decimal(self.price_box.text())
        tax = Decimal(self.tax_rate.value())
        total_price = price + ((tax /100)  * price)
        total_price_string = "The total price with tax is: {:.2f}".format(total_price)
        self.results_output.setText(total_price_string)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())