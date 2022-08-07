#!/usr/bin/python3

import sys
from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QWidget

# Create the app
app = QApplication(sys.argv)

# Create Main window and Label
window = QWidget()
window.setWindowTitle('Hello world window')
window.setGeometry(100, 100, 280, 80)
window.move(60, 15)
helloLabel = QLabel(text='Hello World Label', parent=window)    # This label is inside window because
helloLabel.move(60,15)

# Show Window
window.show()

# Run apps
sys.exit(app.exec_())