import logging
import sys
import random
from time import sleep

from PySide2.QtCore import QMutex, QObject, QThread, Signal
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QMainWindow
from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QWidget

balance = 100.0
mutex = QMutex()

class AccountManager(QObject):
    finished = Signal()
    updatedBalance = Signal()

    def withdraw(self, person, amount):
        logging.info("%s wants to withdraw $%.2f...", person, amount)
        global balance

        mutex.lock()
        if balance - amount >= 0:
            sleep(1)
            balance -= amount
            logging.info("-$%.2f accepted", amount)
        else:
            logging.info("-$%.2f rejected", amount)
        logging.info("===Balance===: $%.2f", balance)
        self.updatedBalance.emit()
        mutex.unlock()

        self.finished.emit()

class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
        self.threads = []

    def setupUi(self):
        self.setWindowTitle("Account Manager")
        self.resize(200, 150)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        button = QPushButton("Withdraw Money!")
        button.clicked.connect(self.startThreads)
        self.balanceLabel = QLabel(f"Current Balance: ${balance:,.2f}")
        layout = QVBoxLayout()
        layout.addWidget(self.balanceLabel)
        layout.addWidget(button)
        self.centralWidget.setLayout(layout)

    def createThread(self, person, amount):
        thread = QThread()
        worker = AccountManager()
        worker.moveToThread(thread)
        thread.started.connect(lambda: worker.withdraw(person, amount))
        worker.updatedBalance.connect(self.updateBalance)
        worker.finished.connect(thread.quit)
        worker.finished.connect(worker.deleteLater)
        thread.finished.connect(thread.deleteLater)
        return thread

    def updateBalance(self):
            self.balanceLabel.setText(f"Current Balance: ${balance:,.2f}")

    def startThreads(self):
        self.threads.clear()
        people = {
            "Alice": random.randint(100, 10000) / 100,
            "Bob": random.randint(100, 10000) / 100,
        }
        self.threads = [
            self.createThread(person, amount)
            for person, amount in people.items()
        ]
        for thread in self.threads:
            thread.start()   

if __name__ == '__main__':
    app = QApplication()
    window = Window()
    window.show()
    sys.exit(app.exec_())