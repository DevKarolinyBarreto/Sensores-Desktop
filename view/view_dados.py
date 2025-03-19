import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QFileDialog, QMessageBox,  QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt

from controller.controller import controller
from view.editar_planta import editar_planta

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



