#!/usr/bin/python3

import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QPushButton

class Window(QWidget):
    """Window class heritage QMainWindow
    """
    def __init__(self, parent=None):
        """Initializer
        """
        super().__init__(parent)
        self.setWindowTitle('Signal-Slot Example')
        layout = QVBoxLayout()
        self.btn = QPushButton('Greet')
        self.btn.clicked.connect(self.greeting)     # Connect event 'clicked' with function 'greeting'
        self.msg = QLabel('')
        layout.addWidget(self.btn)
        layout.addWidget(self.msg)
        self.setLayout(layout)

    def greeting(self):
        """Slot function
        """
        if self.msg.text():
            self.msg.setText('')
        else:
            self.msg.setText('Hello World')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())