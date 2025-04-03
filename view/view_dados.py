# arrumar o botao de deletar

import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QFileDialog, QMessageBox,  QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt

from controller.controller import controller
from view.editar_dados import editar_dados
from view.deletar_dados import DeletarDado

class view_dados(QWidget):
    def __init__(self):
        super().__init__()
        self.controller = controller()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Dados cadastrados ❋')    
        self.setGeometry(500, 100, 400, 300)
        layout = QVBoxLayout()
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(4)
        self.tabela.setHorizontalHeaderLabels (["id", "temperatura", "luminosidade","umidade"])
        layout.addWidget(self.tabela)

        botao_atualizar = QPushButton("Atualizar") 
        botao_atualizar.clicked.connect(self.carregar_dados)
        layout.addWidget(botao_atualizar)
        self.setLayout(layout)
        self.carregar_dados()

        botao_edicao = QPushButton("Editar") 
        botao_edicao.clicked.connect(self.abrir_tela_edicao)
        layout.addWidget(botao_edicao)
        self.setLayout(layout)
        self.abrir_tela_edicao()

        botao_deletar = QPushButton("Deletar")
        botao_deletar.clicked.connect(self.abrir_tela_delete)
        layout.addWidget(botao_deletar)

    def carregar_dados(self):
        self.controller = controller()
        dados2 = self.controller.obter_dados()
    
        if not dados2: 
            return 

        self.tabela.setRowCount(len(dados2))
        
        for row, dados in enumerate(dados2):
            self.tabela.setItem(row, 0, QTableWidgetItem(str(dados[0])))
            self.tabela.setItem(row, 1, QTableWidgetItem(str(dados[1])))
            self.tabela.setItem(row, 2, QTableWidgetItem(str(dados[2])))
            self.tabela.setItem(row, 3, QTableWidgetItem(str(dados[3])))

            self.tabela.viewport().update()

    
    def abrir_tela_edicao(self):
        linha_selecionada = self.tabela.currentRow()

        if linha_selecionada != -1:
            id = int(self.tabela.item(linha_selecionada, 0).text())
            temperatura = self.tabela.item(linha_selecionada, 1).text()
            umidade = self.tabela.item(linha_selecionada, 2).text()
            luminosidade = self.tabela.item(linha_selecionada, 3).text()

            self.tela_edicao = editar_dados(id, luminosidade, umidade, temperatura)
            self.tela_edicao.show()
            self.close()  


    def abrir_tela_delete(self):
        linha_selecionada = self.tabela.currentRow()
        
        if linha_selecionada == -1:
            QMessageBox.warning(self, "Aviso", "Selecione um item primeiro!")
            return
        
        try:
            id = self.tabela.item(linha_selecionada, 0)
            if id is None:
                raise ValueError("Nenhum ID encontrado na linha selecionada.")
            
            id = int(id.text())
            print(f"ID Selecionado para Deletar: {id}")
            
            self.tela_delete = DeletarDado(id)
            self.tela_delete.show()
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro: {str(e)}")







