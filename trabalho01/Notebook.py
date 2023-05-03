from Computador import Computador
class Notebook(Computador):
    def __init__(self, modelo, cor, preco,__tempoDeBateria):
        super().__init__(modelo, cor, preco)
        self.__tempoDeBateria = __tempoDeBateria

    def getTempodeBateria(self):
        return self.__tempoDeBateria



    def getInformacoes(self):
        return str(super().getInformacoes())+ " " + str(self.getTempodeBateria())

    
    def cadastrar(self):
        print("Notebook foi cadastrado")