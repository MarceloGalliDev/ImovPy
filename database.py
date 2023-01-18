import sqlite3

class Database:
    def __init__(self, name = "system.db") -> None:
        self.name = name
        
    def connect(self):
        self.connection = sqlite3.connect(self.name)
    
    def disconnect(self):
        try:
            self.connection.close()
        except:
            pass
    
    def create_table_immobile(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Empresas(
                ID INTERGER PRIMARY KEY NOT NULL UNIQUE,
                PERSONA TEXT,
                CNPJ_CPF TEXT,
                NOME_RAZAO_SOCIAL TEXT,
                ENDERECO TEXT,
                NUMERO TEXT,
                COMPLEMENTO TEXT,
                BAIRRO TEXT,
                CIDADE TEXT,
                UF TEXT,
                CEP TEXT,
                TELEFONE TEXT,
                CELULAR TEXT,
                EMAIL TEXT,
                TIPO TEXT,
                STATUS TEXT,
                CARACTERISTICA TEXT,
                VISIBILIDADE TEXT,
                VALOR TEXT,
                DESCRICAO TEXT           
            )          
        """)
    
    def register_immobile(self, fullDataSet):
        input_table = ('PERSONA', 'CNPJ_CPF', 'NOME_RAZAO_SOCIAL', 'ENDERECO', 'NUMERO', 'COMPLEMENTO', 'BAIRRO', 'CIDADE', 'UF', 'CEP', 'TELEFONE', 'CELULAR', 'EMAIL', 'TIPO', 'STATUS', 'CARACTERISTICAS', 'VISIBILIDADE', 'VALOR', 'DESCRICAO')
        
        qtde = ("?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?")
        cursor = self.connection.cursor()
        
        try:
            cursor.execute(f"""INSERT INTO Empresas{input_table} VALUES({qtde})""", fullDataSet)
            self.connection.commit()
            return "OK"
        except:
            return "ERROR"
    
    def select_all_immobile(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM EMPRESAS ORDER BY ID")
            empresas = cursor.fetchall()
            return empresas
        except:
            pass
    
    def delete_immobile(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Empresas WHERE ID = '{id}'")
            self.connection.commit()
            return "Cadastro do imóvel excluído com sucesso!"
        except:
            return "Erro ao excluir registro!"
    
    def update_immobile(self, fullDataSet):
        cursor = self.connection.cursor()
        cursor.execute(f"""UPDATE Empresas set
            ID = '{fullDataSet[0]}',
            PERSONA = '{fullDataSet[1]},
            CNPJ_CPF = '{fullDataSet[2]},
            NOME_RAZAO_SOCIAL = '{fullDataSet[3]},
            ENDERECO = '{fullDataSet[4]},
            NUMERO = '{fullDataSet[5]},
            COMPLEMENTO = '{fullDataSet[6]},
            BAIRRO = '{fullDataSet[7]},
            CIDADE = '{fullDataSet[8]},
            UF = '{fullDataSet[9]},
            CEP = '{fullDataSet[10]},
            TELEFONE = '{fullDataSet[11]},
            CELULAR = '{fullDataSet[12]},
            EMAIL = '{fullDataSet[13]},
            TIPO = '{fullDataSet[14]},
            STATUS = '{fullDataSet[15]},
            CARACTERISTICA = '{fullDataSet[16]},
            VISIBILIDADE = '{fullDataSet[17]},
            VALOR = '{fullDataSet[18]},
            DESCRICAO = '{fullDataSet[19]},
            WHERE ID = '{fullDataSet[0]},                
        """)
        
        self.connection.commit()