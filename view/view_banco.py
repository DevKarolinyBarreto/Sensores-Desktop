import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QFileDialog, QMessageBox,  QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt

from controller.controller import controller

class view_plantas(QWidget):
    def __init__(self):
        super().__init__()
        self.controller = controller()
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

    def carregar_dados(self):
        dados = self.controller.obter_plantas()
        self.tabela.setRowCount(len(dados))

        for row, planta in enumerate(dados):
            self.tabela.setItem(row, 0, QTableWidgetItem(str(planta[0])))
            self.tabela.setItem(row, 1, QTableWidgetItem(planta[1]))
            self.tabela.setItem(row, 2, QTableWidgetItem(planta[2]))

