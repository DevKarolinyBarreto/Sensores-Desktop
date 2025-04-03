from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QMessageBox
from controller.controller import controller

class editar_planta(QWidget):
    def __init__(self, planta_id, nome_popular, nome_cientifico):
        super().__init__()
        self.planta_id = planta_id
        self.controller = controller()

        self.initUI(nome_popular, nome_cientifico)

    def initUI(self, nome_popular, nome_cientifico):
        self.setWindowTitle("Editar Planta")
        self.setGeometry(600, 300, 300, 200)

        layout = QVBoxLayout()

        self.nome_popular_input = QLineEdit()
        self.nome_popular_input.setText(nome_popular)
        layout.addWidget(QLabel("Nome Popular:"))
        layout.addWidget(self.nome_popular_input)

        self.nome_cientifico_input = QLineEdit()
        self.nome_cientifico_input.setText(nome_cientifico)
        layout.addWidget(QLabel("Nome Científico:"))
        layout.addWidget(self.nome_cientifico_input)

        botao_salvar = QPushButton("Salvar")
        botao_salvar.clicked.connect(self.salvar_dados)
        layout.addWidget(botao_salvar)

        self.setLayout(layout)

    def salvar_dados(self):
        nome_popular = self.nome_popular_input.text()
        nome_cientifico = self.nome_cientifico_input.text()

        if not nome_popular or not nome_cientifico:
            QMessageBox.warning(self, "Aviso", "Preencha todos os campos.")
            return

        sucesso = self.controller.atualizar_planta(self.planta_id, nome_popular, nome_cientifico)

        if sucesso:
            QMessageBox.information(self, "Sucesso", "Planta atualizada com sucesso!")
            self.close()
        else:
            QMessageBox.critical(self, "Erro", "Erro ao atualizar planta.")

