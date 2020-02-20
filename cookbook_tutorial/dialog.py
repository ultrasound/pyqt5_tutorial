# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setGeometry(QtCore.QRect(20, 40, 111, 16))
        self.labelResponse.setObjectName("labelResponse")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 90, 59, 16))
        self.label.setObjectName("label")
        self.lineEditName = QtWidgets.QLineEdit(Dialog)
        self.lineEditName.setGeometry(QtCore.QRect(150, 40, 191, 21))
        self.lineEditName.setObjectName("lineEditName")
        self.ButtonClickMe = QtWidgets.QPushButton(Dialog)
        self.ButtonClickMe.setGeometry(QtCore.QRect(170, 140, 113, 32))
        self.ButtonClickMe.setObjectName("ButtonClickMe")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelResponse.setText(_translate("Dialog", "Enter Your name"))
        self.label.setText(_translate("Dialog", "TextLabel"))
        self.ButtonClickMe.setText(_translate("Dialog", "Click"))
