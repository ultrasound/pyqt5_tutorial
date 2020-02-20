# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checkbox.ui'
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
        self.label.setGeometry(QtCore.QRect(140, 20, 131, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 171, 16))
        self.label_2.setObjectName("label_2")
        self.labelAmount = QtWidgets.QLabel(Dialog)
        self.labelAmount.setGeometry(QtCore.QRect(30, 220, 321, 16))
        self.labelAmount.setText("")
        self.labelAmount.setObjectName("labelAmount")
        self.checkBoxCheese = QtWidgets.QCheckBox(Dialog)
        self.checkBoxCheese.setGeometry(QtCore.QRect(220, 70, 141, 20))
        self.checkBoxCheese.setObjectName("checkBoxCheese")
        self.checkBoxOlives = QtWidgets.QCheckBox(Dialog)
        self.checkBoxOlives.setGeometry(QtCore.QRect(220, 120, 151, 20))
        self.checkBoxOlives.setObjectName("checkBoxOlives")
        self.checkBoxSausages = QtWidgets.QCheckBox(Dialog)
        self.checkBoxSausages.setGeometry(QtCore.QRect(220, 150, 141, 20))
        self.checkBoxSausages.setObjectName("checkBoxSausages")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Regular Pizza $10"))
        self.label_2.setText(_translate("Dialog", "Select your extra toppings"))
        self.checkBoxCheese.setText(_translate("Dialog", "Extra Cheese $1"))
        self.checkBoxOlives.setText(_translate("Dialog", "Extra Olives $1"))
        self.checkBoxSausages.setText(_translate("Dialog", "Extra Sausages $2"))
