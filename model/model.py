import mysql.connector

class Model:
    def __init__(self):
      
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",       
            password="",       
            database="plantas"  
        )
        self.cursor = self.conexao.cursor()  

    def inserir_plantas(self, nome_popular, nome_cientifico, imagem_path):
       
        sql = "INSERT INTO cadastro_plantas (nome_popular, nome_cientifico, imagem_path) VALUES (%s, %s, %s)"
        valores = (nome_popular, nome_cientifico, imagem_path)
        self.cursor.execute(sql, valores)  
        self.conexao.commit()
        return self.cursor.lastrowid  


    def listar(self):
        self.cursor.execute("select * from cadastro_plantas")
        return self.cursor.fetchall()


    def fechar_conexao(self):
      
        self.cursor.close() 
        self.conexao.close() 
