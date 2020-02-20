#!/usr/bin/env python
# coding: utf-8

import sys

from PyQt5.QtWidgets import QApplication, QDialog
from geolocation.main import GoogleMaps

from googlemap import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super(MyForm, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonSearch.clicked.connect(self.display_details)
        self.show()

    def display_details(self):
        address = str(self.ui.lineEditLocation.text())
        google_maps = GoogleMaps(api_key='AIzaSyCqZcxCYBoZ4ui8ihg02MmR0CLEWzGhZp0')
        location = google_maps.search(location=address)
        my_location = location.first()
        self.ui.labelCity.setText("City: " + str(my_location.city))
        self.ui.labelPostalCode.setText("Postal Code: " + str(my_location.postal_code))
        self.ui.labelLongitude.setText("Longitude: " + str(my_location.lng))
        self.ui.labelLatitude.setText("Latitude: " + str(my_location.lat))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())