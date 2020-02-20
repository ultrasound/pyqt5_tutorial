#!/usr/bin/env python
# coding: utf-8

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter
from PyQt5 import QtCore

from custommenubar import Ui_MainWindow


class AppWindow(QMainWindow):
    def __init__(self):
        super(AppWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.pos1 = [0, 0]
        self.pos2 = [0, 0]
        self.toDraw = ""

        self.ui.actionDraw_Circle.triggered.connect(self.draw_circle)
        self.ui.actionDraw_Rectangle.triggered.connect(self.draw_rectangle)
        self.ui.actionDraw_Line.triggered.connect(self.draw_line)
        self.ui.actionPage_Setup.triggered.connect(self.page_setup)
        self.ui.actionSet_Password.triggered.connect(self.set_password)
        self.ui.actionCut.triggered.connect(self.cut_method)
        self.ui.actionCopy.triggered.connect(self.copy_method)
        self.ui.actionPaste.triggered.connect(self.paste_method)

        self.show()

    def paintEvent(self, QPaintEvent):
        qp = QPainter()
        qp.begin(self)
        if self.toDraw == 'rectangle':
            width = self.pos2[0] - self.pos1[0]
            height = self.pos2[1] - self.pos1[1]
            qp.drawRect(self.pos1[0], self.pos1[1], width, height)
        elif self.toDraw == 'line':
            qp.drawLine(self.pos1[0], self.pos1[1], self.pos2[0],
                        self.pos2[1])
        elif self.toDraw == "circle":
            width = self.pos2[0] - self.pos1[0]
            height = self.pos2[1] - self.pos1[1]
            rect = QtCore.QRect(self.pos1[0], self.pos1[1], width, height)
            startAngle = 0
            arcLength = 360 * 16
            qp.drawArc(rect, startAngle, arcLength)
        qp.end()

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.buttons() & QtCore.Qt.LeftButton:
            self.pos1[0], self.pos1[1] = QMouseEvent.pos().x(), QMouseEvent.pos().y()

    def mouseReleaseEvent(self, QMouseEvent):
        self.pos2[0], self.pos2[1] = QMouseEvent.pos().x(), QMouseEvent.pos().y()
        self.update()

    def draw_circle(self):
        self.ui.label.setText("")
        self.toDraw = "circle"

    def draw_rectangle(self):
        self.ui.label.setText("")
        self.toDraw = "rectangle"

    def draw_line(self):
        self.ui.label.setText("")
        self.toDraw = "line"

    def page_setup(self):
        self.ui.label.setText("Page Setup menu item is selected")

    def set_password(self):
        self.ui.label.setText("Set Pasword menu item is selected")

    def cut_method(self):
        self.ui.label.setText("Cut menu item is selected")

    def copy_method(self):
        self.ui.label.setText("Copy menu item is selected")

    def paste_method(self):
        self.ui.label.setText("Paste menu item is selected")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())
