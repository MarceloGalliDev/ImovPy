from PySide6.QtCore import QPropertyAnimation, QEasingCurve
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QTableWidgetItem)
from PySide6.QtGui import QIcon
from ui_main import Ui_MainWindow
import sys
from ui_functions import consulta_cnpj
from database import Database
import pandas as pd
import sqlite3

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("ImovPy by Galli Brothers Inc.")
        appIcon = QIcon(u"")
        self.setWindowIcon(appIcon)
    
    
if __name__ == "__main__":
    db = Database()
    db.connect()
    db.create_table_immobile()
    db.disconnect()
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()