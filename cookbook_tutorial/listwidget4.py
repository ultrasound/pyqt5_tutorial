# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listwidget4.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(548, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 30, 81, 20))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(100, 30, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButtonAdd = QtWidgets.QPushButton(Dialog)
        self.pushButtonAdd.setGeometry(QtCore.QRect(100, 80, 113, 32))
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(240, 30, 291, 192))
        self.listWidget.setObjectName("listWidget")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(240, 240, 296, 32))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonEdit = QtWidgets.QPushButton(self.widget)
        self.pushButtonEdit.setObjectName("pushButtonEdit")
        self.horizontalLayout.addWidget(self.pushButtonEdit)
        self.pushButtonDelete = QtWidgets.QPushButton(self.widget)
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.horizontalLayout.addWidget(self.pushButtonDelete)
        self.pushButtonDeleteAll = QtWidgets.QPushButton(self.widget)
        self.pushButtonDeleteAll.setObjectName("pushButtonDeleteAll")
        self.horizontalLayout.addWidget(self.pushButtonDeleteAll)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter an item"))
        self.pushButtonAdd.setText(_translate("Dialog", "Add"))
        self.pushButtonEdit.setText(_translate("Dialog", "Edit"))
        self.pushButtonDelete.setText(_translate("Dialog", "Delete"))
        self.pushButtonDeleteAll.setText(_translate("Dialog", "Delete All"))
