#!/usr/bin/python3

import sys
from tkinter import CENTER

from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QFormLayout

# Create the app
app = QApplication(sys.argv)

# Create Main window and Label
window = QWidget()
window.setWindowTitle('Layout Example')

# Horizontal Layout
# The widgets appear from left to right as the order it is added into layout
# QVBoxLayout is similar to QHBoxLayout but for vertical
layout = QHBoxLayout()
layout.addWidget(QPushButton('Left'))
layout.addWidget(QPushButton('Center'))
layout.addWidget(QPushButton('Right'))

window.setLayout(layout)
window.show()

# Run the app
sys.exit(app.exec_())