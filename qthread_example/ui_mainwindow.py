# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(358, 303)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnClick = QPushButton(self.centralwidget)
        self.btnClick.setObjectName(u"btnClick")
        self.btnClick.setGeometry(QRect(130, 90, 80, 24))
        self.btnLongTask = QPushButton(self.centralwidget)
        self.btnLongTask.setObjectName(u"btnLongTask")
        self.btnLongTask.setGeometry(QRect(110, 180, 131, 31))
        self.labelCount = QLabel(self.centralwidget)
        self.labelCount.setObjectName(u"labelCount")
        self.labelCount.setGeometry(QRect(130, 50, 81, 21))
        self.labelCount.setAlignment(Qt.AlignCenter)
        self.labelProgress = QLabel(self.centralwidget)
        self.labelProgress.setObjectName(u"labelProgress")
        self.labelProgress.setGeometry(QRect(130, 140, 81, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 358, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btnClick.clicked.connect(MainWindow.slotClickCount)
        self.btnLongTask.clicked.connect(MainWindow.slotLongTask)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnClick.setText(QCoreApplication.translate("MainWindow", u"Click me!!!", None))
        self.btnLongTask.setText(QCoreApplication.translate("MainWindow", u"Long Running Task", None))
        self.labelCount.setText("")
        self.labelProgress.setText("")
    # retranslateUi

