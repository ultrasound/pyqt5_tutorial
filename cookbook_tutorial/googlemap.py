# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'googlemap.ui'
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
        self.widget.setGeometry(QtCore.QRect(30, 20, 351, 261))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEditLocation = QtWidgets.QLineEdit(self.widget)
        self.lineEditLocation.setObjectName("lineEditLocation")
        self.horizontalLayout.addWidget(self.lineEditLocation)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pushButtonSearch = QtWidgets.QPushButton(self.widget)
        self.pushButtonSearch.setObjectName("pushButtonSearch")
        self.verticalLayout.addWidget(self.pushButtonSearch)
        self.labelCity = QtWidgets.QLabel(self.widget)
        self.labelCity.setText("")
        self.labelCity.setObjectName("labelCity")
        self.verticalLayout.addWidget(self.labelCity)
        self.labelPostalCode = QtWidgets.QLabel(self.widget)
        self.labelPostalCode.setText("")
        self.labelPostalCode.setObjectName("labelPostalCode")
        self.verticalLayout.addWidget(self.labelPostalCode)
        self.labelLongitude = QtWidgets.QLabel(self.widget)
        self.labelLongitude.setText("")
        self.labelLongitude.setObjectName("labelLongitude")
        self.verticalLayout.addWidget(self.labelLongitude)
        self.labelLatitude = QtWidgets.QLabel(self.widget)
        self.labelLatitude.setText("")
        self.labelLatitude.setObjectName("labelLatitude")
        self.verticalLayout.addWidget(self.labelLatitude)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Find out the City, Postal Code, Longitude and latitude"))
        self.label_2.setText(_translate("Dialog", "Enter location"))
        self.pushButtonSearch.setText(_translate("Dialog", "Search"))
