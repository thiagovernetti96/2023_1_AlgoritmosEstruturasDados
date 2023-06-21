from Livro import Livro
from Pilha import Pilha

l1 = Livro("A Rosa","César",100)
l2 = Livro("Harry Potter", "J.K Rowling",500)
l3 = Livro("O tempo e o vento","Érico Veríssimo",1000)

pilha = Pilha()

pilha.imprimir()
pilha.add(l1)
pilha.add(l2)
pilha.add(l3)
pilha.imprimir()
pilha.remover()
pilha.remover()
pilha.remover()
