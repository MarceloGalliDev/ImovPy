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
        self.btn_cadastrar.clicked.connect(self.register_fields)
        self.btn_limpar.clicked.connect(self.clear_fields)
        #########################
        
        ### SYSTEM PAGES ###
        self.btn_home.clicked.connect(lambda: self.tabWidget_content.setCurrentWidget(self.page_home))
        self.btn_cadastro.clicked.connect(lambda: self.tabWidget_content.setCurrentWidget(self.page_cadastro))
        self.btn_consultar.clicked.connect(lambda: self.tabWidget_content.setCurrentWidget(self.page_consultar))
        self.btn_contato.clicked.connect(lambda: self.tabWidget_content.setCurrentWidget(self.page_contato))
        ##################### 
    
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
    
    ### REGISTER ###
    def register_fields(self):
        db = Database()
        db.connect()
        
        fullDataSet = (
            self.comboBox_persona.currentText(),
            self.lineEdit_cpf_cnpj.text(),
            self.lineEdit_nome.text(),
            self.lineEdit_logradouro.text(),
            self.lineEdit_numero.text(),
            self.lineEdit_complemento.text(),
            self.lineEdit_bairro.text(),
            self.lineEdit_municipio.text(),
            self.lineEdit_uf.text(),
            self.lineEdit_cep.text(),
            self.lineEdit_telefone.text().strip(),
            self.lineEdit_celular.text().strip(),
            self.lineEdit_email.text(),
            self.comboBox_tipo.currentText(),
            self.comboBox_status.currentText(),
            self.comboBox_caracteristica.currentText(),
            self.comboBox_opcao.currentText(),
            self.lineEdit_valor.text(),
            self.textEdit_descricao.toPlainText(),
        )
        
        resp = db.register_immobile(fullDataSet)
        
        self.immobile_search()
        
        if resp == "OK":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Cadastro")
            msg.setText("Cadastro realizado com sucesso!")
            msg.exec()           
            db.disconnect()
            
            self.label_id.clear()
            self.comboBox_persona.clear(),
            self.lineEdit_cpf_cnpj.clear(),
            self.lineEdit_nome.clear(),
            self.lineEdit_logradouro.clear(),
            self.lineEdit_numero.clear(),
            self.lineEdit_complemento.clear(),
            self.lineEdit_bairro.clear(),
            self.lineEdit_municipio.clear(),
            self.lineEdit_uf.clear(),
            self.lineEdit_cep.clear(),
            self.lineEdit_telefone.clear(),
            self.lineEdit_celular.clear(),
            self.lineEdit_email.clear(),
            self.comboBox_tipo.clear(),
            self.comboBox_status.clear(),
            self.comboBox_caracteristica.clear(),
            self.comboBox_opcao.clear(),
            self.lineEdit_valor.clear(),
            self.textEdit_descricao.clear() 
            return         
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erro")
            msg.setText("Erro ao cadastrar, verifique as informações!")
            msg.exec()
            db.disconnect()
            return
    ###############

    ### CLEAR FIELDS ###
    def clear_fields(self):
            self.comboBox_persona.clear(),
            self.lineEdit_cpf_cnpj.clear(),
            self.lineEdit_nome.clear(),
            self.lineEdit_logradouro.clear(),
            self.lineEdit_numero.clear(),
            self.lineEdit_complemento.clear(),
            self.lineEdit_bairro.clear(),
            self.lineEdit_municipio.clear(),
            self.lineEdit_uf.clear(),
            self.lineEdit_cep.clear(),
            self.lineEdit_telefone.clear(),
            self.lineEdit_celular.clear(),
            self.lineEdit_email.clear(),
            self.comboBox_tipo.clear(),
            self.comboBox_status.clear(),
            self.comboBox_caracteristica.clear(),
            self.comboBox_opcao.clear(),
            self.lineEdit_valor.clear(),
            self.textEdit_descricao.clear() 
    ####################
    
    ### SEARCH ###
    def immobile_search(self):
        db = Database()
        db.connect()
        result = db.select_all_immobile()
              
        self.table_immobile.clearContents()
        self.table_immobile.setRowCount(len(result))
        
        for row, text in enumerate(result):
            for column, data, in enumerate(text):
                self.table_immobile.setItem(row, column, QTableWidgetItem(str(data)))
        
        db.disconnect()
    ############## 
    
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