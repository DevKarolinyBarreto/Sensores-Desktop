import sys
import os

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QFileDialog, QMessageBox, QMainWindow
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt

from view.tela2 import CadastroPlantas
from view.tela3 import Dados
from view.view_banco import view_plantas
from view.view_dados import view_dados

class tela1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.window_st = CadastroPlantas()
        self.window_st2 = Dados() 
        self.window_st3 = view_plantas()
        self.window_st4 = view_dados()

    def start1(self):
        self.window_st.show()

    def start2(self):
           self.window_st2.show()

    def start3(self):
            self.window_st3.show() 

    def start4(self):
            self.window_st4.show()                 

    def initUI(self):
        self.setWindowTitle("Tela principal") 
        self.setGeometry(100, 100, 300, 400) 
        self.setStyleSheet("background-color: rgb(107, 48, 103;")

        layout = QVBoxLayout()
        titulo = QLabel("Selecione uma ação ❋ ")
        titulo.setFont(QFont("Arial", 14, QFont.Bold))  
        titulo.setAlignment(Qt.AlignCenter) 

        botao_cadastrar = QPushButton("Cadastrar uma planta ")
        botao_cadastrar.setStyleSheet("background-color: white; color: rgb(107, 48, 103;") 
        botao_cadastrar.clicked.connect(self.start1) 

        botao_enviar = QPushButton("Enviar dados sobre uma planta ")
        botao_enviar.setStyleSheet("background-color: white; color: rgb(107, 48, 103;")  
        botao_enviar.clicked.connect(self.start2) 

        botao_view = QPushButton("Ver plantas cadastradas")
        botao_view.setStyleSheet("background-color: white; color: rgb(107, 48, 103;")  
        botao_view.clicked.connect(self.start3) 

        botao_view2 = QPushButton("Ver dados")
        botao_view2.setStyleSheet("background-color: white; color: rgb(107, 48, 103;")  
        botao_view2.clicked.connect(self.start4) 

        layout.addWidget(titulo)
        layout.addWidget(botao_cadastrar)
        layout.addWidget(botao_enviar)
        layout.addWidget(botao_view)
        layout.addWidget(botao_view2)

        dados = QLabel("Envie os dados:)")
        dados.setFont(QFont("Arial", 14, QFont.Bold))  
        dados.setStyleSheet("color: #245336;")  
        self.setStyleSheet('background-color: #F0FFF0;')
        dados.setAlignment(Qt.AlignCenter)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv) 
    janela = tela1() 
    janela.show() 
    sys.exit(app.exec_())  