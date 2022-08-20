import sys
from unittest.result import failfast

from PySide2 import QtCore, QtGui, QtWidgets
from ui_console import Ui_Console

class Console(QtWidgets.QWidget, Ui_Console):
    errorSignal = QtCore.Signal(str) 
    outputSignal = QtCore.Signal(str)
    startSignal = QtCore.Signal(str)
    killSignal = QtCore.Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.txtOutput.setReadOnly(True)

        self.cmd_history = []
        self.cmd_history_index = 0

        self.output = None
        self.error = None

        self.process = QtCore.QProcess()
        self.process.readyReadStandardError.connect(self.slotReadyStdErr)
        self.process.readyReadStandardOutput.connect(self.slotReadyStdOut)
        self.startSignal.connect(self.slotStart)
        self.killSignal.connect(self.slotKill)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Enter or \
            event.key() == QtCore.Qt.Key_Return:
            # Enter key
            if self.process.state() != QtCore.QProcess.NotRunning:   # return if process is still running
                return
            cmd = self.txtCmd.text()
            self.txtCmd.setText('')
            self.cmd_history_index = 0
            self.cmd_history.append(cmd)
            self.startSignal.emit(cmd)
        elif event.modifiers() == QtCore.Qt.ControlModifier and \
            event.key() == QtCore.Qt.Key_Q:
            # Ctrl+Q key
            self.killSignal.emit()
        elif event.key() == QtCore.Qt.Key_Up:
            # Up arrow key
            self.cmd_history_index -= 1
            try:
                self.txtCmd.setText(self.cmd_history[self.cmd_history_index])
            except IndexError:
                self.cmd_history_index += 1
        elif event.key() == QtCore.Qt.Key_Down:
            # Down arrow key
            self.cmd_history_index += 1
            try:
                self.txtCmd.setText(self.cmd_history[self.cmd_history_index])
            except IndexError:
                self.cmd_history_index -= 1

    def slotReadyStdErr(self):
        error = self.process.readAllStandardError().data().decode()
        self.txtOutput.appendPlainText(error)
        self.errorSignal.emit(error)

    def slotReadyStdOut(self):
        result = self.process.readAllStandardOutput().data().decode()
        self.txtOutput.appendPlainText(result)
        self.outputSignal.emit(result)

    def slotStart(self, cmd):
        """Executes a system command.
        """
        self.txtOutput.appendPlainText('> {}'.format(cmd))
        cmdSplitted = cmd.split(' ')
        self.process.setProgram(cmdSplitted[0])
        self.process.setArguments(cmdSplitted[1:])
        self.process.start()

    def slotKill(self):
        self.process.kill()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Console()
    w.show()
    sys.exit(app.exec_())