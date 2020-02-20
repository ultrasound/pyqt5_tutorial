# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listwidget2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 472)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 101, 20))
        self.label.setObjectName("label")
        self.listWidgetDiagnosis = QtWidgets.QListWidget(Dialog)
        self.listWidgetDiagnosis.setGeometry(QtCore.QRect(130, 10, 256, 192))
        self.listWidgetDiagnosis.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidgetDiagnosis.setObjectName("listWidgetDiagnosis")
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDiagnosis.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDiagnosis.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDiagnosis.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDiagnosis.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDiagnosis.addItem(item)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 220, 111, 20))
        self.label_2.setObjectName("label_2")
        self.listWidgetSelectedTests = QtWidgets.QListWidget(Dialog)
        self.listWidgetSelectedTests.setGeometry(QtCore.QRect(130, 220, 256, 192))
        self.listWidgetSelectedTests.setObjectName("listWidgetSelectedTests")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Diagnosis Tests"))
        __sortingEnabled = self.listWidgetDiagnosis.isSortingEnabled()
        self.listWidgetDiagnosis.setSortingEnabled(False)
        item = self.listWidgetDiagnosis.item(0)
        item.setText(_translate("Dialog", "Urine Analysys $5"))
        item = self.listWidgetDiagnosis.item(1)
        item.setText(_translate("Dialog", "Chest X Ray $100"))
        item = self.listWidgetDiagnosis.item(2)
        item.setText(_translate("Dialog", "Sugar Level test $3"))
        item = self.listWidgetDiagnosis.item(3)
        item.setText(_translate("Dialog", "hemoglobin test $7"))
        item = self.listWidgetDiagnosis.item(4)
        item.setText(_translate("Dialog", "Thyroid Stimulating harmone test $10"))
        self.listWidgetDiagnosis.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("Dialog", "Selected tests are"))
