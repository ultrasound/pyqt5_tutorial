#!/usr/bin/env python
# coding: utf-8

import sys

from PyQt5.QtWidgets import QApplication, QDialog

from singleinheritance import Ui_Dialog


class Student:
    name = ""
    code = ""

    def __init__(self, code, name):
        self.code = code
        self.name = name

    def get_code(self):
        return self.code

    def get_name(self):
        return self.name


class Marks(Student):
    history_marks = 0
    geography_marks = 0

    def __init__(self, code, name, history_marks, geography_marks):
        Student.__init__(self, code, name)
        self.history_makrs = history_marks
        self.geography_marks = geography_marks

    def get_history_marks(self):
        return self.history_marks

    def get_geography_marks(self):
        return self.geography_marks


class MyForm(QDialog):
    def __init__(self):
        super(MyForm, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.ButtonClickMe.clicked.connect(self.disp_message)
        self.show()

    def disp_message(self):
        marks_obj = Marks(self.ui.lineEditCode.text(),
                          self.ui.lineEditName.text(),
                          self.ui.lineEditHistoryMarks.text(),
                          self.ui.lineEditGeographymarks.text())
        self.ui.labelResponse.setText(
            "Code: " + marks_obj.get_code() + ", Geography Marks: " + marks_obj.get_geography_marks()
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())