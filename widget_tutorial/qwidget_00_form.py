#!/usr/bin/env python
# coding: utf-8

# 기본 위젯을 사용하여 기본 창을 생성
# '창 이름'을 변경한다.

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

__author__ = "Nick Kim"


class Form(QWidget):
    """
    만들고자 하는 프로그램의 기본이 되는 창 또는 폼 위젯
    본 위젯 위에 다른 위젯을 올려서 모양을 만든다.

    QWidget을 상속받아서 필요한 메소드를 작성
    """
    def __init__(self):
        """
        보통 __init__에서 필요한 것들을 다른 위젯들을 선언해줘도 되지만 init_widget을 따로 만들어 호춣한다.
        """
        QWidget.__init__(self, flags=Qt.Widget)
        self.init_widget()

    def init_widget(self):
        """
        현재 위젯의 모양들을 초기화
        :return:
        """
        self.setWindowTitle("Hello World")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())