#!/usr/bin/env python
# coding: utf-8

import sys
from PyQt5.QtWidgets import QApplication, QDialog, QFontDialog
from fontdialog import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super(MyForm, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.ui.pushButtonFont.clicked.connect(self.change_font)
        
        self.show()
        
    def change_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.ui.textEdit.setFont(font)
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
    