from curses import window
import sys
from time import sleep
from PySide2 import QtGui, QtCore
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow
from ui_mainwindow import Ui_MainWindow

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
        self.progressLabelText = 'Progrss {}/5'
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
        for i in range(5):
            self.labelProgress.setText(self.progressLabelText.format(i))
            sleep(1)

        self.labelProgress.setText('Done')       

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
