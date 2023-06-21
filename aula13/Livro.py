class Livro:
    def __init__(self,titulo,autor,pg):
        self.titulo = titulo
        self.autor = autor
        self.paginas = pg
        self.proximo = None

    def __str__(self):
        texto ="----------------------"
        texto += "\nTítulo: " + self.titulo
        texto += "\nAutor: " + self.autor
        texto += "\nTítulo: " + str(self.paginas)
        return texto

    
    def remover(self,):
        if self.primeiro == None:
            print("Nenhum valor removível")
        elif self.proximo == None:
            self.primeiro = None
            self.quantidade-= 1
        else:
            self.proximo= None
            self.quantidade -= 1
    
    