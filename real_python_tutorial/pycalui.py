#!/usr/bin/env python
# coding: utf-8

import sys
from functools import partial

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow

qt_creator_file = "pycalui.ui"
ERROR_MSG = 'ERROR'


class PyCalcUi:
    def __init__(self):
        self.ui = uic.loadUi(qt_creator_file)
        self.ui.setFixedSize(235, 235)
        self.ui.show()

    def setDisplayText(self, text):
        self.ui.lineEdit.setText(text)
        self.ui.lineEdit.setFocus()

    def displayText(self):
        return self.ui.lineEdit.text()

    def clearDisplay(self):
        self.setDisplayText('')


class PyCalcCtrl:
    def __init__(self, model, view):
        self._evaluate = model
        self._view = view
        self._connectSignals()

    def _calculateResult(self):
        result = self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)

    def _buildExpression(self, sub_exp):
        if self._view.displayText() == ERROR_MSG:
            self._view.clearDisplay()

        expression = self._view.displayText() + sub_exp
        self._view.setDisplayText(expression)

    def _connectSignals(self):
        count = self._view.ui.gridLayout.count()

        btn_text_dic = {}
        for i in range(1, count+1):
            btn_text = eval(f"self._view.ui.pushButton_{i}.text()")
            btn_object = eval(f"self._view.ui.pushButton_{i}")
            btn_text_dic[btn_text] = btn_object

        for btn_text, btn_object in btn_text_dic.items():
            if btn_text not in {"=", "C"}:
                btn_object.clicked.connect(partial(self._buildExpression, btn_text))

        btn_text_dic["="].clicked.connect(self._calculateResult)
        self._view.ui.lineEdit.returnPressed.connect(self._calculateResult)
        btn_text_dic["C"].clicked.connect(self._view.clearDisplay)


def evaluateExpression(expression):
    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = ERROR_MSG

    return result


def main():
    pycalc = QApplication(sys.argv)
    view = PyCalcUi()
    model = evaluateExpression
    PyCalcCtrl(view=view, model=model)
    sys.exit(pycalc.exec_())


if __name__ == '__main__':
    main()
