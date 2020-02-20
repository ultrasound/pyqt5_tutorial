#!/usr/bin/env python
# coding: utf-8

import sys
import asyncio

from PyQt5.QtWidgets import QApplication, QDialog
from quamash import QEventLoop

from progressbarwithasync import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super(MyForm, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButtonStart.clicked.connect(self.invokeAsync)
        self.show()

    def invokeAsync(self):
        asyncio.ensure_future(self.updt(0.5, self.ui.progressBarFileDownload))
        asyncio.ensure_future(self.updt(1, self.ui.progressBarVirusScan))

    @staticmethod
    async def updt(delay, ProgressBar):
        for i in range(101):
            await asyncio.sleep(1)
            ProgressBar.setValue(i)

        def stopper(loop):
            loop.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)
    w = MyForm()
    w.exec()
    with loop:
        loop.run_forever()
        loop.close()
    sys.exit(app.exec_())