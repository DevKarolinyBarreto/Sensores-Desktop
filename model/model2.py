import mysql.connector

class Model2:
    def __init__(self):
   
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",       
            password="",       
            database="plantas"  
        )
        self.cursor = self.conexao.cursor()  

    def dados_plantas(self, temperatura, luminosidade, umidade):
     
        
        sql = "INSERT INTO dados (temperatura, luminosidade, umidade) VALUES (%s, %s, %s)"
        valores = (temperatura, luminosidade, umidade)
        self.cursor.execute(sql, valores)  
        self.conexao.commit()
        return self.cursor.lastrowid  

    def fechar_conexao(self):
      
        self.cursor.close() 
        self.conexao.close() 
