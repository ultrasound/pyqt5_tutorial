# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listwidget3.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(562, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(8, 30, 151, 20))
        self.label.setObjectName("label")
        self.lineEditFoodItem = QtWidgets.QLineEdit(Dialog)
        self.lineEditFoodItem.setGeometry(QtCore.QRect(160, 30, 113, 21))
        self.lineEditFoodItem.setObjectName("lineEditFoodItem")
        self.listWidgetSelectedItem = QtWidgets.QListWidget(Dialog)
        self.listWidgetSelectedItem.setGeometry(QtCore.QRect(280, 30, 256, 192))
        self.listWidgetSelectedItem.setObjectName("listWidgetSelectedItem")
        self.pushButtonAdd = QtWidgets.QPushButton(Dialog)
        self.pushButtonAdd.setGeometry(QtCore.QRect(70, 110, 113, 32))
        self.pushButtonAdd.setObjectName("pushButtonAdd")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Your favourite food item"))
        self.pushButtonAdd.setText(_translate("Dialog", "Add to List"))
