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
        self.cursor.execute("SELECT * FROM cadastro_plantas")
        return self.cursor.fetchall()

    def listar2(self):
        self.cursor.execute("SELECT * FROM dados")
        return self.cursor.fetchall()

    def fechar_conexao(self):
        self.cursor.close() 
        self.conexao.close() 

    def update_planta(self, nome_popular, nome_cientifico, planta_id):
        sql = "UPDATE cadastro_plantas SET nome_popular = %s, nome_cientifico = %s WHERE id = %s"
        valores = (nome_popular, nome_cientifico, planta_id)
        self.cursor.execute(sql, valores)
        self.conexao.commit()
        return self.cursor.rowcount > 0

    def update_dados(self, id, luminosidade, umidade, temperatura):
        sql = "UPDATE dados SET luminosidade = %s, umidade = %s, temperatura = %s WHERE id = %s"
        valores = (luminosidade, umidade, temperatura, id)
        self.cursor.execute(sql, valores)
        self.conexao.commit()
        return self.cursor.rowcount > 0

    def delete_dado(self, id):
        try:
            print(f"Tentando deletar o ID: {id}")
            
            sql = "DELETE FROM cadastro_plantas WHERE id = %s"
            self.cursor.execute(sql, [id])
            self.conexao.commit()
            
            if self.cursor.rowcount > 0:
                print("Registro deletado com sucesso!")  
                return True
            else:
                print(f"Nenhum registro foi deletado. Verifique se o ID {id} existe no banco.")  
                return False
        except mysql.connector.Error as err:
            print(f"Erro do MySQL: {err}")
            return False
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return False

