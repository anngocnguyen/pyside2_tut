#!/usr/bin/python3

import sys
from tkinter import Toplevel
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QToolBar
from PySide2.QtWidgets import QStatusBar
from PySide2.QtWidgets import QMenu, QMenuBar

class Window(QMainWindow):
    """Window class heritage QMainWindow
    """
    def __init__(self, parent=None):
        """Initializer
        """
        super().__init__(parent)
        self.setWindowTitle('Main Window Example')
        self.setCentralWidget(QLabel(text='This is a label'))   # Central widgets of QMainWindow, this can be a big layout that combine multiple widgets
        self._createMenu()
        self._createStatusbar()
        self._createToolbar()
        
    def _createMenu(self):
        menu = self.menuBar().addMenu('&File') # Menu Bar of QMainWindow
        menu.addAction('&Open', self.close)
        menu.addAction('&Exit', self.close)

    def _createToolbar(self):
        tools = QToolBar()
        tools.addAction('Exit', self.close)
        self.addToolBar(tools)  # Toolbar of QMainWindow

    def _createStatusbar(self):
        status = QStatusBar()
        status.showMessage('This is a status bar')
        self.setStatusBar(status)   # Status bar of QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())