#!/usr/bin/env python
# coding: utf-8

# PaintEvent를 사용하여 실시간으로 값 변경하기
# MouseEvent를 사용하여 마우스 값 가져오기

import sys

from PyQt5.QtWidgets import QWidget, QLabel, QApplication
from PyQt5.QtCore import Qt


class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        # 마우스 좌표 저장용 변수
        self.mouse_x = 0
        self.mouse_y = 0

        self.lb = QLabel(self)

        self.properties_list = (
            "width", "height", "x", "y", "geometry",
            "maximumHeight", "maximumWidth", "maximumSize", "minimumSize", "minimumWidth",
            "size", "windowFilePath", "windowTitle",
            "underMouse"
        )  # 출력할 property 이름

        self.init_widget()

    def init_widget(self):
        self.setWindowTitle("Hello World")
        self.setGeometry(100, 100, 640, 480)
        self.setMouseTracking(True)  # 마우스 움직임을 캐치

        self.lb.setStyleSheet("background-color: yellow")
        self.lb.setMouseTracking(True)  # False 값을 경우 Label 위젯에서는 mouse 이벤트가 발생하지 않는다.
        msg = self.get_properties_values(self.properties_list)
        self.lb.setText(msg)

    def get_properties_values(self, properties):
        msg = []
        for p in properties:
            if not hasattr(self, p):
                continue
            value = getattr(self, p)()
            msg.append("{:>20s} : {:<30s}".format(p, str(value)))
        msg.append("{:>20s} : {:<30s}".format("mouse_x", str(self.mouse_x)))
        msg.append("{:>20s} : {:<30s}".format("mouse_y", str(self.mouse_y)))
        msg = "\n".join(msg)
        return msg

    def mouseMoveEvent(self, QMouseEvent):
        """
        위젯 안에서의 마우스 움직임이 일어날 때 호출
        :return:
        """
        self.mouse_x = QMouseEvent.x()
        self.mouse_y = QMouseEvent.y()
        self.update()

    def moveEvent(self, QMoveEvent):
        """
        창이 이동했을 경우(이동 중 아님.) 호출
        :param QMoveEvent:
        :return:
        """
        self.update()

    def paintEvent(self, QPaintEvent):
        """
        창을 다시 그려야 할 때 호출
        :param QPaintEvent:
        :return:
        """
        msg = self.get_properties_values(self.properties_list)
        self.lb.setText(msg)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())
