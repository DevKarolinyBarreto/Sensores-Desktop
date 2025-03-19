import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QFileDialog, QMessageBox,  QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt

from controller.controller import controller
from view.editar_planta import editar_planta

class view_plantas(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Plantas cadastradas ❋')    
        self.setGeometry(500, 100, 400, 300)
        layout = QVBoxLayout()
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(3)
        self.tabela.setHorizontalHeaderLabels (["ID", "Nome Popular", "Nome Científico"])
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

    def carregar_dados(self):
    
        dados = self.controller = controller()
        dados2 = self.controller.obter_plantas()
    
        if not dados2: 
            return 

        self.tabela.setRowCount(len(dados2))
        
        for row, planta in enumerate(dados2):
            self.tabela.setItem(row, 0, QTableWidgetItem(str(planta[0])))
            self.tabela.setItem(row, 1, QTableWidgetItem(planta[1]))
            self.tabela.setItem(row, 2, QTableWidgetItem(planta[2]))

     
    def abrir_tela_edicao(self):
        linha_selecionada = self.tabela.currentRow()

        if linha_selecionada != -1:
            planta_id = int(self.tabela.item(linha_selecionada, 0).text())
            nome_popular = self.tabela.item(linha_selecionada, 1).text()
            nome_cientifico = self.tabela.item(linha_selecionada, 2).text()

            self.tela_edicao = editar_planta(planta_id, nome_popular, nome_cientifico)
            self.tela_edicao.show()
            self.close()



