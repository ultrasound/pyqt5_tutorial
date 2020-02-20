#!/usr/bin/env python
# coding: utf-8


import sys

from PyQt5.QtWidgets import QApplication, QDialog

from hotelbooking import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.roomtypes = ['Suite', 'Super Luxury', 'Super Deluxe', 'Ordinary']
        self.add_content()
        self.ui.pushButton.clicked.connect(self.computeRoomRent)

        self.show()

    def add_content(self):
        for i in self.roomtypes:
            self.ui.comboBox.addItem(i)

    def computeRoomRent(self):
        date_selected = self.ui.calendarWidget.selectedDate()
        date_in_string = str(date_selected.toPyDate())
        number_of_day = self.ui.spinBox.value()
        chosen_room_type = self.ui.comboBox.itemText(self.ui.comboBox.currentIndex())
        self.ui.Enteredinfo.setText('Date of reservation: ' + date_in_string + ', Number of days: ' +
                                    str(number_of_day) + ', \nRoom type selected: ' + chosen_room_type)

        room_rent = 0
        if chosen_room_type == "Suite":
            room_rent = 40
        elif chosen_room_type == "Super Luxury":
            room_rent = 30
        elif chosen_room_type == "Super Deluxe":
            room_rent = 20
        elif chosen_room_type == "Ordinary":
            room_rent = 10

        total = room_rent * number_of_day
        self.ui.RoomRentinfo.setText('Room Rent for single day for ' + chosen_room_type + ' type is ' +
                                     str(room_rent) + '$. \nTotal room rent is ' + str(total))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
