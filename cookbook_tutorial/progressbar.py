# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'progressbar.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(372, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(140, 30, 131, 16))
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(70, 90, 251, 61))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.pushButtonStart = QtWidgets.QPushButton(Dialog)
        self.pushButtonStart.setGeometry(QtCore.QRect(110, 190, 191, 32))
        self.pushButtonStart.setObjectName("pushButtonStart")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Downloading the file"))
        self.pushButtonStart.setText(_translate("Dialog", "Start Donwloading"))
