#!/usr/bin/env python
# coding: utf-8

import sys

from PyQt5.QtWidgets import QDialog, QApplication

from listwidget2 import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.listWidgetDiagnosis.itemSelectionChanged.connect(self.disp_selected_test)

        self.show()

    def disp_selected_test(self):
        self.ui.listWidgetSelectedTests.clear()
        items = self.ui.listWidgetDiagnosis.selectedItems()
        for i in list(items):
            self.ui.listWidgetSelectedTests.addItem(i.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())