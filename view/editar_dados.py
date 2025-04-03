from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QMessageBox
from controller.controller import controller

class editar_dados(QWidget):
    def __init__(self, id, luminosidade, temperatura, umidade):
        super().__init__()
        self.id = id
        self.controller = controller()

        self.initUI(luminosidade, temperatura, umidade)

    def initUI(self, luminosidade, temperatura, umidade):
        self.setWindowTitle("Editar dados")
        self.setGeometry(600, 300, 300, 200)

        layout = QVBoxLayout()

        self.temperatura = QLineEdit()
        self.temperatura.setText(temperatura)
        layout.addWidget(QLabel("Temperatura:"))
        layout.addWidget(self.temperatura)

        self.luminosidade = QLineEdit()
        self.luminosidade.setText(luminosidade)
        layout.addWidget(QLabel("Luminosidade:"))
        layout.addWidget(self.luminosidade)

        self.umidade = QLineEdit()
        self.umidade.setText(umidade)
        layout.addWidget(QLabel("Umidade:"))
        layout.addWidget(self.umidade)

        botao_salvar = QPushButton("Salvar")
        botao_salvar.clicked.connect(self.salvar_dados)
        layout.addWidget(botao_salvar)

        self.setLayout(layout)

    def salvar_dados(self):
        temperatura = self.temperatura.text()
        luminosidade = self.luminosidade.text()
        umidade = self.umidade.text()

        if not temperatura or not umidade or not luminosidade:
            QMessageBox.warning(self, "Aviso", "Preencha todos os campos.")
            return

        sucesso = self.controller.atualizar_dados(self.id, temperatura, luminosidade, umidade)

        if sucesso:
            QMessageBox.information(self, "Sucesso", "Dados atualizados com sucesso!")
            self.close()
        else:
            QMessageBox.critical(self, "Erro", "Erro ao atualizar dados.")

