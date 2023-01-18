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
        self.lineEdit_cpf_cnpj.editingFinished.connect(self.api_consult)
        #########################
    
    ### MENU ANIMATION ###
    def toggleMenu(self):
        width = self.frame_aside.width()
        if width == 0:
            newWidth = 220
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
        if self.comboBox_persona.currentText() == "Jurídica":
            fields = cnpj_consult(self.lineEdit_cpf_cnpj.text())
            self.lineEdit_nome.setText(fields[0])
            self.lineEdit_logradouro.setText(fields[1])
            self.lineEdit_numero.setText(fields[2])
            self.lineEdit_complemento.setText(fields[3])
            self.lineEdit_bairro.setText(fields[4])
            self.lineEdit_municipio.setText(fields[5])
            self.lineEdit_uf.setText(fields[6])
            self.lineEdit_cep.setText(fields[7].replace('.','').replace('-',''))
            self.lineEdit_telefone.setText(fields[8].replace('(','').replace('-','').replace(')',''))
            self.lineEdit_email.setText(fields[9])
        elif self.comboBox_persona.currentText() == 'Física':
            pass
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erro")
            msg.setText("Erro ao cadastrar, selecione uma opção de persona!")
            msg.exec()  
    ###################
    
    ### 

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