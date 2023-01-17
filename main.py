from PySide6.QtCore import QPropertyAnimation, QEasingCurve
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QTableWidgetItem)
from PySide6.QtGui import QIcon
from ui_imovpy import Ui_MainWindow
import sys
from ui_functions import cnpj_consult
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
        
        ### BUTTONS FUNCTIONS ###
        self.btn_toggle_button.clicked.connect(self.toggleMenu)
        #########################
    
    ### MENU ANIMATION ###
    def toggleMenu(self):
        width = self.frame_aside.width()
        
        if width == 0:
            newWidth = 200
        else:
            newWidth = 0
        
        self.animation = QPropertyAnimation(self.frame_aside, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()
    ######################
    
    ### API CONSULT ###
    def api_consult(self):
        if self.comboBox_persona.setText("Jurídica"):
            
    ###################

### CONNECTION ###    
if __name__ == "__main__":
    db = Database()
    db.connect()
    db.create_table_immobile()
    db.disconnect()
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
###################