# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lcdnumber.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(30, 40, 211, 91))
        self.lcdNumber.setObjectName("lcdNumber")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
