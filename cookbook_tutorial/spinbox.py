# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spinbox.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(452, 175)
        self.labelTotalAmount = QtWidgets.QLabel(Dialog)
        self.labelTotalAmount.setGeometry(QtCore.QRect(310, 140, 121, 16))
        self.labelTotalAmount.setText("")
        self.labelTotalAmount.setObjectName("labelTotalAmount")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(40, 90, 394, 23))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelSugarPrice = QtWidgets.QLabel(self.widget)
        self.labelSugarPrice.setObjectName("labelSugarPrice")
        self.horizontalLayout.addWidget(self.labelSugarPrice)
        self.lineEditSugarPrice = QtWidgets.QLineEdit(self.widget)
        self.lineEditSugarPrice.setObjectName("lineEditSugarPrice")
        self.horizontalLayout.addWidget(self.lineEditSugarPrice)
        self.doubleSpinBoxSugarWeight = QtWidgets.QDoubleSpinBox(self.widget)
        self.doubleSpinBoxSugarWeight.setObjectName("doubleSpinBoxSugarWeight")
        self.horizontalLayout.addWidget(self.doubleSpinBoxSugarWeight)
        self.lineEditSugarAmount = QtWidgets.QLineEdit(self.widget)
        self.lineEditSugarAmount.setEnabled(False)
        self.lineEditSugarAmount.setObjectName("lineEditSugarAmount")
        self.horizontalLayout.addWidget(self.lineEditSugarAmount)
        self.widget1 = QtWidgets.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(40, 40, 375, 23))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelBookPrice = QtWidgets.QLabel(self.widget1)
        self.labelBookPrice.setObjectName("labelBookPrice")
        self.horizontalLayout_2.addWidget(self.labelBookPrice)
        self.lineEditBookPrice = QtWidgets.QLineEdit(self.widget1)
        self.lineEditBookPrice.setObjectName("lineEditBookPrice")
        self.horizontalLayout_2.addWidget(self.lineEditBookPrice)
        self.spinBoxBookQty = QtWidgets.QSpinBox(self.widget1)
        self.spinBoxBookQty.setObjectName("spinBoxBookQty")
        self.horizontalLayout_2.addWidget(self.spinBoxBookQty)
        self.lineEditBookAmount = QtWidgets.QLineEdit(self.widget1)
        self.lineEditBookAmount.setEnabled(False)
        self.lineEditBookAmount.setObjectName("lineEditBookAmount")
        self.horizontalLayout_2.addWidget(self.lineEditBookAmount)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelSugarPrice.setText(_translate("Dialog", "Sugar Price"))
        self.labelBookPrice.setText(_translate("Dialog", "Book Price"))
