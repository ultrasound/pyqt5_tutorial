# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fontdialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.pushButtonFont = QtWidgets.QPushButton(Dialog)
        self.pushButtonFont.setGeometry(QtCore.QRect(130, 30, 113, 32))
        self.pushButtonFont.setObjectName("pushButtonFont")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(50, 100, 291, 161))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtonFont.setText(_translate("Dialog", "Change Font"))
