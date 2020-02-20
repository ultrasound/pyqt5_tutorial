#!/usr/bin/env python
# coding: utf-8

# 마우스의 움직임에 따라 위젯의 배경색을 바꿈

import sys

from PyQt5.QtWidgets import QWidget, QLabel, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPalette

from math import sqrt


class Label(QLabel):
    def __init__(self, parent=None):
        super(Label, self).__init__(parent)
        self.setMouseTracking(True)  # 마우스가 Label 위를 이동하는 것을 감지
        self.setAutoFillBackground(True)  # 자동으로 배경색을 바꾸는 것 허용
