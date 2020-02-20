# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calendar.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.dateEdit = QtWidgets.QDateEdit(Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(140, 230, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.calendarWidget = QtWidgets.QCalendarWidget(Dialog)
        self.calendarWidget.setGeometry(QtCore.QRect(50, 20, 304, 173))
        self.calendarWidget.setObjectName("calendarWidget")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
