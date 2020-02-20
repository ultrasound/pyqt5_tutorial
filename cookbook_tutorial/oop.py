# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'oop.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 50, 111, 16))
        self.label.setObjectName("label")
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setGeometry(QtCore.QRect(60, 120, 59, 16))
        self.labelResponse.setObjectName("labelResponse")
        self.lineEditName = QtWidgets.QLineEdit(Dialog)
        self.lineEditName.setGeometry(QtCore.QRect(200, 50, 113, 21))
        self.lineEditName.setObjectName("lineEditName")
        self.pushButtonClickMe = QtWidgets.QPushButton(Dialog)
        self.pushButtonClickMe.setGeometry(QtCore.QRect(150, 210, 113, 32))
        self.pushButtonClickMe.setObjectName("pushButtonClickMe")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter your name"))
        self.labelResponse.setText(_translate("Dialog", "TextLabel"))
        self.pushButtonClickMe.setText(_translate("Dialog", "Click"))
