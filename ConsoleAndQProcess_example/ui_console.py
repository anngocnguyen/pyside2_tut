# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'console.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Console(object):
    def setupUi(self, Console):
        if not Console.objectName():
            Console.setObjectName(u"Console")
        Console.resize(400, 300)
        Console.setInputMethodHints(Qt.ImhNone)
        self.gridLayoutWidget = QWidget(Console)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 381, 281))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.txtOutput = QPlainTextEdit(self.gridLayoutWidget)
        self.txtOutput.setObjectName(u"txtOutput")

        self.gridLayout.addWidget(self.txtOutput, 0, 0, 1, 2)

        self.txtCmd = QLineEdit(self.gridLayoutWidget)
        self.txtCmd.setObjectName(u"txtCmd")

        self.gridLayout.addWidget(self.txtCmd, 2, 0, 1, 2)


        self.retranslateUi(Console)

        QMetaObject.connectSlotsByName(Console)
    # setupUi

    def retranslateUi(self, Console):
        Console.setWindowTitle(QCoreApplication.translate("Console", u"Console", None))
    # retranslateUi

