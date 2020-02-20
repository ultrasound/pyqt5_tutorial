#!/usr/bin/env python
# coding: utf-8

import sys

from PyQt5.QtWidgets import QApplication, QDialog, QInputDialog

from inputdialog import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super(MyForm, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButtonCountry.clicked.connect(self.disp_message)

        self.show()

    def disp_message(self):
        countries = ('Albania', 'Algeria', 'Andorra', 'Angola')
        country_name, ok = QInputDialog.getItem(self, "Input Dialog", "List of countries", countries, 0, False)
        if ok and country_name:
            self.ui.lineEditCountry.setText(country_name)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
