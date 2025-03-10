import sys

from PyQt5.QtWidgets import QApplication, QWidget
from view.tela2 import CadastroPlantas

if __name__ == "__main__":
    app = QApplication(sys.argv) 
    janela = CadastroPlantas() 
    janela.show() 
    sys.exit(app.exec_())  