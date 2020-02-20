#!/usr/bin/env python
# coding: utf-8

import sys
import threading
import time

from PyQt5.QtWidgets import QApplication, QDialog

from progressbarwithcontextmanager import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super(MyForm, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()


class MyThread(threading.Thread):
    counter = 0

    def __init__(self, w, Progressbar):
        threading.Thread.__init__(self)
        self.w = w
        self.counter = 0
        self.progressBar = Progressbar

    def run(self):
        print("Starting " + self.name + "\n")
        with threadLock:
            while self.counter <= 100:
                time.sleep(1)
                self.progressBar.setValue(self.counter)
                self.counter += 10
        print("Exiting " + self.name + "\n")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    thread1 = MyThread(w, w.ui.progressBarFileDownload)
    thread2 = MyThread(w, w.ui.progressBarVirusScan)
    threadLock = threading.Lock()
    threads = []
    thread1.start()
    thread2.start()
    w.exec()
    threads.append(thread1)
    threads.append(thread2)
    for t in threads:
        t.join()

    sys.exit(app.exec_())
