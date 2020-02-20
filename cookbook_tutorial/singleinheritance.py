# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'singlinheritance.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setGeometry(QtCore.QRect(20, 180, 261, 51))
        self.labelResponse.setText("")
        self.labelResponse.setObjectName("labelResponse")
        self.ButtonClickMe = QtWidgets.QPushButton(Dialog)
        self.ButtonClickMe.setGeometry(QtCore.QRect(80, 260, 113, 32))
        self.ButtonClickMe.setObjectName("ButtonClickMe")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(18, 40, 141, 121))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.widget1 = QtWidgets.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(160, 40, 127, 116))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEditCode = QtWidgets.QLineEdit(self.widget1)
        self.lineEditCode.setObjectName("lineEditCode")
        self.verticalLayout_2.addWidget(self.lineEditCode)
        self.lineEditName = QtWidgets.QLineEdit(self.widget1)
        self.lineEditName.setObjectName("lineEditName")
        self.verticalLayout_2.addWidget(self.lineEditName)
        self.lineEditHistoryMarks = QtWidgets.QLineEdit(self.widget1)
        self.lineEditHistoryMarks.setObjectName("lineEditHistoryMarks")
        self.verticalLayout_2.addWidget(self.lineEditHistoryMarks)
        self.lineEditGeographymarks = QtWidgets.QLineEdit(self.widget1)
        self.lineEditGeographymarks.setObjectName("lineEditGeographymarks")
        self.verticalLayout_2.addWidget(self.lineEditGeographymarks)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ButtonClickMe.setText(_translate("Dialog", "Click"))
        self.label.setText(_translate("Dialog", "Student Code"))
        self.label_2.setText(_translate("Dialog", "Student Name"))
        self.label_3.setText(_translate("Dialog", "History Marks"))
        self.label_4.setText(_translate("Dialog", "Geography marks"))
