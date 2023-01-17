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
    