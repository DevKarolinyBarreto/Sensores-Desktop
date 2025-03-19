import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QFileDialog, QMessageBox,  QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt

from controller.controller import controller

class editar_planta(QWidget):
    def __init__(self, planta_id, nome_popular, nome_cientifico):
        super().__init__()
        self.controller = controller()
        self.planta_id = planta_id
        self.initUI(nome_popular, nome_cientifico)
        

    def initUI(self, nome_popular, nome_cientifico):
        self.setWindowTitle('Editar plantas ❋')    
        self.setGeometry(500, 150, 300, 200)

        layout = QVBoxLayout()

        self.nome_popular_input = QLineEdit(nome_popular)
        self.nome_cientifico_input = QLineEdit(nome_cientifico)
        self.salvar_button = QPushButton("Salvar alterações")
        self.salvar_button.clicked.connect(self.salvar_edicao)


        layout.addWidget(QLabel("Nome popular: "))
        layout.addWidget(self.nome_popular_input)

        layout.addWidget(QLabel("Nome cientifico: "))
        layout.addWidget(self.nome_cientifico_input)

        layout.addWidget(self.salvar_button)

        self.setLayout(layout)

    def salvar_edicao(self):
        nome_popular = self.nome_popular_input.text().strip()
        nome_cientifico = self.nome_cientifico_input.text().strip()

        if not nome_popular or not nome_cientifico:
            QMessageBox.critical(self, "Erro", "Preencha todos os campos!")
            return
        else:
            QMessageBox.information(self, "Sucesso", "Planta atualizada com sucesso!")  
     
        self.controller.atualizar_planta(self.planta_id, nome_popular, nome_cientifico)

        self.close()

    

  