import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

    def __init__(self, client):
        super(Window, self).__init__()
        self.client = client
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("ChatME")

        self.askName()
        self.home()

    def askName(self):
        text, ok = QtGui.QInputDialog.getText(self, 'Text Input Dialog', 'Enter your name:')
        if ok:
            self.name = text
        else:
            sys.exit()

    def home(self):
        self.textbox = QtGui.QLineEdit(self)
        self.textbox.move(0, 275)
        self.textbox.resize(500, 25)
        self.textbox.returnPressed.connect(self.sendMessage)

        self.logOutput = QtGui.QTextEdit(self)
        self.logOutput.setReadOnly(True)
        self.logOutput.resize(500,273)
        self.logOutput.setLineWrapMode(QtGui.QTextEdit.NoWrap)

        font = self.logOutput.font()
        font.setFamily("Courier")
        font.setPointSize(10)

        self.logOutput.moveCursor(QtGui.QTextCursor.End)
        self.logOutput.setCurrentFont(font)

        self.show()

    def sendMessage(self):
        message = '{}: {}'.format(self.name, str(self.textbox.text()))
        self.client.sendMessage(message)
        self.textbox.setText('')

    def printMessage(self, message):
        self.logOutput.insertPlainText(message + '\n')
        sb = self.logOutput.verticalScrollBar()
        sb.setValue(sb.maximum())
