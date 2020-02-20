# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serverside.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(60, 20, 258, 261))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.textEditMessages = QtWidgets.QTextEdit(self.widget)
        self.textEditMessages.setObjectName("textEditMessages")
        self.verticalLayout.addWidget(self.textEditMessages)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEditMessage = QtWidgets.QLineEdit(self.widget)
        self.lineEditMessage.setObjectName("lineEditMessage")
        self.horizontalLayout.addWidget(self.lineEditMessage)
        self.pushButtonSend = QtWidgets.QPushButton(self.widget)
        self.pushButtonSend.setObjectName("pushButtonSend")
        self.horizontalLayout.addWidget(self.pushButtonSend)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Server"))
        self.pushButtonSend.setText(_translate("Dialog", "Send"))
