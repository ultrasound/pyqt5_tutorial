#!/usr/bin/env python
# coding: utf-8

import sys, time
from threading import Thread
import socket

from PyQt5.QtWidgets import QApplication, QDialog

from serverside import Ui_Dialog

conn = None


class Window(QDialog):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.textEditMessage = self.ui.textEditMessages

        self.show()

    def disp_message(self):
        text = self.ui.lineEditMessage.text()
        global conn
        conn.send(text.encode('utf-8'))
        self.ui.textEditMessages.append("Server: " + self.ui.lineEditMessage.text())
        self.ui.lineEditMessage.setText('')


class ServerThread(Thread):
    def __init__(self, window):
        Thread.__init__(self)
        self.window = window

    def run(self):
        TCP_IP = '0.0.0.0'
        TCP_PORT = 80
        BUFFER_SIZE = 1024
        tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tcpServer.bind((TCP_IP, TCP_PORT))
        threads = []
        tcpServer.listen(4)
        while True:
            global conn
            (conn, (ip, port)) = tcpServer.accept()
            newthread = ClientThread(ip, port, window)
            newthread.start()
            threads.append(newthread)

            for t in threads:
                t.join()


class ClientThread(Thread):
    def __init__(self, ip, port, window):
        Thread.__init__(self)
        self.window = window
        self.ip = ip
        self.port = port

    def run(self):
        while True:
            global conn
            data = conn.recv(1024)
            window.textEditMessages.append("Client: " + data.decode("utf-8"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    serverThread = ServerThread(window)
    serverThread.start()
    window.exec()
    sys.exit(app.exec_())