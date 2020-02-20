# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'radio_button.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.radioButtonFirstClass = QtWidgets.QRadioButton(Dialog)
        self.radioButtonFirstClass.setGeometry(QtCore.QRect(40, 70, 100, 20))
        self.radioButtonFirstClass.setObjectName("radioButtonFirstClass")
        self.radioButtonBusinessClass = QtWidgets.QRadioButton(Dialog)
        self.radioButtonBusinessClass.setGeometry(QtCore.QRect(40, 120, 161, 20))
        self.radioButtonBusinessClass.setObjectName("radioButtonBusinessClass")
        self.radioButtonEconomyClass = QtWidgets.QRadioButton(Dialog)
        self.radioButtonEconomyClass.setGeometry(QtCore.QRect(40, 170, 151, 20))
        self.radioButtonEconomyClass.setObjectName("radioButtonEconomyClass")
        self.labelFare = QtWidgets.QLabel(Dialog)
        self.labelFare.setGeometry(QtCore.QRect(50, 30, 171, 16))
        self.labelFare.setObjectName("labelFare")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.radioButtonFirstClass.setText(_translate("Dialog", "First Class $150"))
        self.radioButtonBusinessClass.setText(_translate("Dialog", "Business Class $125"))
        self.radioButtonEconomyClass.setText(_translate("Dialog", "Economy Class $100"))
        self.labelFare.setText(_translate("Dialog", "Choose the flight type"))
