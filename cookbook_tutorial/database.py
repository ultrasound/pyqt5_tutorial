# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'database.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 509)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 10, 381, 491))
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.lineEditDBName = QtWidgets.QLineEdit(self.widget)
        self.lineEditDBName.setObjectName("lineEditDBName")
        self.horizontalLayout.addWidget(self.lineEditDBName)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pushButtonCreateDB = QtWidgets.QPushButton(self.widget)
        self.pushButtonCreateDB.setObjectName("pushButtonCreateDB")
        self.verticalLayout.addWidget(self.pushButtonCreateDB)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.lineEditTableName = QtWidgets.QLineEdit(self.widget)
        self.lineEditTableName.setObjectName("lineEditTableName")
        self.horizontalLayout_2.addWidget(self.lineEditTableName)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.lineEditColumnName = QtWidgets.QLineEdit(self.widget)
        self.lineEditColumnName.setObjectName("lineEditColumnName")
        self.verticalLayout_2.addWidget(self.lineEditColumnName)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.comboBoxDataType = QtWidgets.QComboBox(self.widget)
        self.comboBoxDataType.setObjectName("comboBoxDataType")
        self.verticalLayout_3.addWidget(self.comboBoxDataType)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.pushButtonAddColumn = QtWidgets.QPushButton(self.widget)
        self.pushButtonAddColumn.setObjectName("pushButtonAddColumn")
        self.horizontalLayout_3.addWidget(self.pushButtonAddColumn)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.pushButtonCreateTable = QtWidgets.QPushButton(self.widget)
        self.pushButtonCreateTable.setObjectName("pushButtonCreateTable")
        self.verticalLayout_4.addWidget(self.pushButtonCreateTable)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.lineEditEmailAddress = QtWidgets.QLineEdit(self.widget)
        self.lineEditEmailAddress.setObjectName("lineEditEmailAddress")
        self.horizontalLayout_4.addWidget(self.lineEditEmailAddress)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.lineEditPassword = QtWidgets.QLineEdit(self.widget)
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.horizontalLayout_5.addWidget(self.lineEditPassword)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.pushButtonInsertRow = QtWidgets.QPushButton(self.widget)
        self.pushButtonInsertRow.setObjectName("pushButtonInsertRow")
        self.verticalLayout_4.addWidget(self.pushButtonInsertRow)
        self.labelResponse = QtWidgets.QLabel(self.widget)
        self.labelResponse.setText("")
        self.labelResponse.setObjectName("labelResponse")
        self.verticalLayout_4.addWidget(self.labelResponse)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter database name"))
        self.pushButtonCreateDB.setText(_translate("Dialog", "Create Database"))
        self.label_2.setText(_translate("Dialog", " Enter table name"))
        self.label_3.setText(_translate("Dialog", "Column Name"))
        self.label_4.setText(_translate("Dialog", "Data Type"))
        self.pushButtonAddColumn.setText(_translate("Dialog", "Add Column"))
        self.pushButtonCreateTable.setText(_translate("Dialog", "Create Table"))
        self.label_5.setText(_translate("Dialog", "Email Address"))
        self.label_6.setText(_translate("Dialog", "Password"))
        self.pushButtonInsertRow.setText(_translate("Dialog", "Insert Row"))