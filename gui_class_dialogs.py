#!/usr/bin/python3

import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QDialog
from PySide2.QtWidgets import QDialogButtonBox
from PySide2.QtWidgets import QFormLayout
from PySide2.QtWidgets import QLineEdit
from PySide2.QtWidgets import QVBoxLayout

class Dialog(QDialog):
    """Dialog class
    Dialog window is implemented using Object oriented programming
    """

    def __init__(self, parent=None):
        """Initializer of Dialog"""
        super().__init__(parent)
        self.setWindowTitle('Dialog example')
        
        dlgLayout = QVBoxLayout()
        formLayout = QFormLayout()
        formLayout.addRow('Name:', QLineEdit())
        formLayout.addRow('Age:', QLineEdit())
        formLayout.addRow('Job:', QLineEdit())
        dlgLayout.addLayout(formLayout)
        btns = QDialogButtonBox()
        btns.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        dlgLayout.addWidget(btns)
        self.setLayout(dlgLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())

