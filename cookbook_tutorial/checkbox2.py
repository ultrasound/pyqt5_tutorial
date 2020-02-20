# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checkbox2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(408, 393)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 20, 59, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 130, 141, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 240, 121, 16))
        self.label_3.setObjectName("label_3")
        self.labelAmount = QtWidgets.QLabel(Dialog)
        self.labelAmount.setGeometry(QtCore.QRect(30, 330, 361, 31))
        self.labelAmount.setText("")
        self.labelAmount.setObjectName("labelAmount")
        self.groupBoxIceCreams = QtWidgets.QGroupBox(Dialog)
        self.groupBoxIceCreams.setGeometry(QtCore.QRect(210, 70, 194, 125))
        self.groupBoxIceCreams.setCheckable(True)
        self.groupBoxIceCreams.setObjectName("groupBoxIceCreams")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBoxIceCreams)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBoxChocolateChips = QtWidgets.QCheckBox(self.groupBoxIceCreams)
        self.checkBoxChocolateChips.setObjectName("checkBoxChocolateChips")
        self.verticalLayout.addWidget(self.checkBoxChocolateChips)
        self.checkBoxCookieDough = QtWidgets.QCheckBox(self.groupBoxIceCreams)
        self.checkBoxCookieDough.setObjectName("checkBoxCookieDough")
        self.verticalLayout.addWidget(self.checkBoxCookieDough)
        self.checkBoxChocolateAlmond = QtWidgets.QCheckBox(self.groupBoxIceCreams)
        self.checkBoxChocolateAlmond.setObjectName("checkBoxChocolateAlmond")
        self.verticalLayout.addWidget(self.checkBoxChocolateAlmond)
        self.checkBoxRockyRoad = QtWidgets.QCheckBox(self.groupBoxIceCreams)
        self.checkBoxRockyRoad.setObjectName("checkBoxRockyRoad")
        self.verticalLayout.addWidget(self.checkBoxRockyRoad)
        self.groupBoxDrinks = QtWidgets.QGroupBox(Dialog)
        self.groupBoxDrinks.setGeometry(QtCore.QRect(210, 200, 105, 104))
        self.groupBoxDrinks.setCheckable(True)
        self.groupBoxDrinks.setObjectName("groupBoxDrinks")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBoxDrinks)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBoxCoffee = QtWidgets.QCheckBox(self.groupBoxDrinks)
        self.checkBoxCoffee.setObjectName("checkBoxCoffee")
        self.verticalLayout_2.addWidget(self.checkBoxCoffee)
        self.checkBoxSoda = QtWidgets.QCheckBox(self.groupBoxDrinks)
        self.checkBoxSoda.setObjectName("checkBoxSoda")
        self.verticalLayout_2.addWidget(self.checkBoxSoda)
        self.checkBoxTea = QtWidgets.QCheckBox(self.groupBoxDrinks)
        self.checkBoxTea.setObjectName("checkBoxTea")
        self.verticalLayout_2.addWidget(self.checkBoxTea)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Menu"))
        self.label_2.setText(_translate("Dialog", "Select your IceCream"))
        self.label_3.setText(_translate("Dialog", "Select your drink"))
        self.groupBoxIceCreams.setTitle(_translate("Dialog", "IceCreams"))
        self.checkBoxChocolateChips.setText(_translate("Dialog", "Mint Chocolate Chips $4"))
        self.checkBoxCookieDough.setText(_translate("Dialog", "Cookie Dough $2"))
        self.checkBoxChocolateAlmond.setText(_translate("Dialog", "Chocolate Almond $3"))
        self.checkBoxRockyRoad.setText(_translate("Dialog", "Rocky Road $5"))
        self.groupBoxDrinks.setTitle(_translate("Dialog", "Drinks"))
        self.checkBoxCoffee.setText(_translate("Dialog", "Coffee $2"))
        self.checkBoxSoda.setText(_translate("Dialog", "Soda $3"))
        self.checkBoxTea.setText(_translate("Dialog", "Tea $1"))
