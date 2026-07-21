#Crie a classe Caneta, que simule o funcionamento de uma caneta clorida, 
#podendo escrever frases na cor relativa.

from rich import print

class Caneta: 

    def __init__(self, cor):
        self.cor = cor

    def escrever(self, frase):
        print(f'[{self.cor}]{frase}[/{self.cor}]')

        
f1 = Caneta(cor = 'yellow')
f1.escrever('Ola, como vai voce? ')