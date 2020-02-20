#!/usr/bin/env python
# coding: utf-8

import sys

from PyQt5.QtWidgets import QApplication, QDialog

from muitilevelinheritance import Ui_Dialog


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


class Result(Marks):
    total_marks = 0
    percentage = 0

    def __init__(self, code, name, history_marks, geography_marks):
        Marks.__init__(self, code, name, history_marks, geography_marks)
        self.total_marks = history_marks + geography_marks
        self.percentage = (history_marks + geography_marks) / 200 * 100

    def get_total_marks(self):
        return self.total_marks

    def get_percentage(self):
        return self.percentage


class MyForm(QDialog):
    def __init__(self):
        super(MyForm, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.ButtonClickMe.clicked.connect(self.disp_message)
        self.show()

    def disp_message(self):
        result_obj = Result(self.ui.lineEditCode.text(),
                            self.ui.lineEditName.text(),
                            int(self.ui.lineEditHistoryMarks.text()),
                            int(self.ui.lineEditGeographymarks.text()))
        self.ui.lineEditTotal.setText(str(result_obj.get_total_marks()))
        self.ui.lineEditPercentage.setText(str(result_obj.get_percentage()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
