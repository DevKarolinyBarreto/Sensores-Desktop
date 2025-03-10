import sys

from PyQt5.QtWidgets import QApplication, QWidget
from view.tela3 import Dados

if __name__ == "__main__":
    app = QApplication(sys.argv) 
    janela = Dados() 
    janela.show() 
    sys.exit(app.exec_())  