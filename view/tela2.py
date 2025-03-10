import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QFileDialog, QMessageBox
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt

from controller.controller import controller


class CadastroPlantas(QWidget):
    def __init__(self):
        super().__init__() 
        self.controller = controller()  
        self.imagem_path = ""  
        self.initUI()

    def botao_clicado(self):
        nome_popular = self.input_nome_popular.text().strip()
        nome_cientifico = self.input_nome_cientifico.text().strip()
       
        if not nome_popular or not nome_cientifico:
            QMessageBox.critical(self, "Erro", "Preencha todos os campos!")  
            return  

        planta_id = self.controller.salvar_planta(nome_popular, nome_cientifico, self.imagem_path)

        if planta_id:
            QMessageBox.information(self, "Sucesso", "Planta cadastrada com sucesso!")  
            self.input_nome_popular.clear()
            self.input_nome_cientifico.clear()
            self.area_imagem.clear()
            self.imagem_path = ""
        else:
            QMessageBox.critical(self, "Erro", "Erro ao cadastrar a planta.")  

    def initUI(self):
        self.setWindowTitle("Cadastro de Plantas") 
        self.setGeometry(100, 100, 300, 400) 
        self.setStyleSheet("background-color: rgb(107, 48, 103;")

        layout = QVBoxLayout() 

        titulo = QLabel("Faça o cadastro :)")
        titulo.setFont(QFont("Arial", 14, QFont.Bold))  
        titulo.setStyleSheet("color: #245336;")  
        self.setStyleSheet('background-color: #F0FFF0;')
        titulo.setAlignment(Qt.AlignCenter)

        self.input_nome_popular = QLineEdit()
        self.input_nome_popular.setPlaceholderText("Nome Popular")  
        self.input_nome_popular.setStyleSheet("background-color: white;")  

        
        self.input_nome_cientifico = QLineEdit()
        self.input_nome_cientifico.setPlaceholderText("Nome Científico")
        self.input_nome_cientifico.setStyleSheet("background-color: white;")

        self.botao_imagem = QPushButton("Insira uma Imagem")
        self.botao_imagem.setStyleSheet("background-color: white; color: rgb(107, 48, 103;") 
        self.botao_imagem.clicked.connect(self.abrir_arquivo)  
        self.area_imagem = QLabel()
        self.area_imagem.setAlignment(Qt.AlignCenter)  
        self.area_imagem.setStyleSheet("border: 1px solid black; min-height: 100px; background-color:rgb(68, 129, 99);")  

        botao_cancelar = QPushButton("Cancelar")
        botao_cancelar.setStyleSheet("background-color: white; color: rgb(107, 48, 103;") 

        botao_cadastrar = QPushButton("Cadastrar")
        botao_cadastrar.setStyleSheet("background-color: white; color: rgb(107, 48, 103;")  
        botao_cadastrar.clicked.connect(self.botao_clicado)  

        layout.addWidget(titulo)
        layout.addWidget(self.input_nome_popular)
        layout.addWidget(self.input_nome_cientifico)
        layout.addWidget(self.botao_imagem)
        layout.addWidget(self.area_imagem)
        layout.addWidget(botao_cancelar)
        layout.addWidget(botao_cadastrar)

        self.setLayout(layout) 

    def abrir_arquivo(self):
        options = QFileDialog.Options()  
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Abrir Arquivo", "", "Imagens (*.png *.jpg *.jpeg *.bmp *.gif);;Todos os Arquivos (*)", options=options
        )
        if file_name: 
            self.imagem_path = file_name 
            pixmap = QPixmap(file_name) 
            self.area_imagem.setPixmap(pixmap.scaled(200, 200, Qt.KeepAspectRatio)) 



