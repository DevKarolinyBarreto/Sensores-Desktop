import sys
from PyQt5.QtWidgets import QApplication
from view.view_banco import view_plantas

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = view_plantas()
    janela.show()
    sys.exit(app.exec_())