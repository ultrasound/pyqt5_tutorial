#!/usr/bin/env python
# coding: utf-8

import sys

from PyQt5.QtWidgets import QApplication, QDialog, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap

from graphview import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super(MyForm, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.scene = QGraphicsScene(self)
        pixmap = QPixmap()
        pixmap.load('IMG_5060.jpeg')
        item = QGraphicsPixmapItem(pixmap)
        self.scene.addItem(item)
        self.ui.graphicsView.setScene(self.scene)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())