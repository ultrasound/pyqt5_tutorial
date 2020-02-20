#!/usr/bin/env python
# coding: utf-8

import sys

from PyQt5.QtWidgets import QDialog, QApplication
from radio_button2 import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.radioButtonMedium.toggled.connect(self.dispSelected)
        self.ui.radioButtonLarge.toggled.connect(self.dispSelected)
        self.ui.radioButtonXL.toggled.connect(self.dispSelected)
        self.ui.radioButtonXXL.toggled.connect(self.dispSelected)

        self.ui.radioButtonDebitCard.toggled.connect(self.dispSelected)
        self.ui.radioButtonNetBanking.toggled.connect(self.dispSelected)
        self.ui.radioButtonCashOnDelivery.toggled.connect(self.dispSelected)
        self.show()

    def dispSelected(self):
        selected1 = ""
        selected2 = ""

        if self.ui.radioButtonMedium.isChecked():
            selected1 = "Medium"
        elif self.ui.radioButtonLarge.isChecked():
            selected1 = "Large"
        elif self.ui.radioButtonXL.isChecked():
            selected1 = "Extra Large"
        elif self.ui.radioButtonXXL.isChecked():
            selected1 = "Extra Extra Large"

        if self.ui.radioButtonDebitCard.isChecked():
            selected2 = "Debit/Credit Card"
        elif self.ui.radioButtonNetBanking.isChecked():
            selected2 = "NetBanking"
        elif self.ui.radioButtonCashOnDelivery.isChecked():
            selected2 = "Cash On Delivery"

        self.ui.labelSelected.setText("Chose shirt size is " + selected1 + "and payment mehtods as " + selected2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())