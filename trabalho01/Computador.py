class Computador:
    def __init__(self,modelo,cor,preco) :
        self.modelo = modelo
        self.cor = cor 
        self.preco = preco
    
    def getInformacoes(self):
      return self.modelo , self.cor , self.preco


    def cadastrar(self):
        pass