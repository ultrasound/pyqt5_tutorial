# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'colordialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.pushButtonColor = QtWidgets.QPushButton(Dialog)
        self.pushButtonColor.setGeometry(QtCore.QRect(50, 70, 113, 32))
        self.pushButtonColor.setObjectName("pushButtonColor")
        self.frameColor = QtWidgets.QFrame(Dialog)
        self.frameColor.setGeometry(QtCore.QRect(220, 40, 120, 80))
        self.frameColor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameColor.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameColor.setObjectName("frameColor")
        self.labelColor = QtWidgets.QLabel(Dialog)
        self.labelColor.setGeometry(QtCore.QRect(60, 190, 281, 51))
        self.labelColor.setText("")
        self.labelColor.setObjectName("labelColor")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtonColor.setText(_translate("Dialog", "Choose color"))
