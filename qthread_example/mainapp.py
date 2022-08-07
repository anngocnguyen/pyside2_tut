from curses import window
import sys
from time import sleep
from PySide2 import QtGui
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow
from ui_mainwindow import Ui_MainWindow
from PySide2.QtCore import QObject, QThread, Signal

class Worker(QObject):
    """Class Worker for long thread
    """
    finished = Signal()     # Define signal finished
    progress = Signal(int)  # Define signal progress this signal also pass info

    def run(self):
        """Implement of long running task
        """
        for i in range(5):
            self.progress.emit(i) # Worker thread emit signal on progress
            sleep(1)
        self.finished.emit()        # Worker thread emit signal on finished

class MainWindow(QMainWindow, Ui_MainWindow):
    """Class MainWindow
    """
    def __init__(self, parent=None):
        """Initializer
        """
        super().__init__(parent)
        self.setupUi(self)

        self.count = 0
        self.countLabelText = 'Count: {}'
        self.progressLabelText = 'Progress {}/5'
        self.labelCount.setText(self.countLabelText.format(self.count))
        self.labelProgress.setText('Done')
    
    def slotClickCount(self):
        """Click Count slot function
        """
        self.count+=1
        self.labelCount.setText(self.countLabelText.format(self.count))

    def slotLongTask(self):
        """Long Task slot function
        """
        self.thread = QThread()     # Create the thread
        self.worker = Worker()      # Create the worker
        self.worker.moveToThread(self.thread)   # Move worker to thread

        # thread started signal -> worker run slot
        self.thread.started.connect(self.worker.run)    
        # worker finished signal -> thread quit slot
        self.worker.finished.connect(self.thread.quit)  
        # worker finished signal -> worker deleteLater slot
        self.worker.finished.connect(self.worker.deleteLater)
        # thread finished signal -> thread deleteLater slot
        self.thread.finished.connect(self.thread.deleteLater)

        # worker progress signal -> slot reportProgress
        self.worker.progress.connect(self.reportProgress)
        # worker progress signal -> slot reportFinish
        self.worker.finished.connect(self.reportFinish)

        self.thread.start()

        self.btnLongTask.setEnabled(False)
        self.thread.finished.connect(
            lambda: self.btnLongTask.setEnabled(True)
        )

    def reportProgress(self, value):
        self.labelProgress.setText(self.progressLabelText.format(value))

    def reportFinish(self):
        self.labelProgress.setText('Done')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
