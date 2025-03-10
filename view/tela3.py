import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QFileDialog, QMessageBox
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt

from controller.controller2 import controller2

class Dados(QWidget):
    def __init__(self):
        super().__init__() 
        self.controller2 = controller2()
        self.initUI()

    def enviadados(self):
        temperatura = self.input_temperatura.text().strip()
        luminosidade = self.input_luminosidade.text().strip()
        umidade = self.input_umidade.text().strip()

        if not temperatura or not luminosidade or not umidade:
            QMessageBox.critical(self, "Erro", "Preencha todos os campos!")  
            return  
        
        dados_id = self.controller2.dados_plantas(temperatura, luminosidade, umidade)

        if dados_id:
            QMessageBox.information(self, "Sucesso", "Dados enviados com sucesso!")  
            self.input_temperatura.clear()
            self.input_luminosidade.clear()
            self.input_umidade.clear()
        else:
            QMessageBox.critical(self, "Erro", "Erro ao enviar dados.")  

    def initUI(self):
        self.setWindowTitle("Dados das plantas") 
        self.setGeometry(100, 100, 300, 400) 
        self.setStyleSheet("background-color: rgb(107, 48, 103;")

        layout = QVBoxLayout() 

        dados = QLabel("Envie os dados :)")
        dados.setFont(QFont("Arial", 14, QFont.Bold))  
        dados.setStyleSheet("color: #245336;")  
        self.setStyleSheet('background-color: #F0FFF0;')
        dados.setAlignment(Qt.AlignCenter)

        self.input_temperatura = QLineEdit()
        self.input_temperatura.setPlaceholderText("Insira a temperatura")  
        self.input_temperatura.setStyleSheet("background-color: white;")  

        self.input_luminosidade = QLineEdit()
        self.input_luminosidade.setPlaceholderText("Insira a luminosidade")
        self.input_luminosidade.setStyleSheet("background-color: white;") 

        self.input_umidade = QLineEdit()
        self.input_umidade.setPlaceholderText("Insira a umidade")
        self.input_umidade.setStyleSheet("background-color: white;") 

        
        botao_cancelar = QPushButton("Cancelar")
        botao_cancelar.setStyleSheet("background-color: white; color: rgb(107, 48, 103;") 

        botao_cadastrar = QPushButton("Cadastrar")
        botao_cadastrar.setStyleSheet("background-color: white; color: rgb(107, 48, 103;")  
        botao_cadastrar.clicked.connect(self.enviadados)  

        
        layout.addWidget(dados)
        layout.addWidget(self.input_temperatura)
        layout.addWidget(self.input_luminosidade)
        layout.addWidget(self.input_umidade)
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