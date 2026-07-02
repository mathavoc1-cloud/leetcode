#Crie a classe livro que vai simular a passagem da paginas de um livro considerando tambem 
#se o usuario chegou ao fim da leitura
from rich import print
from time import sleep

class Livro:

    def __init__(self, nome, paginas = 0):
        self.nome = nome
        self.paginas = paginas
        self.paginas_faltando = 0
        self.paginas_total = 0

    def etiqueta(self):
        conteudo = f"Voce acabou de abrir o livro '{self.nome}' que tem {self.paginas} no total. Voce agora esta na pagina {self.paginas_faltando}"
        print(conteudo)

    def analisar(self):
        self.paginas_faltando = self.paginas - self.paginas_total

    def virar_pagina(self, qtd = 1):
        for i in range(qtd):
            if self.paginas_total < self.paginas:
                self.paginas_total += 1
                sleep(0.2)
                print(f'Virando para a pagina {self.paginas_total}...')
                sleep(0.2)
            else:
                print('[red]Voce chegou ao fim do livro![/red]')
        self.analisar()
        print(f'Voce avancou {self.paginas_total} e agora faltam {self.paginas_faltando} pagina(s)')



l1 = Livro(nome = "O Alqumimsta", paginas = 20)

l1.virar_pagina(21)