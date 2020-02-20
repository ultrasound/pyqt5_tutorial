# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hotelbooking.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(470, 661)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 20, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 121, 16))
        self.label_2.setObjectName("label_2")
        self.calendarWidget = QtWidgets.QCalendarWidget(Dialog)
        self.calendarWidget.setGeometry(QtCore.QRect(150, 60, 304, 173))
        self.calendarWidget.setObjectName("calendarWidget")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 260, 111, 20))
        self.label_3.setObjectName("label_3")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(150, 260, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(18, 330, 81, 20))
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(140, 320, 91, 32))
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(150, 390, 181, 32))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.Enteredinfo = QtWidgets.QLabel(Dialog)
        self.Enteredinfo.setGeometry(QtCore.QRect(20, 460, 421, 71))
        self.Enteredinfo.setText("")
        self.Enteredinfo.setObjectName("Enteredinfo")
        self.RoomRentinfo = QtWidgets.QLabel(Dialog)
        self.RoomRentinfo.setGeometry(QtCore.QRect(20, 550, 421, 81))
        self.RoomRentinfo.setText("")
        self.RoomRentinfo.setObjectName("RoomRentinfo")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Hotel Room Reservation"))
        self.label_2.setText(_translate("Dialog", "Date of Reservation"))
        self.label_3.setText(_translate("Dialog", "Number of days"))
        self.label_4.setText(_translate("Dialog", "Room type"))
        self.pushButton.setText(_translate("Dialog", "Caculate Room Rent"))
