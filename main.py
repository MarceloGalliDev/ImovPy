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
        self.btn_gerar_excel.clicked.connect(self.create_excel)
        self.btn_alterar.clicked.connect(self.update_immobile)
        self.btn_excluir.clicked.connect(self.delete_row)
        #########################
        
        ### SYSTEM PAGES ########
        self.btn_home.clicked.connect(lambda: self.tabWidget_content.setCurrentWidget(self.page_home))
        self.btn_cadastro.clicked.connect(lambda: self.tabWidget_content.setCurrentWidget(self.page_cadastro))
        self.btn_consultar.clicked.connect(lambda: self.tabWidget_content.setCurrentWidget(self.page_consultar))
        self.btn_contato.clicked.connect(lambda: self.tabWidget_content.setCurrentWidget(self.page_contato))
        #########################
        
        self.immobile_search()
    
    ### MENU ANIMATION ##########
    def toggleMenu(self):
        width = self.frame_aside.width()
        if width == 0:
            newWidth = 220
        else:
            newWidth = 0
        
        self.animation = QPropertyAnimation(self.frame_aside, b"minimumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()
    #############################
    
    ### API CONSULT #############
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
    #############################
    
    ### REGISTER ################
    def register_fields(self):
        db = Database()
        db.connect()
        
        fullDataSet = (
            self.lineEdit_id.text(),
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
            self.lineEdit_descricao.text()
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
            
            self.lineEdit_id.clear()
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
            self.lineEdit_valor.clear(),
            self.lineEdit_descricao.clear() 
            return         
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erro")
            msg.setText("Erro ao cadastrar, verifique as informações!")
            msg.exec()
            db.disconnect()
            return
    #############################

    ### CLEAR FIELDS ############
    def clear_fields(self):
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
            self.lineEdit_valor.clear(),
            self.textEdit_descricao.clear() 
    #############################
    
    ### SEARCH ##################
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
    #############################
    
    ### UPDATE ##################
    def update_immobile(self):
        dados = []
        update_dados = []

        for row in range(self.table_immobile.rowCount()):
            for column in range(self.table_immobile.columnCount()):
                dados.append(self.table_immobile.item(row, column).text())
            update_dados.append(dados)
            dados = []
        
        db = Database()
        db.connect()
        
        for emp in update_dados:
            db.update_immobile(tuple(emp))
        db.disconnect()
        
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Atualização de dados")
        msg.setText("Atualização realizada com sucesso!")
        msg.exec()
        
        self.table_immobile.reset()
        self.immobile_search()
    #############################
    
    ### DELETE ROW ##############
    def delete_row(self):
        db = Database()
        db.connect()
        
        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Este registro será excluído!")
        msg.setInformativeText("Você tem certeza que deseja excluir esse registro?")
        msg.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
        resp = msg.exec()
        
        if resp == QMessageBox.Yes:
            id = self.table_immobile.selectionModel().currentIndex().siblingAtColumn(0).data()
            result = db.delete_immobile(id)
            self.immobile_search()
            
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Excluir")
            msg.setText(result)
            msg.exec()
            
            db.disconnect()
        
        db.disconnect() 
    #############################
    
    ### CREATE EXCEL ############
    def create_excel(self):
        cnx = sqlite3.connect("system.db")
        
        empresas = pd.read_sql_query("""SELECT * FROM Empresas""", cnx) 
        empresas.to_excel("Empresas.xlsx", sheet_name="empresas", index=False)
        
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Exccel")
        msg.setText("Relatório excel gerado com sucesso!")
        msg.exec()                  
    #############################
    
### CONNECTION ##################    
if __name__ == "__main__":
    db = Database()
    db.connect()
    db.create_table_immobile()
    db.disconnect()
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
#################################