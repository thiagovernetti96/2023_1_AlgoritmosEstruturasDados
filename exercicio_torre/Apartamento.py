from Torre import Torre 
class Apartamento(Torre):
    def __init__(self,numero,torre):
        self.id = None
        self.numero = numero
        self.torre = torre
        self.vaga = None
        self.proximo = None

    def __str__(self) :
        texto = "\n----------------------------"
        texto += "\nNúmero" +self.numero
        texto+= "\nEndereço: " + self.torre.endereco
        return texto 


    def cadastrar(self):
        print("Apartamento registrado com sucesso")


    def imprimir(self):
        pass

        

