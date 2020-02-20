# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(305, 198)
        self.labelFirstNumber = QtWidgets.QLabel(Dialog)
        self.labelFirstNumber.setGeometry(QtCore.QRect(30, 20, 121, 16))
        self.labelFirstNumber.setObjectName("labelFirstNumber")
        self.labelSecondNumber = QtWidgets.QLabel(Dialog)
        self.labelSecondNumber.setGeometry(QtCore.QRect(30, 70, 141, 16))
        self.labelSecondNumber.setObjectName("labelSecondNumber")
        self.labelResult = QtWidgets.QLabel(Dialog)
        self.labelResult.setGeometry(QtCore.QRect(30, 160, 261, 21))
        self.labelResult.setText("")
        self.labelResult.setObjectName("labelResult")
        self.lineEditFirstNumber = QtWidgets.QLineEdit(Dialog)
        self.lineEditFirstNumber.setGeometry(QtCore.QRect(180, 20, 113, 21))
        self.lineEditFirstNumber.setObjectName("lineEditFirstNumber")
        self.lineEditSecondNumber = QtWidgets.QLineEdit(Dialog)
        self.lineEditSecondNumber.setGeometry(QtCore.QRect(180, 70, 113, 21))
        self.lineEditSecondNumber.setObjectName("lineEditSecondNumber")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(30, 120, 261, 32))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonPlus = QtWidgets.QPushButton(self.widget)
        self.pushButtonPlus.setObjectName("pushButtonPlus")
        self.horizontalLayout.addWidget(self.pushButtonPlus)
        self.pushButtonSubtract = QtWidgets.QPushButton(self.widget)
        self.pushButtonSubtract.setObjectName("pushButtonSubtract")
        self.horizontalLayout.addWidget(self.pushButtonSubtract)
        self.pushButtonMultiply = QtWidgets.QPushButton(self.widget)
        self.pushButtonMultiply.setObjectName("pushButtonMultiply")
        self.horizontalLayout.addWidget(self.pushButtonMultiply)
        self.pushButtonDivide = QtWidgets.QPushButton(self.widget)
        self.pushButtonDivide.setObjectName("pushButtonDivide")
        self.horizontalLayout.addWidget(self.pushButtonDivide)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelFirstNumber.setText(_translate("Dialog", "Enter First Number"))
        self.labelSecondNumber.setText(_translate("Dialog", "Enter second Number"))
        self.pushButtonPlus.setText(_translate("Dialog", "+"))
        self.pushButtonSubtract.setText(_translate("Dialog", "-"))
        self.pushButtonMultiply.setText(_translate("Dialog", "X"))
        self.pushButtonDivide.setText(_translate("Dialog", "/"))
