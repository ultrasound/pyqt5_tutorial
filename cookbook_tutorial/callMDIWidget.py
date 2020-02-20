#!/usr/bin/env python
# coding: utf-8

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from mdiwidgetui import Ui_MainWindow


class MyForm(QMainWindow):
    def __init__(self):
        super(MyForm, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.mdiArea.addSubWindow(self.ui.subwindow)
        self.ui.mdiArea.addSubWindow(self.ui.subwindow_2)

        self.ui.actionSubWindow_View.triggered.connect(self.subwindow_view)
        self.ui.actionTabbed_View.triggered.connect(self.tabbed_view)
        self.ui.actionCascade_View.triggered.connect(self.cascade_arrange)
        self.ui.actionTile_View.triggered.connect(self.tile_arrange)

        self.show()

    def subwindow_view(self):
        self.ui.mdiArea.setViewMode(0)

    def tabbed_view(self):
        self.ui.mdiArea.setViewMode(1)

    def cascade_arrange(self):
        self.ui.mdiArea.cascadeSubWindows()

    def tile_arrange(self):
        self.ui.mdiArea.tileSubWindows()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())