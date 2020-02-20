# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'combox.ui'
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
        self.label.setGeometry(QtCore.QRect(30, 40, 161, 16))
        self.label.setObjectName("label")
        self.labelAccountType = QtWidgets.QLabel(Dialog)
        self.labelAccountType.setGeometry(QtCore.QRect(40, 250, 311, 16))
        self.labelAccountType.setText("")
        self.labelAccountType.setObjectName("labelAccountType")
        self.comboBoxAccountType = QtWidgets.QComboBox(Dialog)
        self.comboBoxAccountType.setGeometry(QtCore.QRect(210, 40, 91, 32))
        self.comboBoxAccountType.setObjectName("comboBoxAccountType")
        self.comboBoxAccountType.addItem("")
        self.comboBoxAccountType.addItem("")
        self.comboBoxAccountType.addItem("")
        self.comboBoxAccountType.addItem("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Select your account type"))
        self.comboBoxAccountType.setItemText(0, _translate("Dialog", "Saving Account"))
        self.comboBoxAccountType.setItemText(1, _translate("Dialog", "Current Account"))
        self.comboBoxAccountType.setItemText(2, _translate("Dialog", "Recurring Deposit Account"))
        self.comboBoxAccountType.setItemText(3, _translate("Dialog", "Fixed Deposit Account"))
