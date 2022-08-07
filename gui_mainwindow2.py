#!/usr/bin/python3

import sys
from curses import window
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt

class MainWindow(QMainWindow):
    """Main Window class
    """
    def __init__(self, parent=None):
        """Intializer
        """
        super().__init__(parent)
        self.setWindowTitle('Main Window Example')
        self.resize(400, 200)

        # Create Central Widget as a Label, it can be any QtWidgets
        # Normally, put a layout into this place and that layout has a lot of QtWidgets in that
        self.ctrlWidget = QLabel('Hello World')
        self.ctrlWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.ctrlWidget)

        self._creatAction()     # Create actions
        self._createMenuBar()   # Create Menu Bar
        self._createToolBar()   # Create Tool Bar
        self._createContextMenu()   # Create Context Menu

    def _createMenuBar(self):
        """Menu bar Creator
        """
        menuBar = QMenuBar(self)            # Create menu bar menuBar
        fileMenu = QMenu('&File', self)     # Create menu fileMenu
        fileMenu.addAction(self.newAction)
        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.saveAction)
        fileMenu.addAction(self.exitAction)
        editMenu = QMenu('&Edit', self)     # Create menu editMenu
        editMenu.addAction(self.copyAction)        
        editMenu.addAction(self.pasteAction)        
        editMenu.addAction(self.cutAction)
        findMenu = QMenu('Find & Replace')  # Create submenu findMenu that will add to editMenu
        findMenu.addAction('Find...')
        findMenu.addAction('Replace...')
        editMenu.addMenu(findMenu)
        helpMenu = QMenu('&Help', self)     # Create menu helpMenu
        helpMenu.addAction(self.helpAction)        
        helpMenu.addAction(self.aboutAction)
        menuBar.addMenu(fileMenu)           # Add menu fileMenu to menuBar
        menuBar.addMenu(editMenu)
        menuBar.addMenu(helpMenu)
        self.setMenuBar(menuBar)

    def _createToolBar(self):
        """Tool bar Creator
        """
        fileToolBar = QToolBar('File', self)    # fileToolBar
        fileToolBar.addAction(self.newAction)
        fileToolBar.addAction(self.openAction)
        fileToolBar.addAction(self.saveAction)
        self.addToolBar(fileToolBar)
        editToolBar = QToolBar('Edit', self)    # editToolBar
        editToolBar.addAction(self.exitAction)
        editToolBar.addAction(self.copyAction)
        editToolBar.addAction(self.pasteAction)
        self.addToolBar(editToolBar)
        helpToolBar = QToolBar('Help', self)    # helpToolBar
        self.addToolBar(helpToolBar)

    def _creatAction(self):
        """Action Creator
        """
        self.newAction = QAction('&New', self)              # Create action
        self.openAction = QAction('&Open...', self)
        self.saveAction = QAction('&Save', self)
        self.exitAction = QAction('&Exit', self)
        self.copyAction = QAction('&Copy', self)
        self.pasteAction = QAction('&Paste', self)
        self.cutAction = QAction('&Cut', self)
        self.helpAction = QAction('&Help', self)
        self.aboutAction = QAction('&About', self)
        self.newAction.triggered.connect(self.newFile)      # Connect action event with slot
        self.openAction.triggered.connect(self.openFile)

    def _createContextMenu(self):
        """Context Menu creator
        """
        self.ctrlWidget.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.ctrlWidget.addAction(self.newAction)
        self.ctrlWidget.addAction(self.openAction)
        self.ctrlWidget.addAction(self.saveAction)
        self.ctrlWidget.addAction(self.copyAction)
        self.ctrlWidget.addAction(self.pasteAction)        
        self.ctrlWidget.addAction(self.cutAction)

    def newFile(self):
        """New File slot function
        """
        self.ctrlWidget.setText('FILE')

    def openFile(self):
        self.ctrlWidget.setText('OPEN')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())