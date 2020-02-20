#!/usr/bin/env python
# coding: utf-8

import sys
from PyQt5.QtWidgets import QDialog, QApplication

from scrollbar import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.horizontalScrollBarSugarLevel.valueChanged.connect(self.scroll_horizontal)
        self.ui.verticalScrollBarPulseRate.valueChanged.connect(self.scroller_vertical)
        self.ui.horizontalSliderBloodPressure.valueChanged.connect(self.slider_horizontal)
        self.ui.verticalSliderCholestrolLevel.valueChanged.connect(self.slider_vertical)

        self.show()

    def scroll_horizontal(self, value):
        self.ui.lineEditResult.setText("Sugar Level : " + str(value))

    def scroller_vertical(self, value):
        self.ui.lineEditResult.setText("Pulse Rate : " + str(value))

    def slider_horizontal(self, value):
        self.ui.lineEditResult.setText("Blood Pressure : " + str(value))

    def slider_vertical(self, value):
        self.ui.lineEditResult.setText("Cholestrol Level : " + str(value))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
