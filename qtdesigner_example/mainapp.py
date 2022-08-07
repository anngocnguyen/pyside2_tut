import sys
from PySide2 import QtCore
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow

"""This is example of using ui python file generator
    Run this command to generate ui python file
        pyside2-uic -o ui_mainwindow.py MainWindow.ui
    
"""

from ui_mainwindow import Ui_MainWindow     # Import ui generated python code

class MainWindow(QMainWindow, Ui_MainWindow):
    """Class MainWindow
    Noted that the name of the class is similar to ObjectName on Qt Designer
    """
    def __init__(self, parent=None):
        """Initializer
        """
        super().__init__(parent)
        self.setupUi(self)

    # User need to implement the slot function over here. \
    # Slot-signal connection is already done by Pyside designer
    @QtCore.Slot(int)
    def slotPushButton(self, value):        
        """Slot function slotPushButton
        """
        if self.label.text():
            self.label.setText('')
        else:
            self.label.setText('PUSHED')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())