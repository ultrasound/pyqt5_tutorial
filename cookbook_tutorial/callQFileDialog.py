#!/usr/bin/env python
# coding: utf-8

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog

from qfiledialog import Ui_MainWindow


class MyForm(QMainWindow):
    def __init__(self):
        super(MyForm, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionOpen.triggered.connect(self.open_file_dialog)
        self.ui.actionSave.triggered.connect(self.save_file_dialog)
        self.show()

    def open_file_dialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', '/Users/nick')
        if fname[0]:
            f = open(fname[0], 'r')
            with f:
                data = f.read()
                self.ui.textEdit.setText(data)

    def save_file_dialog(self):
        options = QFileDialog.Options()
        print(options)
        options |= QFileDialog.DontUseNativeDialog
        print(options)
        file_name, _ = QFileDialog.getSaveFileName(self,
                                                   "QFileDialog.getSaveFileName()",
                                                   "",
                                                   "All Files (*);;Text Files (*.txt)",
                                                   options=options)
        f = open(file_name, 'w')
        text = self.ui.textEdit.toPlainText()
        f.write(text)
        f.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())