# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'progressbarwithtwothreads.ui'
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
        self.widget.setGeometry(QtCore.QRect(40, 30, 321, 94))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.progressBarFileDownload = QtWidgets.QProgressBar(self.widget)
        self.progressBarFileDownload.setProperty("value", 0)
        self.progressBarFileDownload.setObjectName("progressBarFileDownload")
        self.verticalLayout.addWidget(self.progressBarFileDownload)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.progressBarVirusScan = QtWidgets.QProgressBar(self.widget)
        self.progressBarVirusScan.setProperty("value", 0)
        self.progressBarVirusScan.setObjectName("progressBarVirusScan")
        self.verticalLayout.addWidget(self.progressBarVirusScan)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Downloading the file"))
        self.label_2.setText(_translate("Dialog", "Scanning for Virus"))
