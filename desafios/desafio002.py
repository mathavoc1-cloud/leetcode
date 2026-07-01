#Crie uma classe Produto, onde podemos cadastrar nome e o preco. Crie tambem um metodo que mostre uma etiqueta de preco do produto.

from rich import print
from rich.panel import Panel
from rich.text import Text

class Produto:

    def __init__(self, nome, preco):

        self.nome = nome
        self.preco = preco

    def etiqueta (self):
     conteudo = Text(justify='center')
     conteudo.append(f'{self.nome}\n{'-' * 30}\n{"." * 10}R${self.preco:.2f}{"."*10}')
     print(Panel(conteudo, title = 'Produto', width = 35 ))


p1 = Produto(nome = "iPhone 17 Pro Max", preco = 1300)
p2 = Produto(nome = "Mouse", preco = 120)

        
p1.etiqueta()
p2.etiqueta()