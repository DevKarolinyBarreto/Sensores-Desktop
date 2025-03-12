from model.model import Model

class controller:
    def __init__(self):
        self.model = Model()

    def salvar_planta(self, nome_popular, nome_cientifico, imagem_path):   
        if nome_popular and nome_cientifico:
            return self.model.inserir_plantas(nome_popular, nome_cientifico, imagem_path)
        return None
    
    def obter_plantas(self):
        return self.model.listar()
    
    def obter_dados(self):
        return self.model.listar2()