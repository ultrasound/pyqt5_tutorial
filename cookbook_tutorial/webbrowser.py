# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'webbrowser.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(692, 300)
        self.widget = QtWebEngineWidgets.QWebEngineView(Dialog)
        self.widget.setGeometry(QtCore.QRect(30, 60, 601, 221))
        self.widget.setObjectName("widget")
        self.widget1 = QtWidgets.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(30, 20, 611, 33))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEditURL = QtWidgets.QLineEdit(self.widget1)
        self.lineEditURL.setObjectName("lineEditURL")
        self.horizontalLayout.addWidget(self.lineEditURL)
        self.pushButtonGo = QtWidgets.QPushButton(self.widget1)
        self.pushButtonGo.setObjectName("pushButtonGo")
        self.horizontalLayout.addWidget(self.pushButtonGo)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter URL"))
        self.pushButtonGo.setText(_translate("Dialog", "Go"))
from PyQt5 import QtWebEngineWidgets
