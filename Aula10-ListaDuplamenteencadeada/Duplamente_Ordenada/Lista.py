from No import No

class Lista:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0
    
    def add(self, valor):
        nodo = No(valor)
        if self.inicio == None:
            self.inicio = nodo
            self.fim = nodo 
        else:
         self.fim.proximo = nodo
        self.tamanho += 1
        self.imprimir()
        
    def imprimir(self):
        print("---------------------")
        if self.inicio == None:
            print("Lista Vazia!")
        else:
            aux = self.inicio
            while aux :
                print( aux.dado )
                aux = aux.proximo
            print( "Tamanho: ", str(self.tamanho))

    def imprimirreverso(self):
        print("---------------------")
        if self.inicio == None:
            print("Lista Vazia!")
        else:
            aux = self.fim
            while aux :
                print( aux.dado )
                aux = aux.anterior
            print( "Tamanho: ", str(self.tamanho))   

    
             
            
    def removerDoFim(self):
        if self.inicio == None:
            print("Lista Vazia!")
        elif self.inicio.proximo == None:
            self.inicio = None
            self.fim = None
            self.tamanho = 0
        else:
            self.fim = self.fim.anterior
            self.fim.proximo = None
            self.tamanho -= 1
        self.imprimir()   

    def removerDoInicio(self):
        if self.inicio == None:
            print("Lista Vazia!")
        elif self.inicio.proximo == None:
            self.inicio = None
            self.fim = None
            self.tamanho = 0
        else:
            self.inicio = self.inicio.proximo
            self.inicio.anterior = None
            self.tamanho -= 1
        self.imprimir()
