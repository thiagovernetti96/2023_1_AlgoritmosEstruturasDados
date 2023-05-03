from Computador import Computador
class Desktop(Computador):
    def __init__(self, modelo, cor, preco, _potenciaDaFonte):
        super().__init__(modelo, cor, preco)
        self._potenciaDaFonte = _potenciaDaFonte

    def getPotenciaDaFonte(self):
        return self._potenciaDaFonte


    def getInformacoes(self):
        return str(super().getInformacoes())+ " " + str(self.getPotenciaDaFonte())
        

    

    def cadastrar(self):
       print("O Desktop foi cadastrado") 