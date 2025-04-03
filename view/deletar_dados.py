from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QMessageBox
from controller.controller import controller


class DeletarDado(QWidget):
    def __init__(self, id):
        super().__init__()
        self.id = id 
        self.controller = controller()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Deletar Planta")
        self.setGeometry(600, 300, 300, 150)

        layout = QVBoxLayout()

        label = QLabel(f"Tem certeza que deseja deletar o registro ID {self.id}?")
        layout.addWidget(label)

        botao_confirmar = QPushButton("Confirmar")
        botao_confirmar.clicked.connect(self.deletar_dado)
        layout.addWidget(botao_confirmar)

        botao_cancelar = QPushButton("Cancelar")
        botao_cancelar.clicked.connect(self.close)
        layout.addWidget(botao_cancelar)

        self.setLayout(layout)

    def deletar_dado(self):
        sucesso = self.controller.deletar_registro(self.id)

        if sucesso:
            QMessageBox.information(self, "Sucesso", "Registro deletado com sucesso!")
        else:
            QMessageBox.critical(self, "Erro", "Erro ao deletar o registro.")

        self.close()
