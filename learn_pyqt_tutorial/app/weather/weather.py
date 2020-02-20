#!/usr/bin/env python
# coding: utf-8

import os
from urllib.parse import urlencode
from datetime import datetime

import requests
import requests_cache

from PyQt5 import uic
from PyQt5.QtCore import QObject, pyqtSignal, QRunnable, pyqtSlot, QThreadPool
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QPixmap

qtcreator_file = "weather.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)
OPENWEATHERMAP_API_KEY = '484ec8617691976dde3a2ea4e93b85f2'
LOCATION = {"Korea": ['Seoul', 'Busan'],
            "Thailand": ['Bangkok', 'Chiang Mai'],
            "Laos": ['Vientiane']}

requests_cache.install_cache('weather', backend='sqlite', expire_after=180)


def from_ts_to_time_of_day(ts):
    dt = datetime.fromtimestamp(ts)
    return dt.strftime("%I%p").lstrip("0")


class WorkerSignals(QObject):
    """
    Defines the signals available from a running worker thread
    """
    finished = pyqtSignal()
    error = pyqtSignal(str)
    result = pyqtSignal(dict, dict)


class WeatherWorker(QRunnable):
    """
    Worker thread for weather updates
    """
    signals = WorkerSignals()
    is_interrupted = False

    def __init__(self, location):
        super(WeatherWorker, self).__init__()
        self.location = location

    @pyqtSlot()
    def run(self):
        try:
            params = dict(
                q=self.location,
                appid=OPENWEATHERMAP_API_KEY
            )

            url = 'http://api.openweathermap.org/data/2.5/weather?%s&units=metric' % urlencode(params)
            r = requests.get(url)
            weather = r.json()

            # Check if we had a failure (the forecast will fail in the same way).
            if weather['cod'] != 200:
                raise Exception(weather['message'])

            url = 'http://api.openweathermap.org/data/2.5/forecast?%s&units=metric' % urlencode(params)
            r = requests.get(url)
            forecast = r.json()

            self.signals.result.emit(weather, forecast)
        except Exception as e:
            self.signals.error.emit(str(e))
        finally:
            self.signals.finished.emit()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        for country in LOCATION.keys():
            self.comboBoxCountry.addItem(country)
        for city in LOCATION[self.comboBoxCountry.currentText()]:
            self.comboBoxCity.addItem(city)

        self.comboBoxCountry.currentTextChanged.connect(self.set_city)
        self.pushButton.pressed.connect(self.update_weather)

        self.threadpool = QThreadPool()
        self.show()

    def set_city(self, country):
        self.comboBoxCity.clear()
        for city in LOCATION[country]:
            self.comboBoxCity.addItem(city)

    def update_weather(self):
        location = self.comboBoxCity.currentText() + "," + self.comboBoxCountry.currentText()
        worker = WeatherWorker(location)
        worker.signals.result.connect(self.weather_result)
        worker.signals.error.connect(self.alert)
        self.threadpool.start(worker)

    def alert(self, message):
        QMessageBox.warning(self, "Warning", message)

    def weather_result(self, weather, forecasts):
        self.latitudeLabel.setText("%.2f °" % weather['coord']['lat'])
        self.longitudeLabel.setText("%.2f °" % weather['coord']['lon'])

        self.windLabel.setText("%.2f m/s" % weather['wind']['speed'])

        self.temperatureLabel.setText("%.1f °C" % weather['main']['temp'])
        self.pressureLabel.setText("%d" % weather['main']['pressure'])
        self.humidityLabel.setText("%d" % weather['main']['humidity'])

        self.weatherLabel.setText("%s (%s)" % (
            weather['weather'][0]['main'],
            weather['weather'][0]['description']
        ))

        self.set_weather_icon(self.weatherIcon, weather['weather'])

        for n, forecast in enumerate(forecasts['list'][:5], 1):
            getattr(self, 'forecastTime%d' % n).setText(from_ts_to_time_of_day(forecast['dt']))
            self.set_weather_icon(getattr(self, 'forecastIcon%d' % n), forecast['weather'])
            getattr(self, 'forecastTemp%d' % n).setText("%.1f °C" % forecast['main']['temp'])

    def set_weather_icon(self, label, weather):
        label.setPixmap(
            QPixmap(os.path.join('images', "%s.png" % weather[0]['icon']))
        )


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec_()
