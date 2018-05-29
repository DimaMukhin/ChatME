import socket
import threading
import time
import gui
import sys
from PyQt4 import QtGui, QtCore

class ChatClient(object):

    def __init__(self):
        self.shutDown = False
        self.tLock = threading.Lock()
        self.GUI = None

    def startClient(self):
        self.serverConnect()
        self.runGUI()

    def serverConnect(self):
        server = ('192.168.1.2', 5000)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(server)
        self.client.setblocking(1)
        self.rT = threading.Thread(target = self.tServerInput, args = ('RecvThread', self.client))
        self.rT.start()

    def runGUI(self):
        app = QtGui.QApplication(sys.argv)
        self.GUI = gui.Window(self)
        sys.exit(app.exec_())

    def sendMessage(self, text):
        if text != '':
            self.client.send(text)

    def tServerInput(self, name, sock):
        while not self.shutDown:
            try:
                data = sock.recv(1024)
                self.GUI.printMessage(data)
            except Exception as e:
                print e

    def closeApp(self):
        self.shutDown = True
        self.rT.join()
        self.client.close()

def main():
    client = ChatClient()
    try:
        client.startClient()
    finally:
        client.closeApp()

if __name__=='__main__':
    main()
