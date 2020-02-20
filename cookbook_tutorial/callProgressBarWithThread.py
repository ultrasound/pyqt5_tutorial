#!/usr/bin/env python
# coding: utf-8

import sys
import threading
import time

from PyQt5.QtWidgets import QApplication, QDialog

from prograssbarwiththread import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super(MyForm, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()


class MyThread(threading.Thread):
    counter = 0

    def __init__(self, w):
        threading.Thread.__init__(self)
        self.w = w
        self.counter = 0

    def run(self):
        print("Starting " + self.name)
        while self.counter <= 100:
            time.sleep(1)
            self.w.ui.progressBar.setValue(self.counter)
            self.counter += 10
        print("Exiting " + self.name)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    thread1 = MyThread(w)
    thread1.start()
    sys.exit(app.exec_())

