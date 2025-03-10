from model.model2 import Model2

class controller2:
    def __init__(self):
        self.model = Model2()

    def dados_plantas(self, temperatura, luminosidade, umidade):   
        if temperatura and luminosidade and umidade:
            return self.model.dados_plantas(temperatura, luminosidade, umidade)
        return None