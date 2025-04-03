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
    
    def atualizar_planta(self, planta_id, nome_popular, nome_cientifico):
        if nome_popular and nome_cientifico:
            return self.model.update_planta(nome_popular, nome_cientifico, planta_id)
   
    def atualizar_dados(self, id, luminosidade, umidade, temperatura):
        if luminosidade and temperatura and umidade:
            return self.model.update_dados(id, luminosidade, umidade, temperatura)

    def deletar_registro(self, dado_id):
        return self.model.delete_dado(dado_id)